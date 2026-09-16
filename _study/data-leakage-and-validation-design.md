---
layout: study_note
title: "Data Leakage and Validation Design"
description: "How information crosses from test to train in medical data, and what each validation design can claim."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-01-08-busbra-breast-ultrasound-dataset"
  - "2025-11-03-transfer-learning-liver-steatosis"
---

A held-out result estimates performance for a particular sampling and information-access scheme. Leakage occurs when development or prediction gains information that would be unavailable under the intended scheme. The central issue is the claim the estimate represents.

## Core question and definition

Before dividing data, specify:

- Who the future patient is relative to development patients.
- Which information exists at prediction time.
- What unit receives the prediction and subsequent action.
- Which outcomes will establish correctness.
- Which development decisions may use which data.

Two boundaries matter.

**The evaluation boundary** separates model development from information used to estimate its performance.

**The prediction-time boundary** separates information available when the decision is made from information that appears later.

Patient overlap, full-data feature selection, repeated test inspection, and post-decision inputs cross different boundaries. They should not be treated as one undifferentiated problem.

Likewise, dependence among test images and leakage between training and test data are different. Dependence can invalidate an uncertainty estimate without biasing the mean. Training-test patient overlap can change the task itself and inflate mean performance.

## Key concepts

### 1. Define the risk before choosing a split

Let a fitted pipeline be $$f_{\mathcal D}$$, where $$\mathcal D$$ includes all development information used to choose preprocessing, model parameters, calibration, and the decision rule.

For an intended population $$P$$, its risk is

$$
R_P(f_{\mathcal D})
=
\mathbb E_{(X,Y)\sim P}
[\ell(f_{\mathcal D}(X),Y)].
$$

A held-out estimate is

$$
\widehat R
=
\frac1N\sum_{i=1}^N
\ell(f_{\mathcal D}(X_i),Y_i).
$$

If test cases are independent of development and have the intended marginal distribution, then, conditional on the fitted pipeline,

$$
\begin{aligned}
\mathbb E[\widehat R\mid\mathcal D]
&=
\frac1N\sum_i
\mathbb E[\ell(f_{\mathcal D}(X_i),Y_i)\mid\mathcal D]\\
&=
R_P(f_{\mathcal D}).
\end{aligned}
$$

Independence among test cases is not required for this equality of expectations. It is required for the usual simple variance formula and many standard uncertainty calculations.

This distinction prevents a common overstatement: correlated test observations do not automatically make the average optimistic. They can make the reported certainty unjustified.

### 2. Medical data contain several nested units

A dataset may contain

$$
\text{institutions}
\supset
\text{patients}
\supset
\text{examinations}
\supset
\text{series or clips}
\supset
\text{frames}.
$$

Different claims require different boundaries.

| Intended claim | Separation needed for that claim |
|---|---|
| New frames from an already observed examination | A frame-level task with that limited interpretation |
| New examinations from unseen patients | Patient separation across development and evaluation |
| Future observations of known patients | A longitudinal design using only legitimately available history |
| New patients at a new institution | Patient separation and a held-out institutional setting |
| Future clinical use | A time-respecting design, including information and label availability |

A random image split cannot support a new-patient claim merely because filenames differ.

Conversely, using earlier observations from a known patient is not intrinsically wrong. It is appropriate if the intended task is forecasting for known patients and the evaluation reproduces the allowed history.

### 3. Construct an example showing mean inflation from patient overlap

Suppose each patient has a unique identifier $$U_i$$ and a binary outcome

$$
Y_i\sim\operatorname{Bernoulli}(1/2).
$$

Assume the identifier is independent of the outcome and every image carries enough information to recognize the patient. There is no disease-related information in the images.

A model can memorize the outcome of every patient represented in training.

For another image of a known patient, its error is zero. For a new patient, the identifier contains no information about outcome, so the best possible error remains

$$
\frac12.
$$

Now give each patient $$m$$ images. Assign each image independently to training with probability $$q$$.

