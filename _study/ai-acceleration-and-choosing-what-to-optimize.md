---
layout: study_note
title: "AI Acceleration: Reducing Work and Choosing What to Optimize"
description: "Transform convolution separates arithmetic savings from hardware utilization and makes the cost of optimization an explicit engineering decision."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "efficient-computation"
category_title: "Efficient Computation & Acceleration"
subgroup: "Algorithmic Speedups"
order: 1
source: "Lecture, mobile computing / AI acceleration"
written: true
updated: "2026-09-17"
---

The [FFT note](/study/the-fast-fourier-transform/) derives the fast transform, and [convolution via the DFT](/study/convolution-via-the-dft/) establishes the convolution theorem, padding, and block processing. Those results are the starting point here.

The next question is which implementation makes a particular workload cheaper. An algorithm can remove arithmetic while making memory access worse. A specialized processor can execute a kernel quickly while requiring more development time than the application can justify. I need to distinguish the mathematical operation, its execution cost, and the value of completing it sooner.

## What an optimization is allowed to change

Optimization reaches from the algorithm through numerical precision, data layout, scheduling, libraries, and hardware. The highest-level opportunity is to discover that some of the work was unnecessary.

An algebraically equivalent algorithm is especially attractive: the intended operator stays fixed. FFT and Winograd convolution belong to this category in exact arithmetic. Quantization or changing the model architecture introduces a different kind of comparison because approximation or model behavior also changes.

Equivalence does not remove every tradeoff. A transform can require additional storage and amplify rounding error. Reassociation also changes floating-point results. I should state the operator and numerical tolerance before declaring two implementations interchangeable.

## Reusing the FFT: count the convolution work

### One-dimensional convolution

Let $$x$$ contain $$N$$ samples and $$h$$ contain $$K$$ coefficients, with $$1\le K\le N$$. Use zero extension and compute the full linear convolution $$y=x*h$$.

Starting with a zeroed output, a direct implementation contributes every input/filter pair:

$$
y[n+k]\mathrel{+}=x[n]h[k].
$$

There are $$N$$ choices of $$n$$ and $$K$$ choices of $$k$$, hence $$NK$$ products and $$O(NK)$$ arithmetic.

The existing convolution note gives the alternative:

$$
y
=
\operatorname{IFFT}_L
\left[
\operatorname{FFT}_L(x_{\mathrm{pad}})
\odot
\operatorname{FFT}_L(h_{\mathrm{pad}})
\right],
\qquad
L\ge N+K-1,
$$

retaining the required linear-convolution output. The work comprises two forward transforms, $$L$$ pointwise products, and one inverse transform:

$$
W_{\mathrm{FFT}}=O(L\log L)+O(L)=O(L\log L).
$$

Choosing the next power of two above the required length gives $$L=\Theta(N)$$ under the stated bound on $$K$$. The comparison is therefore

$$
O(NK)
\quad\text{versus}\quad
O(N\log N).
$$

The direct method becomes quadratic when $$K=\Theta(N)$$. With a fixed short filter it is already linear in $$N$$, so the FFT has no automatic asymptotic advantage. A fixed filter's transform can be reused, reducing overhead without changing this whole-array comparison.

### Two-dimensional convolution

Now let $$N$$ denote the side length of a square image and use a $$K\times K$$ filter. Direct full convolution forms

$$
N^2K^2
$$

input/filter products.

Pad each dimension to $$L\ge N+K-1$$. A two-dimensional FFT applies length-$$L$$ transforms along $$L$$ rows and $$L$$ columns, so each transform costs

$$
L\,O(L\log L)+L\,O(L\log L)
=
O(L^2\log L).
$$

The pointwise stage costs $$O(L^2)$$. With $$K\le N$$ and suitable padding:

$$
W_{\mathrm{direct}}=O(N^2K^2),
\qquad
W_{\mathrm{FFT}}=O(N^2\log N).
$$

The explicit $$K^2$$ multiplier disappears. Filter size still affects padding, useful output per tile, and transform reuse. The multiplication stage also uses complex values unless further structure is exploited, so an FFT product cannot simply be counted as one real hardware operation.

