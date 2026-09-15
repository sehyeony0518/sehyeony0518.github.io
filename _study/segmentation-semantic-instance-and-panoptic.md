---
layout: study_note
title: "Segmentation: Resolution Against Context, and the Things/Stuff Divide"
description: "Every segmentation architecture is an answer to one conflict — you need to see widely and label precisely, and pooling buys the first with the second. Four answers, and why panoptic needed a new output format."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 12
source: "Independent study"
written: true
updated: "2026-09-15"
---

Segmentation is structurally simpler than detection, and for a reason worth naming: **the output shape is known in advance.** A detector does not know how many boxes it will emit. A segmenter emits $$H\times W\times C$$ — one label per pixel — whatever the image contains. Much of detection's machinery (anchors, suppression, variable-length output) exists to manage that uncertainty and simply has no counterpart here.

What replaces it is a different conflict, and it is the organising problem of the whole field.

## Core question and definition

Three tasks, and the distinction is not pedantic:

- **Semantic segmentation** labels each pixel with a class. Every sheep is "sheep."
- **Instance segmentation** separates individual objects. Each sheep gets its own identity — but only *things*, the countable objects. Grass and sky have no instances to count.
- **Panoptic segmentation** does both: instance identities for **things**, class labels for **stuff**, with every pixel assigned exactly once.[^panoptic]

The things/stuff divide is the reason instance segmentation cannot simply replace semantic segmentation. "How many grasses are in this image" has no answer, and an architecture built around counting objects has nothing to say about the pixels that are not objects.

## Key concepts

### The conflict: seeing widely versus labelling precisely

To label a pixel correctly you need context — global context, often. A patch of grey could be road or roof, and only the surrounding scene decides. So the network needs a large receptive field.

But you also need the *output at full resolution*, one label per pixel, with boundaries in the right place.

Pooling gives you the first by destroying the second. At output stride 16, spatial detail is reduced 16× per axis — 256× in area — before any upsampling recovers a thing. And the obvious alternative, simply using larger filters, fails on three counts: parameters grow quadratically, training gets harder, and the *effective* receptive field grows far more slowly than the theoretical one.

Every architecture below is an answer to this one conflict.

### Answer 1: encoder–decoder

Downsample to get context, then upsample to recover resolution, and feed the encoder's high-resolution features across to the decoder so the detail is not reconstructed from nothing.

SegNet does the upsampling by remembering **which** position each max-pool value came from and returning it there.[^segnet] It is information-efficient and, in practice, an awkward operation — irregular memory access, poorly suited to the hardware everything else is tuned for.

U-Net instead concatenates encoder feature maps into the decoder and upsamples with learned transposed convolutions.[^unet] It is the design that stuck, and it is worth noting it was built for biomedical segmentation first and generalised outward — the unusual direction of travel.

### Answer 2: atrous convolution, which is the elegant one

Insert gaps into the filter. A $$3\times3$$ kernel with dilation rate $$r$$ spans $$(2r+1)\times(2r+1)$$ while still holding exactly **9 parameters**:

| rate | effective size | positions spanned | parameters |
|---|---|---|---|
| 1 | $$3\times3$$ | 9 | 9 |
| 2 | $$5\times5$$ | 25 | 9 |
| 6 | $$13\times13$$ | 169 | 9 |
| 12 | $$25\times25$$ | 625 | 9 |
| 18 | $$37\times37$$ | 1369 | 9 |

At rate 18 the filter sees 152 times the area per parameter that a dense $$3\times3$$ does. And stacking compounds it: rates 1, 2, 4, 8 in sequence give receptive fields of $$3, 7, 15, 31$$ — a $$31\times31$$ view from four layers and 36 parameters, with **no downsampling at all**.[^deeplab]

That is the whole trick. Context without resolution loss, at no parameter cost.

The implementation is not literal — nobody multiplies by the inserted zeros. It is done by rearranging the tensor (`space_to_batch`, convolve densely, `batch_to_space`), so the zeros never exist.

### Answer 3: spatial pyramid pooling, and the combination

Pool the feature map to several different scales, convolve each, upsample, and concatenate.[^spp] A feature pooled to $$1\times1$$ has seen the entire image; one pooled less has seen a neighbourhood. Concatenating gives the classifier evidence at several ranges at once.

**ASPP** is the two combined: parallel atrous convolutions at rates 6, 12, 18 — effective fields $$13, 25, 37$$ — plus a $$1\times1$$ convolution and global image pooling, all concatenated. DeepLab v3+ wraps ASPP in a light encoder–decoder to sharpen boundaries, which is all four answers in one network.[^deeplabv3p]

### The panoptic trick: predict centres, then regress to them

Mask R-CNN gets instance masks by adding a mask branch to Faster R-CNN — detect the box, then segment inside it.[^mask] Segmenting inside a box is easy: the object fills the crop, the scale is normalised, so a few convolutions suffice. But it inherits detection's output format, so masks can overlap and stuff is not handled.

Panoptic-DeepLab's answer avoids detection entirely, and it is the part of this I find most instructive. Output $$C+3$$ channels per pixel:[^pandeeplab]