Conditional on one image being held out, the probability that none of that patient's other images enters training is

$$
(1-q)^{m-1}.
$$

The memorizer makes errors only when the patient is entirely absent from training. Its expected held-out image error is therefore

$$
\boxed{
R_{\mathrm{image\ split}}
=
\frac12(1-q)^{m-1}.
}
$$

For the constructed choice $$q=1/2$$ and $$m=3$$,

$$
R_{\mathrm{image\ split}}
=
\frac12\left(\frac12\right)^2
=
\frac18.
$$

The reported held-out image accuracy is $$7/8$$, although accuracy for a genuinely new patient is only $$1/2$$.

The model has not learned the clinical relationship. The split has made patient recognition useful.

Real repeated images need not contain literal identifiers. Anatomy, lesion appearance, annotations, acquisition patterns, and near-duplicate frames can provide patient- or examination-specific information.

### 4. Derive the effect of correlation within an independent test set

Now consider a different situation: all test patients are absent from development, but each contributes several correlated observations.

Let there be $$n$$ independent patients with $$m$$ observations each. For a fixed fitted pipeline, let loss $$Z_{ij}$$ for patient $$i$$ and observation $$j$$ satisfy

$$
\mathbb E[Z_{ij}]=\mu,
\qquad
\operatorname{Var}(Z_{ij})=\sigma^2.
$$

Assume equal within-patient correlation $$\rho$$:

$$
\operatorname{Cov}(Z_{ij},Z_{ik})
=
\rho\sigma^2,
\qquad j\neq k,
$$

and zero covariance across patients.

The mean loss is

$$
\overline Z
=
\frac1{nm}
\sum_{i=1}^n\sum_{j=1}^m Z_{ij}.
$$

Its expectation remains

$$
\mathbb E[\overline Z]=\mu.
$$

For one patient, the variance of the sum includes $$m$$ individual variances and $$m(m-1)$$ ordered covariance terms:

$$
\operatorname{Var}\left(\sum_{j=1}^m Z_{ij}\right)
=
m\sigma^2+m(m-1)\rho\sigma^2.
$$

Summing over independent patients and dividing by the squared denominator gives

$$
\begin{aligned}
\operatorname{Var}(\overline Z)
&=
\frac{
n[m\sigma^2+m(m-1)\rho\sigma^2]
}{
n^2m^2
}\\
&=
\boxed{
\frac{\sigma^2}{nm}[1+(m-1)\rho].
}
\end{aligned}
$$

The factor

$$
D=1+(m-1)\rho
$$

is the variance inflation relative to treating all $$nm$$ observations as independent.

A variance-equivalent effective sample size is

$$
N_{\mathrm{eff}}
=
\frac{nm}{1+(m-1)\rho}.
$$

This is not a count of actual independent patients. It describes the variance of this particular mean under the stated equal-cluster model.

At $$\rho=0$$ it equals $$nm$$. At $$\rho=1$$ it equals $$n$$: repeated observations carry no additional information about the mean beyond one observation per patient.

### 5. A constructed correlation example

Construct patient-specific error probabilities

$$
Q_i=
\begin{cases}
1/4,&\text{with probability }1/2,\\
3/4,&\text{with probability }1/2.
\end{cases}
$$

Conditional on $$Q_i$$, let a patient's image errors be independent Bernoulli draws with probability $$Q_i$$.

The marginal error probability is

$$
\mathbb E[Q_i]
=
\frac12\cdot\frac14+\frac12\cdot\frac34
=
\frac12.
$$

Thus each binary loss has variance

$$
\sigma^2=\frac12\left(1-\frac12\right)=\frac14.
$$

Two errors from the same patient are conditionally independent, but share $$Q_i$$. Their covariance is

$$
\begin{aligned}
\operatorname{Cov}(Z_{ij},Z_{ik})
&=\operatorname{Var}(Q_i)\\
&=
\frac12\left(\frac14-\frac12\right)^2
+
\frac12\left(\frac34-\frac12\right)^2\\
&=\frac1{16}.
\end{aligned}
$$