A schematic cost comparison is

$$
aN^2K^2
\quad\text{against}\quad
bL^2\log_2L+cL^2,
$$

where the constants account for the arithmetic convention and implementation. At $$K=3$$, the direct method has only nine filter products per interior output. The transform must recover its overhead from those nine products.

These are whole-array costs. The overlap-add and overlap-save methods already derived in the convolution note permit fixed-size block processing. For fixed filters and tiles, their work can also grow linearly with the total number of image pixels. The expressions above explain a pressure toward larger filters, not a universal crossover threshold.

### What the historical example actually establishes

[Cooley and Tukey's 1965 paper](https://research.ibm.com/publications/an-algorithm-for-the-machine-calculation-of-complex-fourier-series) made an efficient DFT algorithm widely accessible for machine computation. Calling it the first efficient method would erase earlier work.

Heideman, Johnson, and Burrus identify an equivalent decomposition in Gauss's work on trigonometric interpolation of astronomical observations, dated by historical inference to around 1805 and published posthumously in 1866. Gauss recognized the computational saving and recursive factorization, but did not give the modern $$O(N\log N)$$ operation analysis. This was mathematical computation before electronic computers, not an early digital implementation. [Gauss and the history of the fast Fourier transform](https://faculty.washington.edu/seattle/physics541/%202010-Fourier-transforms/history-3.pdf)

## Why GPU acceleration needs a software stack

Raster graphics exposes large amounts of parallel work: many vertices or fragments undergo similar calculations. Independent shader invocations are an embarrassingly parallel part of that workload. The whole rendering pipeline is more complicated, including visibility, blending, shared memory traffic, and ordering constraints.

That workload helps explain a GPU's emphasis on throughput across many execution units. Streaming multiprocessors organize the execution of many threads; having many arithmetic units is useful only when work and data reach them. CUDA made this machinery accessible without expressing the computation through a graphics API. [NVIDIA CUDA introduction](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html)

Libraries supply another necessary layer:

| Library | Operation supplied |
| --- | --- |
| cuBLAS | Basic linear algebra, including matrix multiplication |
| cuFFT | Fast Fourier transforms |
| cuDNN | Primitives used by deep neural networks |

These are parts of NVIDIA's [GPU library stack](https://developer.nvidia.com/cuda/cuda-x-libraries). They package algorithm selection, device-specific implementation, and interfaces that applications can actually use.

GPGPU, general-purpose computing on a graphics processing unit, is a slightly comic name for this history: the original application remains in the name after the programming model expands beyond it. The important transition is from available arithmetic capacity to usable computation. A chip without the required software path does not accelerate my application.

## Why fbfft did not settle small-filter convolution

Vasilache and colleagues developed both a cuFFT-based convolution implementation and the specialized fbfft library in [Fast Convolutional Nets With fbfft: A GPU Performance Evaluation](https://arxiv.org/abs/1412.7580), first posted in 2014 and published at ICLR in 2015.

The cost expressions predict the difficulty. Enlarging a spatial filter increases direct work through $$K^2$$. Once the transform size is fixed, it does not similarly enlarge the pointwise multiplication. Small filters leave less direct work to eliminate, while padding, transforms, launches, and memory movement remain.

Architectures such as [VGG](https://arxiv.org/abs/1409.1556) emphasized stacked $$3\times3$$ filters. This makes small-filter performance a central problem, but does not establish that every CNN uses that size or that large filters are intrinsically bad.

The fbfft paper's figures comparing cuFFT convolution with cuDNN show the advantage generally improving with filter size. They also report advantageous $$3\times3$$ cases at sufficiently large problem sizes. The blanket claim that FFT helps *only* large filters is too strong. The defensible conclusion is that the regime offering the clearest arithmetic advantage does not automatically match the small filters prominent in these CNNs. Batch size, channel counts, transform reuse, and implementation all affect the result. [Vasilache et al., Section 4](https://arxiv.org/pdf/1412.7580)

## Winograd: make the transform fit a small filter

A useful interpretation is that Winograd pursues the same strategy as FFT convolution with a transform suited to small filters. The uncontested common structure is:

1. Transform the input.
2. Transform the filter.
3. Multiply corresponding transformed components.
4. Transform the products into the required outputs.

How far to call them the same idea is an interpretation. Winograd minimal filtering uses a different algebraic construction, related to polynomial arithmetic and the Chinese remainder theorem. Its output transform is not simply an inverse DFT.

[Lavin and Gray's Fast Algorithms for Convolutional Neural Networks (2016)](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Lavin_Fast_Algorithms_for_CVPR_2016_paper.pdf) applies this construction to CNNs. I will verify the small example directly rather than infer correctness from the shared diagram.

### Fix the operation: two outputs from three filter coefficients

CNN convolution commonly means cross-correlation. Here $$F(2,3)$$ means the following valid, stride-one operation:

$$
Y=
\begin{bmatrix}
d_0g_0+d_1g_1+d_2g_2\\
d_1g_0+d_2g_1+d_3g_2
\end{bmatrix}.
$$

It needs four input values, three filter coefficients, and ordinarily six products. To use the convolution convention from the earlier note, reverse the filter and align the output indices accordingly.

The transform representation is

$$
Y=A^\top\left[(Gg)\odot(B^\top d)\right].
$$

The matrices, written in the orientation used in this expression, are

$$
B^\top=
\begin{bmatrix}
1&0&-1&0\\
0&1&1&0\\
0&-1&1&0\\
0&1&0&-1
\end{bmatrix},
\qquad
G=
\begin{bmatrix}
1&0&0\\
\frac12&\frac12&\frac12\\
\frac12&-\frac12&\frac12\\
0&0&1
\end{bmatrix},
$$

$$
A^\top=
\begin{bmatrix}
1&1&1&0\\
0&1&-1&-1
\end{bmatrix}.
$$

Thus $$B$$ is $$4\times4$$, $$G$$ is $$4\times3$$, and $$A$$ is $$4\times2$$. These are the $$F(2,3)$$ matrices in Lavin and Gray, Section 4.1.

Writing out the component products exposes the saving:

$$
\begin{aligned}
p_0&=g_0(d_0-d_2),\\
p_1&=\frac{g_0+g_1+g_2}{2}(d_1+d_2),\\
p_2&=\frac{g_0-g_1+g_2}{2}(d_2-d_1),\\
p_3&=g_2(d_1-d_3).
\end{aligned}
$$

The output transform gives

$$
Y_0=p_0+p_1+p_2,
\qquad
Y_1=p_1-p_2-p_3.
$$

To check the cancellations, first combine the middle products:

$$
p_1+p_2=g_1d_1+(g_0+g_2)d_2,
$$

$$
p_1-p_2=(g_0+g_2)d_1+g_1d_2.
$$

Adding $$p_0$$ in the first expression and subtracting $$p_3$$ in the second recovers the two direct dot products.

For a constructed numerical check, choose

$$
d=(1,2,3,4)^\top,
\qquad
g=(2,-1,3)^\top.
$$

Then

$$
B^\top d=(-2,5,1,-2)^\top,
\qquad
Gg=(2,2,3,3)^\top,
$$

$$
p=(-4,10,3,-6)^\top,
\qquad
Y=(9,13)^\top.
$$

Direct evaluation gives $$2-2+9=9$$ and $$4-3+12=13$$.

The count has fallen from six to four **products between input-dependent and filter-dependent quantities**. The ratio is $$6/4=1.5$$. It has not removed the transforms: this implementation also needs four input additions, four output additions, and a filter transform that can share $$g_0+g_2$$, using three additions and two multiplications by one half.

### Nest the construction in two dimensions

For a $$4\times4$$ input tile $$d$$ and a $$3\times3$$ filter $$g$$, apply the same transforms along both axes:

$$
U=GgG^\top,
\qquad
V=B^\top dB,
$$

$$
Y=A^\top\left[U\odot V\right]A.
$$

Both transformed arrays are $$4\times4$$, and $$Y$$ is $$2\times2$$. The corresponding direct operation is

$$
Y_{ij}=\sum_{p=0}^{2}\sum_{q=0}^{2}g_{pq}d_{i+p,j+q},
\qquad i,j\in\{0,1\}.
$$

There are four output locations, each using nine products:

$$
M_{\mathrm{direct}}=2^2\cdot3^2=36.
$$

The transformed multiplication uses

$$
M_{\mathrm{Winograd}}=4^2=16.
$$

Thus the multiplication-count reduction is

$$
\frac{36}{16}=2.25,
\qquad
1-\frac{16}{36}=\frac59
$$

of those products eliminated. For fixed tile and filter sizes, this is a constant-factor reduction, not a change in asymptotic growth with image area.

For a constructed two-dimensional check, take

$$
d=
\begin{bmatrix}
1&2&0&1\\
0&1&3&2\\
2&0&1&1\\
1&2&1&0
\end{bmatrix},
\qquad
g=
\begin{bmatrix}
1&0&-1\\
2&1&0\\
0&-1&1
\end{bmatrix}.
$$

The transforms produce

$$
U=
\begin{bmatrix}
1&0&0&-1\\
\frac32&\frac34&\frac34&0\\
-\frac12&-\frac34&\frac14&0\\
0&0&1&1
\end{bmatrix},
\qquad
V=
\begin{bmatrix}
0&1&-3&2\\
-2&5&3&-2\\
4&-3&-1&0\\
-3&1&3&-3
\end{bmatrix}.
$$

Multiplying corresponding entries gives

$$
M=
\begin{bmatrix}
0&0&0&-2\\
-3&\frac{15}{4}&\frac94&0\\
-2&\frac94&-\frac14&0\\
0&0&3&-3
\end{bmatrix},
$$

and reconstructing gives

$$
Y=A^\top MA=
\begin{bmatrix}
3&6\\
0&-1
\end{bmatrix}.
$$

For example, the top-right direct dot product is

$$
(2+0-1)+(2+3+0)+(0-1+1)=6.
$$

All four outputs agree with direct evaluation. Zeros in this deliberately small example simplify some products; the counts of 36 and 16 describe the generic algorithms.

### What the multiplication count leaves out

The data transform applies a four-addition vector transform to four columns and four rows:

$$
4(4+4)=32
$$

additions. The output transform applies its four-addition vector operation to four columns and then two rows:

$$
4(4+2)=24
$$

additions.

For one isolated input/filter pair, even with the filter already transformed, this gives 16 products and 56 additions. Direct evaluation needs 36 products and 32 additions. Counting each addition and multiplication equally gives 72 versus 68 operations. The multiplication saving alone therefore does not establish a total-operation saving for this isolated tile.

CNN layers provide reuse. A transformed input tile serves multiple output channels; transformed filters serve many tiles. With input channels indexed by $$c$$, linearity allows

$$
Y_o
=
A^\top
\left[
\sum_c U_{o,c}\odot V_c
\right]
A.
$$

The output transform is applied after the channel sum. The useful comparison includes this amortization, transformed storage, channel reductions, and data movement.

Larger output tiles can reduce products per output further, but their transforms become more expensive and numerically less well conditioned. Exact algebra does not bound floating-point error. [Barabasz et al.](https://arxiv.org/abs/1803.10986) analyze this error growth and methods to reduce it. Tile size and precision belong in the accuracy test as well as the timing test.

## Reading throughput above the hardware peak

Lavin and Gray's published experiment used a Titan X. Section 7 lists 3,072 cores and a clock of 1,126 MHz, while reporting a single-precision peak of 6.96 TFLOPS. Table 5 reports 9.49 effective TFLOPS at batch size 16 for the VGG network's convolution layers with single-precision data. [Experimental setup and results](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Lavin_Fast_Algorithms_for_CVPR_2016_paper.pdf)

There is a small arithmetic discrepancy in the reported peak. Counting a fused multiply-add as two FLOPs, the stated core count and clock give

$$
P_{\mathrm{stated\ configuration}}
=
2\cdot3072\cdot1.126\times10^9
=
6.918144\times10^{12}\ \mathrm{FLOP/s},
$$

or about 6.92 TFLOPS. Running the reported peak backwards gives $$6.96\times10^{12}/(2\cdot3072)=1132.8$$ MHz, about 0.6 percent above the quoted clock. Either figure is a peak, and the gap between them is far smaller than the effect being discussed, so nothing below depends on which is used.

The throughput metric explains why the result can exceed either peak estimate. For a dense, ungrouped convolution with batch size $$b$$, output dimensions $$H_o,W_o$$, channel counts $$C_{\mathrm{in}},C_{\mathrm{out}}$$, and filter width $$K$$, a conventional direct-work count is

$$
F_{\mathrm{direct}}
=
2bH_oW_oC_{\mathrm{in}}C_{\mathrm{out}}K^2,
$$

counting each multiply-accumulate as two FLOPs. Effective throughput is

$$
R_{\mathrm{effective}}
=
\frac{F_{\mathrm{direct}}}{t_{\mathrm{measured}}}.
$$

Its numerator describes the reference algorithm, even when the implementation executes less arithmetic. If actual work is $$F_{\mathrm{executed}}$$, then

$$
R_{\mathrm{effective}}
=
\frac{F_{\mathrm{direct}}}{F_{\mathrm{executed}}}
\frac{F_{\mathrm{executed}}}{t_{\mathrm{measured}}}.
$$

An arithmetic reduction multiplies the apparent throughput relative to the reference workload. This does not mean the device executed floating-point instructions above its peak.

The two axes remain separate. In a simplified compute model with common peak $$P$$ and achieved arithmetic efficiency $$u$$,

$$
t=\frac{F}{uP},
\qquad
\frac{t_{\mathrm{old}}}{t_{\mathrm{new}}}
=
\frac{F_{\mathrm{old}}}{F_{\mathrm{new}}}
\frac{u_{\mathrm{new}}}{u_{\mathrm{old}}}.
$$

Reducing work by a factor of ten while reducing efficiency to one tenth leaves runtime unchanged in this model. Extra launch or transfer overhead can make it worse. A FLOP reduction and a utilization improvement are distinct achievements; measured end-to-end latency determines their combined value.

## Waiting for hardware is a competing implementation strategy

The four-color theorem illustrates the scale of historical computation, but its history needs care. Appel and Haken's own account reports completion in June 1976, 1,200 hours across three computers, and 1,482 configurations used in the final proof. Their method combined an unavoidable set with computer checks of reducibility. [The solution of the four-color-map problem](https://celebratio.org/Appel_KI/article/674/)

Robin Wilson records an earlier list of 1,936 configurations and its reduction to the published set. Counts from different versions should not be attached to one supposedly unchanged run. [Wilson's historical account](https://celebratio.org/Appel_KI/article/796/)

The authors describe extensive mathematical and program revisions. This is not evidence that the proof was obtained simply by waiting for faster hardware. Nor is aggregate computer time a calendar duration:

$$
1200/24=50
$$

days of continuous use of one machine, as an accounting equivalent.

A claim that the historical workload would take minutes now needs a specified program and machine. For example, turning 1,200 hours into ten minutes requires a workload speedup of

$$
\frac{1200\cdot60}{10}=7200.
$$

That is a required ratio, not a modern benchmark. Transistor growth alone does not establish it.

### Include development time in the comparison

Let a fixed job take $$T_0$$ on today's machine. A special-purpose implementation takes $$D$$ time to develop and then provides speedup $$s$$ relative to that machine. Ignoring other overhead:

$$
T_{\mathrm{build}}=D+\frac{T_0}{s}.
$$

If I instead wait $$w$$ for an available machine with workload speedup $$r(w)$$, then

$$
T_{\mathrm{wait}}=w+\frac{T_0}{r(w)}.
$$

Use a constructed scenario, not a historical hardware estimate:

$$
T_0=11\ \mathrm{years},
\qquad
D=1\ \mathrm{year},
\qquad
s=5.
$$

Building finishes in

$$
1+\frac{11}{5}=3.2\ \mathrm{years}.
$$

Waiting one year for a twofold improvement finishes in

$$
1+\frac{11}{2}=6.5\ \mathrm{years}.
$$

Here building wins on completion time. Waiting one year would need a speedup greater than five to finish sooner than 3.2 years. The numbers do not support an unconditional recommendation to wait.

The economic comparison also includes design, verification, compiler and library development, application porting, maintenance, and the value of earlier results. Repeated workloads can amortize those costs; an urgent deadline can rule out waiting. Conversely, buying improved general-purpose hardware can serve many applications without maintaining a separate implementation for each.

Even when waiting is slower, it can be rational if the earlier result is worth less than the engineering and maintenance cost. Neither a one-year development schedule nor a particular hardware improvement rate is a universal fact. Waiting is rational when its expected benefit exceeds its delay cost, not because future hardware is guaranteed to rescue every workload.

## The software argument behind a durable accelerator

In his [2021 Next Platform interview](https://www.nextplatform.com/ai/2021/11/16/nvidia-ceo-on-competition-software-and-the-omniverse/1643022), Jensen Huang argues that an accelerator competes with doing nothing and waiting for general-purpose machines to improve. A fast chip needs application-specific algorithms, libraries, and developers willing to adopt them. He presents CPUs and GPUs as the architectures that overcame this adoption barrier.

The logic is a moving comparison. If an accelerator has speedup $$s$$ over today's baseline, but that baseline improves by $$r$$ before deployment, its remaining advantage is

$$
\frac{s}{r}.
$$

A widening application-level lead makes development and porting easier to justify. A fixed lead can disappear while the software is being built.

This position also serves NVIDIA's interests: a large existing CUDA ecosystem makes software coverage a favorable criterion for competition. The historical claim that only CPUs and GPUs have succeeded is too broad. [Jouppi et al.'s TPU study](https://arxiv.org/abs/1704.04760) documents a specialized accelerator deployed in Google's data centers since 2015.

The requirement is a sufficient advantage after adoption and operating costs. It need not widen forever, and the relevant advantage may be energy, predictable latency, or cost rather than peak FLOPS alone.

## The inverse-square-root trick and its expiration date

Normalizing a nonzero vector requires multiplication by the reciprocal square root of its squared length. Quake III's published fast inverse square root forms an initial estimate from the bit pattern using the constant $$\mathtt{0x5f3759df}$$, followed by a Newton step:

$$
z_{\mathrm{new}}
=
z\left(\frac32-\frac{xz^2}{2}\right),
\qquad
x>0.
$$

This follows by applying Newton's method to $$f(z)=z^{-2}-x$$. The result is an approximation, unlike the exact-arithmetic identities used for transform convolution. [Quake III source: Q_rsqrt](https://github.com/id-Software/Quake-III-Arena/blob/master/code/game/q_math.c)

On x86 processors supporting SSE, RSQRTSS supplies an approximate reciprocal square root directly. Its documented accuracy and exceptional-input behavior still matter; it is not a correctly rounded replacement for every expression involving a square root. [Intel instruction reference](https://cdrdv2-public.intel.com/782151/253667-sdm-vol-2b.pdf)

That makes the handwritten bit trick a historical technique rather than a default optimization for such targets. There is no universal cycle count or speedup to quote without naming the processor and accuracy requirement. Useful primitives can move into instructions, compiler support, and libraries, changing which manual implementations are worth maintaining.

## Technical debt can erase the saved runtime

A shortcut creates technical debt when it makes later changes more expensive. A kernel tied to one layout, precision, or device can transfer a runtime saving into future integration work.

[Sculley et al., Hidden Technical Debt in Machine Learning Systems (2015)](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf) explains why ML adds maintenance risks beyond ordinary code: behavior depends on data, features become entangled, downstream consumers can be undeclared, and predictions can affect future training data through feedback loops.

This explains how ML debt can accumulate rapidly, not a universal numerical rate at which it grows faster than other software. A training script can remain unchanged while a data source changes its meaning. An undocumented preprocessing correction can become a dependency of both the trained model and its evaluation.

For an optimization, I therefore need a reproducible baseline, explicit numerical expectations, and enough configuration history to explain a changed result. A maintained library can spread implementation effort across users. A custom path needs a benefit large enough to support its own future changes.

## Choose the battle by the requirement

> 百戰百勝，非善之善者也。
>
> Winning every battle is not the highest excellence.

> 知彼知己，百戰不殆。
>
> Know the enemy and know yourself: in a hundred battles you will not be endangered.

Both passages belong to chapter 3, 謀攻, commonly translated as “Attack by Stratagem.” The first continues toward overcoming the opponent without fighting; the second promises freedom from danger, not victory in every encounter. [Chinese text](https://ctext.org/art-of-war/attack-by-stratagem), [Giles translation, chapter 3](https://www.gutenberg.org/files/132/132-h/132-h.htm)

My engineering reading is to understand both the workload and my constraints before committing to optimization. Dependencies, memory traffic, transform overhead, precision, and software coverage describe the problem. Deadlines, available effort, and the value of earlier results describe my position.

“Faster is better” leaves the decision undefined. “The result must be available before this workflow reaches its decision point” supplies a requirement. “This saving lets me complete a necessary set of experiments within my compute budget” supplies a value. Once that requirement is met, further speed needs its own justification.

## Revision checklist

| Check | What I should reconstruct without looking |
| --- | --- |
| Equivalence | Separate an unchanged mathematical operator from numerical and resource tradeoffs. |
| One-dimensional cost | Count $$NK$$ direct products and justify $$O(N\log N)$$ with the padding assumption. |
| Two-dimensional cost | Recover $$N^2K^2$$ versus $$O(N^2\log N)$$ and explain where filter size still matters. |
| Small filters | Explain why transform overhead is difficult to amortize and why FFT can still win in some cases. |
| Software stack | Connect GPU parallelism to CUDA, libraries, and an application's usable implementation. |
| Winograd identity | Reconstruct the matrices, the four products, and the cancellations for $$F(2,3)$$. |
| Two-dimensional tile | Recover $$A^\top[(GgG^\top)\odot(B^\top dB)]A$$ and the 36-to-16 product count. |
| Honest accounting | Count transform additions and explain reuse across tiles and channels. |
| Numerical behavior | Explain why larger tiles require an explicit accuracy check. |
| Throughput | Distinguish direct-reference FLOPs, executed work, and hardware utilization. |
| Waiting | Compare $$D+T_0/s$$ with $$w+T_0/r(w)$$ before adding lifecycle costs. |
| Adoption and debt | Explain how software coverage and maintenance can outweigh a kernel's speed advantage. |
| Requirement | Tie the latency target to a concrete decision or research outcome. |

## Why it matters for my work

As a master's student studying whether medical AI models rely on clinically valid evidence, I benefit from acceleration when it expands an audit I can actually complete. Faster inference could make it feasible to repeat region ablations, compare sensitivity to clinical findings and acquisition artifacts, or evaluate the same intervention across a held-out cohort.

An unchanged convolution operator does not make the model's evidence clinically valid. It only helps preserve the computation while testing that question. I would check that changing the numerical implementation preserves predictions and the conclusions of the intervention analysis within justified tolerances. An ablation that creates unrealistic images remains a questionable test even when it runs quickly.

If computation is already adequate, improving data provenance, intervention design, and evaluation may contribute more to my research than another kernel optimization. The relevant saving is additional reliable evidence obtained with limited time and resources.

## What I have not resolved

I do not know where my own audit pipeline actually spends its time, what latency it has to meet, or what numerical tolerance its conclusions can absorb. Answering that needs timings that cover preprocessing, host-device transfers, inference, and the repeated interventions, not a kernel benchmark. Choosing an algorithm before those measurements exist would be choosing in the dark.

Whether swapping the convolution implementation can move a small intervention effect enough to change an evidence-reliance conclusion is an empirical question I have not tested. The accuracy table above suggests the transform is not the fragile part at this tile size, but that is a statement about element error on one network, not about the stability of an effect estimate.

The claim that the historical four-color computation would now finish in minutes is one I left out of the argument. It needs a specified program on a specified machine, and the 7,200-fold ratio derived above is what such a claim would have to demonstrate, not evidence that it holds.