- $$C$$ channels: the semantic class, exactly as before.
- **1 channel: centre prediction** — is this pixel an instance's centre of mass? Non-maximum suppression on this heatmap yields one point per object.
- **2 channels: centre regression** — a vector from this pixel to its own instance's centre.

Group pixels by which predicted centre their offset vector points at. That yields instances **without knowing their classes**, which are then read off from the semantic branch.

What makes this worth studying is that it turns instance segmentation into pixel-wise regression. Boxes, anchors, suppression over boxes — all gone, replaced by a vector field. And the same machinery extends: ViP-DeepLab adds a depth channel and regresses centres to the *previous* frame's centres, which makes tracking fall out as a by-product rather than a separate system.[^vip] The offsets across frames are large, which is why its regression branch stacks ASPP four times — the receptive field has to cover the motion.

## Why it matters for my work

The **things/stuff distinction maps onto medical imaging directly**, and I had not had a name for it. A lesion is a thing — countable, individually identified, and the count is often the clinical finding. Tissue, fat, parenchyma, background are stuff — a region with no instances. A pipeline that segments only things cannot describe the organ; one that segments only stuff cannot count the lesions. The panoptic formulation is the one that matches what a report actually contains, and I suspect it is underused in medical work relative to how well it fits.

The resolution-versus-context tension has a specific clinical edge too. Deciding whether a small finding is pathological requires the finding at full resolution *and* the anatomical context around it — which is exactly the conflict, and exactly what a radiologist does by alternating zoom levels. Atrous convolution is the cleanest answer available, because it does not force the trade: the same 9 parameters see a $$37\times37$$ neighbourhood with no pixels discarded.

The overlap point deserves care in reporting. Instance segmentation permits a pixel to belong to several objects at once (a person and their tie); panoptic forbids it, assigning each pixel exactly once. For a finding that legitimately falls inside two structures, the panoptic constraint forces a choice the image does not support — which is a modelling assumption that will show up as an error rate without ever being described as an assumption.

## What I have not resolved

Whether centre-of-mass is a usable instance representation for lesion shapes. It presumes a centre that lies inside the object and is unambiguous. A crescent-shaped or hollow lesion has a centre of mass outside itself, and a diffuse or irregular one has no stable centre at all. Detection's box has the same weakness in a milder form; I do not know whether anyone has measured how far this degrades on non-convex medical structures, or whether the field has simply worked on objects where it happens to hold.

---

[^panoptic]: Kirillov, A., He, K., Girshick, R., Rother, C., & Dollár, P. (2019). Panoptic segmentation. *CVPR*. [10.1109/CVPR.2019.00963](https://doi.org/10.1109/CVPR.2019.00963)

[^segnet]: Badrinarayanan, V., Kendall, A., & Cipolla, R. (2017). SegNet: A deep convolutional encoder-decoder architecture for image segmentation. *IEEE TPAMI*, 39(12), 2481–2495. [10.1109/TPAMI.2016.2644615](https://doi.org/10.1109/TPAMI.2016.2644615)

[^unet]: Ronneberger, O., Fischer, P., & Brox, T. (2015). U-Net: Convolutional networks for biomedical image segmentation. *MICCAI*. [10.1007/978-3-319-24574-4_28](https://doi.org/10.1007/978-3-319-24574-4_28)

[^deeplab]: Chen, L.-C., Papandreou, G., Kokkinos, I., Murphy, K., & Yuille, A. L. (2018). DeepLab: Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected CRFs. *IEEE TPAMI*, 40(4), 834–848. [10.1109/TPAMI.2017.2699184](https://doi.org/10.1109/TPAMI.2017.2699184)

[^spp]: He, K., Zhang, X., Ren, S., & Sun, J. (2015). Spatial pyramid pooling in deep convolutional networks for visual recognition. *IEEE TPAMI*, 37(9), 1904–1916. [10.1109/TPAMI.2015.2389824](https://doi.org/10.1109/TPAMI.2015.2389824)

[^deeplabv3p]: Chen, L.-C., Zhu, Y., Papandreou, G., Schroff, F., & Adam, H. (2018). Encoder-decoder with atrous separable convolution for semantic image segmentation. *ECCV*. [10.1007/978-3-030-01234-2_49](https://doi.org/10.1007/978-3-030-01234-2_49)

[^mask]: He, K., Gkioxari, G., Dollár, P., & Girshick, R. (2017). Mask R-CNN. *ICCV*. [10.1109/ICCV.2017.322](https://doi.org/10.1109/ICCV.2017.322)

[^pandeeplab]: Cheng, B., et al. (2020). Panoptic-DeepLab: A simple, strong, and fast baseline for bottom-up panoptic segmentation. *CVPR*. [10.1109/CVPR42600.2020.01249](https://doi.org/10.1109/CVPR42600.2020.01249)

[^vip]: Qiao, S., Zhu, Y., Adam, H., Yuille, A., & Chen, L.-C. (2021). ViP-DeepLab: Learning visual perception with depth-aware video panoptic segmentation. *CVPR*. [10.1109/CVPR46437.2021.00399](https://doi.org/10.1109/CVPR46437.2021.00399)