Therefore,

$$
\rho=\frac{1/16}{1/4}=\frac14.
$$

Take 20 patients with five observations each. Then

$$
D=1+(5-1)\frac14=2,
$$

and

$$
N_{\mathrm{eff}}=\frac{100}{2}=50.
$$

The independence-based variance would be

$$
\frac{1/4}{100}=\frac1{400},
$$

whereas the actual variance under this construction is

$$
\frac1{400}\cdot2=\frac1{200}.
$$

The standard error is larger by $$\sqrt2$$.

The average error still estimates $$1/2$$ without bias. The failure is overstated precision, not necessarily an inflated mean.

### 6. Unequal image counts can change the estimand

Let patient $$i$$ contribute $$m_i$$ observations with average loss $$\overline L_i$$.

An image-weighted estimate is

$$
\widehat R_{\mathrm{image}}
=
\frac{\sum_i m_i\overline L_i}{\sum_i m_i}.
$$

A patient-weighted estimate is

$$
\widehat R_{\mathrm{patient}}
=
\frac1n\sum_i\overline L_i.
$$

For independently sampled patients and suitable finite moments, the large-sample image-weighted target is

$$
\frac{\mathbb E[m\overline L]}{\mathbb E[m]}.
$$

Using the covariance identity,

$$
\mathbb E[m\overline L]
=
\mathbb E[m]\mathbb E[\overline L]
+
\operatorname{Cov}(m,\overline L),
$$

so

$$
\boxed{
R_{\mathrm{image}}
=
\mathbb E[\overline L]
+
\frac{\operatorname{Cov}(m,\overline L)}{\mathbb E[m]}.
}
$$

If harder patients generate more images, image weighting emphasizes harder patients. If easier patients generate more, the direction reverses.

This is not automatically leakage. It is a mismatch between the averaging rule and the intended population-level question.

### 7. Enumerate leakage mechanisms by how information enters

| Mechanism | Information crossing the boundary | Why the estimate can become optimistic |
|---|---|---|
| Images from one patient in multiple partitions | Patient identity and repeated anatomy | Test cases can be recognized through development relatives |
| Augmented or near-duplicate images across partitions | The original observation | Evaluation measures familiarity with transformations of known data |
| Full-data supervised feature selection | Held-out outcomes | Features are chosen partly for chance agreement with test labels |
| Full-data fitted preprocessing | Held-out input distribution | The pipeline adapts to evaluation conditions unavailable under the claimed deployment protocol |
| Test-driven model or threshold selection | Held-out performance and errors | The reported winner benefits from selection on noise |
| Post-decision input features | Future clinical information | The model receives evidence unavailable at its intended decision time |
| Acquisition or annotation after recognition | Human knowledge of the finding | The input may reveal that someone already located or diagnosed the target |
| Reference incorporating model output | The prediction itself | Agreement is partly built into the reference rather than independently assessed |

The mechanisms differ. Their remedies must address the information path that actually exists.

### 8. Keep learned preprocessing inside development

A fitted pipeline may include

$$
\text{imputation}
\rightarrow
\text{normalization}
\rightarrow
\text{feature selection}
\rightarrow
\text{model}
\rightarrow
\text{calibration}
\rightarrow
\text{decision rule}.
$$

Every learned component is part of the predictor.

For example, if a normalization mean is estimated from all observations,

$$
\widehat\mu_{\mathrm{all}}
=
\frac1N\sum_{i=1}^N X_i,
$$

then transformed training inputs depend on held-out inputs. The evaluated procedure has access to information from the evaluation population.

This does not mathematically guarantee an improved score. Unsupervised full-data preprocessing can increase, decrease, or leave performance unchanged. The defensible criticism is that it violates the claimed inductive evaluation protocol and can produce optimism by adapting to the future population.

If deployment explicitly permits adaptation using an unlabeled target batch, that is a different, transductive procedure. It can be evaluated, but its allowed information must be declared and reproduced.

A fixed transformation applied separately to each image is different. Resizing according to a prespecified rule does not estimate a population parameter from the holdout.

Supervised preprocessing is more direct: selecting features using all labels allows test outcomes to influence which predictive relationships are retained.

### 9. Derive optimism from choosing the best held-out result

Suppose candidate procedure $$k$$ has true risk $$R_k$$ and estimated risk

$$
\widehat R_k=R_k+\varepsilon_k,
\qquad
\mathbb E[\varepsilon_k]=0.
$$

Even if each estimate is unbiased before selection, choosing the smallest estimate changes its interpretation.

In the simple case where every candidate has the same true risk $$R$$,

$$
\min_k\widehat R_k
=
R+\min_k\varepsilon_k.
$$

Since the minimum is no greater than any individual noise term,

$$
\mathbb E[\min_k\varepsilon_k]\leq0.
$$

Thus,

$$
\boxed{
\mathbb E[\min_k\widehat R_k]\leq R.
}
$$

The winning estimate benefits from favorable noise.

A concrete construction makes the problem exact. Let outcomes be independent fair Bernoulli draws. Compare two constant classifiers: always predict zero and always predict one. Both have true error $$1/2$$.

If the validation set's positive fraction is $$\overline Y$$, their errors are

$$
\widehat R_0=\overline Y,
\qquad
\widehat R_1=1-\overline Y.
$$

The selected error is

$$
\min(\overline Y,1-\overline Y)
=
\frac12-\left|\overline Y-\frac12\right|.
$$

With one validation case, the selected classifier has validation error zero, regardless of the outcome. Its error on a new independent case remains $$1/2$$.

Repeated inspection can create the same adaptation without an explicit automated search. Choosing architectures, prompts, preprocessing, or audit rules in response to test failures makes the test set part of development.

### 10. Separate model selection from performance estimation

In nested cross-validation:

1. An outer training partition contains the development process.
2. Inner partitions select preprocessing, model settings, and other learned choices.
3. The chosen procedure is fitted using the outer training data.
4. The outer held-out partition evaluates the result.
5. This is repeated according to the declared outer design.

Patient grouping and temporal restrictions apply inside both levels where required.

The outer estimate concerns the development procedure under that sampling scheme. It is not an independent certificate for the final model later refitted on all data.

The selected threshold and recalibration mapping are part of the procedure. Fitting them on an outer test fold would reopen the boundary.

Fold results are also not generally independent: training sets overlap. Treating variation across folds as if it arose from independent experiments can misrepresent uncertainty.

For a final frozen model, resampling independent test patients estimates evaluation uncertainty conditional on that model. To study variation from model development itself, the development procedure must also vary. These are different uncertainty questions.

### 11. Temporal leakage is about availability, not merely timestamps

Specify a prediction time $$t_0$$. A valid input must be available by that time under the intended workflow.

Potential violations include:

- A pathology result produced after the imaging decision.
- A diagnosis code entered after the episode was resolved.
- Follow-up images obtained because the original finding was suspicious.
- A report section written using later information.
- A treatment variable that reveals the clinician's eventual diagnosis.

An outcome observed after $$t_0$$ can legitimately serve as the reference for a prediction made at $$t_0$$. The error is allowing that future information to enter the predictors.

Training availability has its own timeline. A historical case may have occurred before a deployment cutoff while its outcome label became available only afterward. A faithful simulation of prospective development must respect when the training information was actually known.

Temporal splitting alone does not repair post-decision features. A model can receive future information for every patient in both time periods.

### 12. Acquisition cues require a task-specific interpretation

Suppose a detection model receives only frames saved after a clinician found and centered a lesion. The frame selection already contains human localization information.

Such data may support classification of a recognized lesion. They do not by themselves evaluate initial detection in an unselected examination.

Similarly, measurement calipers, region crops, text overlays, or protocol choices may reveal what the operator suspected.

Not every acquisition association is leakage. A cue genuinely available before the intended decision may be a valid input under the declared task. It can nevertheless be a shortcut that fails when another hospital uses different acquisition practices.

The useful distinction is:

- **Unavailable at the claimed decision time:** an information-availability violation.
- **Available but associated through local practice:** a potential transport or evidence-reliance problem.
- **Explicitly supplied for a narrower task:** legitimate information whose role must be stated.

Patient separation addresses identity overlap. It does not resolve these task-definition problems.

### 13. What each validation design can claim

| Design | Main question | What it does not establish |
|---|---|---|
| Random patient holdout | Performance on new patients from the sampled source | Transfer to every institution or future workflow |
| Temporal holdout | Performance in the later period that actually occurred | Robustness to all possible future changes |
| Geographic holdout | Transfer to the particular held-out sites | Universal cross-site validity |
| Prospective silent evaluation | Performance on incoming cases without changing care | The consequences of clinicians acting on outputs |
| Comparative use evaluation | Effects of introducing a defined workflow | Automatic transport of those effects to other settings |

These designs can be combined. Their names do not replace documentation of patient overlap, acquisition changes, reference standards, and adaptation.

A low external score does not prove that internal validation leaked. It can arise from a real population change, different reference process, missing support, or altered measurement.

Likewise, a high external score does not prove leakage absent. Related patients, copied datasets, shared preprocessing, or repeated adaptation may cross institutional labels.

### 14. A practical audit follows data and decisions

Before fitting models:

- Establish patient, examination, and source identifiers.
- Define the prediction moment and target.
- Split original units before generating augmentations or derived frames.
- Record label provenance and availability.
- Identify the intended weighting of patients and observations.

During development:

- Fit learned transformations inside the permitted training data.
- Keep calibration and threshold selection inside development.
- Record how checkpoints and model variants are selected.
- Treat repeated evaluation-driven changes as adaptation.

Before final evaluation:

- Check identity overlap, duplicates, and near-duplicates.
- Inspect acquisition and annotation cues against the task timeline.
- Trace every fitted parameter to its data source.
- Freeze the complete pipeline and aggregation rule.
- Choose uncertainty calculations that respect clustering.

File hashes detect exact duplicates, not every crop, compression, or near-identical acquisition. A clean hash comparison is one check, not proof of independence.

### 15. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What does the held-out mean estimate? | Risk under a specified target distribution and information-access scheme |
| Does test correlation necessarily bias the mean? | No; it can leave the mean unbiased while inflating variance |
| Why does patient overlap change performance? | Recognition of a development patient can replace learning a transferable relationship |
| What is the cluster variance factor? | $$1+(m-1)\rho$$ under the equal-cluster model |
| Why can image and patient averages differ? | Image weighting depends on the relation between image count and difficulty |
| Is full-data preprocessing always optimistically biased? | No; it changes the protocol and can create optimism, but direction is not universal |
| Why does model selection produce optimism? | Selecting the minimum estimate also selects favorable noise |
| What belongs inside cross-validation? | Every learned or selected pipeline component |
| Is a future outcome an invalid label? | No; future information is invalid as an input when unavailable at prediction time |
| What does a new-site test establish? | Performance under the particular transfer tested, subject to its independence and sampling design |

In the ontology, leakage threatens the validity of evaluation evidence. Validation design determines which generalization claim a metric can support. An independent split and a clinically appropriate target are complementary requirements.

## Why it matters for my work

Gallbladder cine frames and selected lesion images make the unit and timing problems especially concrete. Independence must also extend to clinical faithfulness audits: cases used to invent intervention rules cannot simultaneously provide an untouched estimate of how well those rules detect failures in new data.

## What I have not resolved

- Which identifiers and acquisition records are sufficient to reconstruct patient and examination relationships?
- How should an audit reserve independent cases after its interventions have been developed?
- Which temporal and institutional changes can the available data actually represent?

---

Sources: Independent study; the memorization example, cluster-variance derivation, weighting identity, and selection-bias construction are developed above. All numerical examples are stipulated probability models rather than measured study results. These are study notes for research purposes, not clinical guidance.
