---
layout: study_note
title: "Graph Neural Networks: Message Passing, Aggregation, and Inductive Node Embeddings"
description: "Learning a fixed-length descriptor for every node by repeatedly aggregating its neighbours, why a lookup table cannot embed a node it has never seen, and what makes the parameters independent of graph size."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 11
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-16"
---

The [graph Laplacian](/study/the-graph-laplacian/) and [spectral filtering](/study/spectral-filtering-and-graph-convolution/) notes develop the eigenbasis view. Here the starting operation is local: each node receives messages from its neighbours and updates its descriptor. No eigenvectors need to be constructed.

The central distinction is between **learning a vector for each known node** and **learning a shared function that computes a vector for any node with suitable inputs**. Both produce embeddings. Only the second construction supplies a computation for a previously unseen node.

## What a node descriptor must provide

Let an undirected, unweighted graph have node set $$V$$, edge set $$E$$, and adjacency matrix $$A$$. Initially there are no self-loops. Define

$$
n=|V|,
\qquad
\mathcal N(v)=\{u:(u,v)\in E\},
\qquad
d_v=|\mathcal N(v)|.
$$

A node has input features $$x_v\in\mathbb R^f$$. After $$K$$ layers, its descriptor is

$$
h_v^{(0)}=x_v,
\qquad
z_v=h_v^{(K)}\in\mathbb R^d.
$$

The width $$d$$ is fixed across nodes, even though their degrees differ. Features might describe content or measurements; structural features such as degree are also possible. "Learned from the graph" does not mean that useful features or a training objective appear automatically.

The downstream task determines what the descriptor should retain:

| Task | How the descriptor is used |
| --- | --- |
| Node classification | A shared classifier maps each descriptor to class scores. |
| Link prediction | A decoder scores a pair of descriptors for a possible edge. |
| Recommendation | Candidate item descriptors are ranked against a user or collection descriptor. |
| Similarity search | Descriptors are compared using the similarity used during training. |

For example, a linear classifier assigns scores $$a_v=Cz_v+b$$. Converting them to probabilities by exponentiating and dividing by their sum gives

$$
p_{v,c}=\frac{\exp(a_{v,c})}{\sum_j\exp(a_{v,j})}.
$$

This makes probabilities positive and sum to one. Maximising the product of correct-label probabilities is equivalent, after taking a negative logarithm, to minimising

$$
\mathcal L_{\mathrm{class}}
=
-\sum_{v\in V_{\mathrm{labelled}}}\log p_{v,y_v}.
$$

Backpropagation trains the descriptor generator through the classifier. Alternatively, graph edges or graph-walk co-occurrences can supply the training targets. Message passing defines an encoder, not a learning objective by itself.

## Why a grid operator needs to change

A one-dimensional grid convolution can write

$$
y_i=\sum_{r=-R}^{R}w_r x_{i+r}.
$$

The offset $$r$$ has a stable meaning. The left neighbour always occupies the left-neighbour slot. A general graph supplies adjacency without this coordinate system.

### Relabelling must only relabel the output

Numbering nodes is storage bookkeeping. Let $$P$$ be a permutation matrix. Relabelling the graph and its feature rows gives

$$
A'=PAP^{\mathsf T},
\qquad
X'=PX.
$$

A node encoder must satisfy

$$
F_\theta(PAP^{\mathsf T},PX)=P F_\theta(A,X).
$$

This is **permutation equivariance**: the output rows follow their nodes. Requiring the output matrix to remain unchanged would incorrectly make node-specific predictions invariant to moving the nodes.

Within one node's neighbourhood, reordering the same neighbours must leave the aggregated message unchanged. This is **permutation invariance**. Global equivariance and local invariance are compatible requirements at different levels.

### Degree cannot determine the layer's input width

Concatenating every neighbour of a node with degree $$d_v$$ produces a vector of width $$d_v f$$. A weight matrix expecting that width cannot also process a node with a different degree. Padding supplies a size limit but does not supply meaningful neighbour positions.

The operator therefore needs a reduction from a variable number of vectors to one vector of a prescribed width.

### New nodes cannot require new learned slots

A graph may acquire a node after training. The grid-convolution principle of shared computation can still transfer, but a model whose input weights or output vectors are tied to a fixed list of identities cannot simply accept another identity.

These are separate obstacles. Handling variable degree does not automatically ensure invariance, and invariance does not automatically provide unseen-node embeddings.

## Shallow embeddings and the missing-row problem

A shallow embedding model stores

$$
T\in\mathbb R^{n\times d},
\qquad
z_v=T^{\mathsf T}e_v,
$$

where $$e_v$$ is the one-hot indicator for node $$v$$. Multiplication selects its table row. There are exactly $$nd$$ learned scalars, hence parameter count $$O(|V|d)$$. Nodes have separate free vectors, although the loss couples those vectors through their interactions.

To train it in a word2vec-like way, treat nodes that co-occur along graph walks as positive context pairs and sample negative context pairs. For a score $$s_{vu}=z_v^{\mathsf T}z_u$$, define the logistic probability

$$
g(s)=\frac{1}{1+\exp(-s)}.
$$

For a binary pair target $$y$$, the probability of the observed target is $$g(s)^y[1-g(s)]^{1-y}$$. Since $$\log g(s)=s-\log(1+\exp s)$$ and $$\log[1-g(s)]=-\log(1+\exp s)$$, its negative logarithm is

$$
\ell(s,y)
=
-y\log g(s)-(1-y)\log[1-g(s)]
=
\log(1+\exp s)-ys.
$$

Thus positive pairs favour larger dot products, while negative pairs favour smaller ones. Separate node and context tables would double the table parameters without changing their order of growth.

Now introduce a node absent during training. Its indicator has no corresponding table row. Appending a random row makes lookup possible, but does not make the row learned. The original training loss never involved that row, so every possible value gives the same original loss.

**The missing ingredient is a rule that maps the new node's observations to its vector.** Optimising an appended row using new edges is additional fitting, not inference through the trained table. This is the precise transductive limitation, also discussed in the [embedding-table and cold-start note](/study/recommender-systems-and-sparse-features/).

A transductive experiment may include an unlabelled test node in the training graph. That node is already known structurally. It is different from a node whose features and connections arrive only after training.

## Constructing a message-passing layer

Let layer widths be $$p_0=f,p_1,\ldots,p_K=d$$. Use column vectors for individual node states. A shared linear neighbour-message rule is

$$
m_{u\to v}^{(k)}
=
W_{\mathrm{neigh}}^{(k)}h_u^{(k-1)},
\qquad
W_{\mathrm{neigh}}^{(k)}
\in\mathbb R^{p_k\times p_{k-1}}.
$$

For a mean reduction, transforming each message and then averaging is equivalent to averaging first:

$$
\frac{1}{d_v}\sum_{u\in\mathcal N(v)}
W_{\mathrm{neigh}}^{(k)}h_u^{(k-1)}
=
W_{\mathrm{neigh}}^{(k)}
\left(
\frac{1}{d_v}\sum_{u\in\mathcal N(v)}h_u^{(k-1)}
\right).
$$

This follows from linearity and also holds for summation. It does not generally hold for max pooling or a nonlinear message transform.

Give the node's own state a separate transformation, add the neighbourhood contribution, and apply a coordinatewise nonlinearity:

$$
h_v^{(k)}
=
\sigma\left(
W_{\mathrm{self}}^{(k)}h_v^{(k-1)}
+
W_{\mathrm{neigh}}^{(k)}
\operatorname{AGG}
\left(\{h_u^{(k-1)}:u\in\mathcal N(v)\}\right)
\right).
$$

Both matrices have shape $$p_k\times p_{k-1}$$ when the aggregator preserves width. The self term retains a direct route for the node's features. The nonlinearity permits responses that cannot be reduced to a single linear transformation of all input features. Biases are omitted here.

For max aggregation, the displayed equation defines a valid "aggregate, then transform" layer. A layer that transforms each neighbour before taking a maximum is another valid architecture, with different behaviour.

### What an invariant aggregator preserves

The braces represent a multiset: equal descriptors from different neighbours still count separately. For any permutation $$\pi$$,

$$
\operatorname{AGG}(x_1,\ldots,x_m)
=
\operatorname{AGG}(x_{\pi(1)},\ldots,x_{\pi(m)}).
$$

Sum and mean qualify because reordering does not change a sum or the number of entries. Coordinatewise max qualifies because reordering does not change the largest value in a coordinate.

For two neighbour descriptors:

$$
x_1=(1,4)^{\mathsf T},
\qquad
x_2=(3,2)^{\mathsf T},
$$

the sum, mean and max are respectively

$$
(4,6)^{\mathsf T},
\qquad
(2,3)^{\mathsf T},
\qquad
(3,4)^{\mathsf T}.
$$

An order-sensitive rule such as $$x_{1,1}+2x_{2,1}$$ gives $$7$$ in the displayed order and $$5$$ after swapping the neighbours.

Invariance also discards information. The scalar multisets $$\{1,3\}$$ and $$\{1,1,3,3\}$$ both have mean $$2$$ and max $$3$$, but sums $$4$$ and $$8$$. Sum retains evidence about multiplicity, although it still cannot distinguish every multiset: $$\{1,3\}$$ and $$\{2,2\}$$ have the same sum.

For an empty neighbourhood, define the neighbour contribution as zero. Empty mean and max are otherwise undefined. This convention leaves the self pathway available.

### Checking the whole layer's equivariance

Stack node vectors as rows of $$H$$ and write the mean operator as $$R=D^{-1}A$$, assuming positive degrees for this calculation. The layer becomes

$$
H^+
=
\sigma\left(
H W_{\mathrm{self}}^{\mathsf T}
+
R H W_{\mathrm{neigh}}^{\mathsf T}
\right).
$$

Under relabelling, $$D'=PDP^{\mathsf T}$$ and therefore $$R'=PRP^{\mathsf T}$$. Substituting gives

$$
H'^+
=
\sigma\left(
PHW_{\mathrm{self}}^{\mathsf T}
+
PRP^{\mathsf T}PHW_{\mathrm{neigh}}^{\mathsf T}
\right)
=
PH^+.
$$

The cancellation uses $$P^{\mathsf T}P=I$$. Coordinatewise activation commutes with a row permutation. Shared weights are essential: separate weights assigned to storage indices would invalidate this argument.

## A complete two-layer calculation

Construct a four-node path with edges $$\{a,b\},\{b,c\},\{c,d\}$$. Choose

$$
x_a=\begin{pmatrix}1\\0\end{pmatrix},
\quad
x_b=\begin{pmatrix}0\\2\end{pmatrix},
\quad
x_c=\begin{pmatrix}2\\1\end{pmatrix},
\quad
x_d=\begin{pmatrix}0\\0\end{pmatrix}.
$$

Use mean aggregation and, deliberately, the same numerical matrices in both layers:

$$
W_{\mathrm{self}}=I_2,
\qquad
W_{\mathrm{neigh}}=
\begin{pmatrix}1&1\\-1&1\end{pmatrix},
\qquad
\sigma(t)=\max(0,t).
$$

These numbers are constructed arithmetic, not fitted results. Every first-layer value is:

| Node | Neighbour mean | Self plus transformed mean | State after ReLU |
| --- | --- | --- | --- |
| $$a$$ | $$(0,2)$$ | $$(1,0)+(2,2)=(3,2)$$ | $$(3,2)$$ |
| $$b$$ | $$(3/2,1/2)$$ | $$(0,2)+(2,-1)=(2,1)$$ | $$(2,1)$$ |
| $$c$$ | $$(0,1)$$ | $$(2,1)+(1,1)=(3,2)$$ | $$(3,2)$$ |
| $$d$$ | $$(2,1)$$ | $$(0,0)+(3,-1)=(3,-1)$$ | $$(3,0)$$ |

For example, the step at $$b$$ is

$$
W_{\mathrm{neigh}}
\begin{pmatrix}3/2\\1/2\end{pmatrix}
=
\begin{pmatrix}3/2+1/2\\-3/2+1/2\end{pmatrix}
=
\begin{pmatrix}2\\-1\end{pmatrix}.
$$

At the second layer, $$a$$ receives the first-layer state of $$b$$:

$$
h_a^{(2)}
=
\operatorname{ReLU}
\left[
\begin{pmatrix}3\\2\end{pmatrix}
+
\begin{pmatrix}1&1\\-1&1\end{pmatrix}
\begin{pmatrix}2\\1\end{pmatrix}
\right]
=
\begin{pmatrix}6\\1\end{pmatrix}.
$$

Completing the second layer gives

$$
h_b^{(2)}=(7,0)^{\mathsf T},
\qquad
h_c^{(2)}=(6,0)^{\mathsf T},
\qquad
h_d^{(2)}=(8,0)^{\mathsf T}.
$$

For $$c$$, the neighbour mean is $$(5/2,1/2)^{\mathsf T}$$, its transformed message is $$(3,-2)^{\mathsf T}$$, and adding $$(3,2)^{\mathsf T}$$ gives $$(6,0)^{\mathsf T}$$.

The descriptor now contains a path for information from $$c$$ through $$b$$. Changing only $$x_d$$ cannot change this second-layer result at $$a$$.

All nodes must read the previous layer's states. Updating nodes in place and letting later nodes read already-updated values would make one "layer" depend on traversal order.

## Degree normalisation is a modelling choice

Suppose every neighbour supplies the same vector $$q$$. Then

$$
\sum_{u\in\mathcal N(v)}q=d_vq,
\qquad
\frac{1}{d_v}\sum_{u\in\mathcal N(v)}q=q.
$$

Summation makes magnitude depend on degree even when neighbour content is unchanged. Mean aggregation removes that dependence for identical messages. Sum models accumulated evidence; mean models neighbourhood composition. If the number of observations matters, discarding degree can remove useful information.

Symmetric normalisation uses both endpoint degrees:

$$
m_v^{\mathrm{sym}}
=
\sum_{u\in\mathcal N(v)}
\frac{h_u}{\sqrt{d_vd_u}},
\qquad
S=D^{-1/2}AD^{-1/2}.
$$

Why the square roots? Start from the mean operator $$R=D^{-1}A$$ and change coordinates from $$h$$ to $$g=D^{1/2}h$$. A mean-propagation step becomes

$$
g^+
=
D^{1/2}Rh
=
D^{1/2}RD^{-1/2}g
=
D^{-1/2}AD^{-1/2}g.
$$

Thus symmetric normalisation is mean propagation in degree-rescaled coordinates. On an undirected graph, its edge coefficient is the same in either direction. Applying it directly to raw descriptors chooses that rescaled geometry. It is not simply another formula for an ordinary mean.

A star makes the difference visible. Give its centre three leaves and assign scalar feature $$2$$ to every node:

| Operator | Centre receives | Each leaf receives |
| --- | --- | --- |
| Sum | $$2+2+2=6$$ | $$2$$ |
| Mean | $$6/3=2$$ | $$2/1=2$$ |
| Symmetric | $$6/\sqrt3=2\sqrt3$$ | $$2/\sqrt3$$ |

The symmetric weights do not generally sum to one. Mean divides by the receiver's degree; symmetric normalisation also discounts messages from high-degree senders. Neither choice guarantees that high-degree nodes cease to matter.

The formulas above assume nonzero degrees. A self-loop construction makes every normalising degree positive and gives isolated nodes a well-defined update.

## GCN and GraphSAGE organise the self term differently

### GCN: self as another message

Add one unit self-loop per node:

$$
\widetilde A=A+I,
\qquad
\widetilde d_v=d_v+1.
$$

Apply symmetric aggregation over this enlarged neighbourhood, followed by one shared transform:

$$
h_v^{(k)}
=
\sigma\left(
W^{(k)}
\sum_{u\in\mathcal N(v)\cup\{v\}}
\frac{h_u^{(k-1)}}{\sqrt{\widetilde d_v\widetilde d_u}}
\right).
$$

The self coefficient is $$1/\widetilde d_v$$ because both endpoint degrees are the same. Its feature transform is the same $$W^{(k)}$$ used for neighbours. Degrees must be computed after adding the loops; mixing the old and new degrees defines a different operator.

This is the usual GCN propagation rule viewed spatially. Its spectral connection belongs in the linked spectral note.

### GraphSAGE: self and neighbourhood occupy separate slots

For mean GraphSAGE, first form the neighbour mean $$m_v^{(k)}$$, then concatenate it with the self state:

$$
h_v^{(k)}
=
\sigma\left(
W^{(k)}
\begin{bmatrix}
h_v^{(k-1)}\\
m_v^{(k)}
\end{bmatrix}
\right).
$$

Partitioning the matrix exposes its meaning:

$$
W^{(k)}
=
\begin{bmatrix}
W_{\mathrm{self}}^{(k)}&
W_{\mathrm{neigh}}^{(k)}
\end{bmatrix}
\quad\Longrightarrow\quad
W^{(k)}
\begin{bmatrix}h\\m\end{bmatrix}
=
W_{\mathrm{self}}^{(k)}h+
W_{\mathrm{neigh}}^{(k)}m.
$$

This is the separate-transform layer already derived. Concatenating **self and aggregate** is legitimate because the two slots have fixed roles. Concatenating arbitrarily ordered individual neighbours does not have that justification.

Pooling GraphSAGE instead learns a feature detector before reducing over neighbours:

$$
m_v^{(k)}
=
\max_{u\in\mathcal N(v)}
\phi^{(k)}(h_u^{(k-1)}),
\qquad
\phi^{(k)}(h)=\operatorname{ReLU}(Bh+b),
$$

with coordinatewise max. Every neighbour receives the same detector, so reordering still preserves the result. A channel can record whether any neighbour strongly activates a learned pattern.

An LSTM aggregator processes a sequence, so swapping neighbours can change its recurrent state and output. Random neighbour permutations are used to discourage dependence on an arbitrary ordering. **Randomisation does not make each forward pass permutation-invariant.**

A genuinely invariant symmetrisation would average over every ordering:

$$
f_{\mathrm{sym}}(x_1,\ldots,x_m)
=
\frac{1}{m!}\sum_{\pi\in S_m}
f_{\mathrm{LSTM}}(x_{\pi(1)},\ldots,x_{\pi(m)}).
$$

Permuting the inputs only reindexes this sum. Sampling random orderings approximates that averaging if outputs are averaged; training with shuffles alone does not implement it. The factorial cost also explains why exact enumeration is unattractive.

GCN versus GraphSAGE is therefore not an absolute transductive-versus-inductive divide. Both can use shared computations on new nodes. The self pathway, aggregator, sampling procedure and available input features are the relevant distinctions.

## Receptive fields and the cost of depth

For a fixed graph, let $$\mathcal R_k(v)$$ contain nodes whose initial descriptors can reach $$v$$ in the computation. Initially,

$$
\mathcal R_0(v)=\{v\}.
$$

The self and neighbour pathways give the recursion

$$
\mathcal R_k(v)
=
\mathcal R_{k-1}(v)
\cup
\bigcup_{u\in\mathcal N(v)}\mathcal R_{k-1}(u).
$$

Inductively, these are the nodes within at most $$k$$ hops: the previous self state covers shorter paths, and a neighbour followed by a path of length at most $$k-1$$ covers paths of length at most $$k$$. This is the same composition principle as stacked local convolutions.

It is a potential receptive field. Zero weights, inactive nonlinearities or an aggregator's information loss can prevent an individual input from affecting the output. Structural information already encoded in initial features is also present before message passing begins.

If maximum degree is $$\Delta$$, a root can have at most $$\Delta$$ new neighbours, then at most $$\Delta(\Delta-1)$$ new nodes, and so on. Ignoring collisions gives

$$
|\mathcal R_k(v)|
\le
1+\Delta\sum_{j=0}^{k-1}(\Delta-1)^j.
$$

The count is also bounded by the total number of nodes. For a locally tree-shaped neighbourhood with degree four, three hops can contain

$$
1+4+12+36=53
$$

nodes. Overlapping neighbourhoods reduce this count.

More depth can also erase differences. Consider two scalar node states with the deliberately chosen update

$$
a_{k+1}=\frac34a_k+\frac14b_k,
\qquad
b_{k+1}=\frac14a_k+\frac34b_k.
$$

Adding and subtracting gives

$$
a_{k+1}+b_{k+1}=a_k+b_k,
\qquad
a_{k+1}-b_{k+1}=\frac12(a_k-b_k).
$$

Starting at $$a_0=0,b_0=2$$ therefore yields

$$
a_k=1-2^{-k},
\qquad
b_k=1+2^{-k}.
$$

The states become $$(1/2,3/2)$$, then $$(3/4,5/4)$$, and approach the same value. This is an explicit oversmoothing mechanism: repeated mixing preserves shared content while contracting differences.

This calculation proves a property of this averaging operator, not every nonlinear GNN. On irregular graphs, symmetric normalisation need not converge to literally equal raw descriptors. Small depths such as two or three layers are a practical starting point because they limit neighbourhood expansion and repeated mixing, not a universal optimal depth or a guarantee against oversmoothing.

## Why the shared encoder is inductive

For the two-transform architecture without biases, the learned matrix count is

$$
N_{\mathrm{parameters}}
=
2\sum_{k=1}^{K}p_kp_{k-1}.
$$

At constant width $$d$$, this is $$2Kd^2$$, independent of $$|V|$$. For a constructed two-layer model with input width three and both output widths four:

$$
2(4\cdot3)+2(4\cdot4)=24+32=56.
$$

Each layer with a bias adds its output width. Pooling networks and LSTMs add their own shared parameters, still without requiring one new parameter vector per node.

Return to the numerical path example. Add a new node $$e$$ with $$x_e=(1,1)^{\mathsf T}$$ and connect it to $$b$$. Its first-layer descriptor is immediately computable:

$$
h_e^{(1)}
=
\operatorname{ReLU}
\left[
\begin{pmatrix}1\\1\end{pmatrix}
+
W_{\mathrm{neigh}}
\begin{pmatrix}0\\2\end{pmatrix}
\right]
=
\begin{pmatrix}3\\3\end{pmatrix}.
$$

No new weights were fitted. For later layers, recompute affected neighbour states because adding the edge changes their neighbourhoods and possibly their degree normalisation.

This requires features with the same meaning and width at training and inference. If the initial state is itself a learned node-ID lookup, or an identity vector whose width grows with the graph, the missing-row problem has merely moved to the input.

Nor can the encoder manufacture distinguishing information. With identical initial features and mean aggregation, every non-isolated node receives the same mean; by induction their states remain identical unless additional information breaks the symmetry.

Finally, parameter independence does not mean memory independence. Materialising one descriptor with $$d$$ coordinates for every node still requires $$O(|V|d)$$ values, plus graph storage. Inductive means the computation is defined for new nodes, not that it is guaranteed to generalise well to a different data distribution.

## Minibatching when the whole graph does not fit

For a simple sum or mean layer of constant width $$d$$, transforming all node states costs $$O(nd^2)$$ and accumulating edge messages costs $$O(|E|d)$$. Across $$K$$ layers this gives

$$
O\left(K(nd^2+|E|d)\right)
$$

arithmetic, with shared intermediate results. Neighbourhood expansion around one target does not mean that a full-graph implementation must independently recompute an exponential tree for every node.

When graph storage, features and training activations exceed available memory, an ordinary in-memory full-batch pass is unavailable. Neighbour sampling is one solution; partitioning and out-of-core execution are alternatives.

Start with the target nodes in a minibatch. Work backwards from the final layer to identify required previous-layer states. For each required node, retain its self dependency and sample neighbours. Then compute forwards from the sampled input features.

If there are $$B$$ targets and at most $$s$$ sampled neighbours at each expansion, each required state introduces at most $$1+s$$ dependencies. After $$K$$ expansions, the number of input occurrences is at most

$$
B(1+s)^K.
$$

For $$B=2,s=3,K=2$$, the bound is $$2\cdot4^2=32$$. Merging repeated nodes can reduce it. Sampling controls degree-driven growth but does not remove the cost of increasing depth.

### What the approximation changes

For uniform sampling with replacement, let $$U_1,\ldots,U_s$$ be independent neighbours of $$v$$. With fixed previous-layer states,

$$
\widehat m_v=\frac1s\sum_{i=1}^{s}h_{U_i},
\qquad
\mathbb E[\widehat m_v]
=
\frac1s\sum_{i=1}^{s}
\frac1{d_v}\sum_{u\in\mathcal N(v)}h_u
=
m_v.
$$

The sample mean is unbiased for the full mean, but any particular estimate can differ.

For a separate example, take neighbour scalars $$2,4,8$$ and sample two without replacement. The three equally likely sample means are

$$
\frac{2+4}{2}=3,
\qquad
\frac{2+8}{2}=5,
\qquad
\frac{4+8}{2}=6.
$$

Their average is $$14/3$$, equal to the full mean, yet none equals that mean.

Unbiased aggregation does not imply unbiased nonlinear output. Sample one of $$-1,1$$ uniformly. The sample's expectation is zero, but

$$
\mathbb E[\operatorname{ReLU}(\widehat m)]
=
\frac12(0+1)=\frac12
\ne
\operatorname{ReLU}(\mathbb E[\widehat m])=0.
$$

To estimate a full sum, multiply a uniform sample mean by the full degree. To estimate a symmetrically weighted sum, sample the weighted messages and apply that same expansion factor. Recomputing degrees solely on the sampled subgraph generally changes the intended operator.

The realised receptive field now follows sampled paths through part of the full neighbourhood. Some nodes within the nominal hop radius contribute nothing on that pass. Sampling therefore changes both numerical precision and which information is available. A permutation test must use corresponding sampled neighbourhoods, or compare output distributions; independent random draws can differ despite an invariant aggregation rule.

## Recommendation and biomedical link prediction

In an item/collection bipartite graph, an edge means an item belongs to a collection. One hop carries information between types; two hops let an item receive information from other items through shared collections. Content features give a new item an input even before it has many edges.

The descriptor can rank candidate items for a collection or retrieve items related to a query item. Consider a query $$q$$, a positive candidate $$p$$ and a sampled negative $$n$$. Write their scores as $$s^+=s(q,p)$$ and $$s^-=s(q,n)$$.

Require the positive to outrank the negative by at least a margin $$\gamma>0$$:

$$
s^+\ge s^-+\gamma.
$$

Moving terms to one side gives violation $$\gamma-s^++s^-$$. Penalising only positive violations produces the margin objective

$$
\mathcal L_{\mathrm{rank}}
=
\sum_{(q,p,n)}
\max(0,\gamma-s(q,p)+s(q,n)).
$$

The margin requests a score gap, not merely correct ordering. In an active term,

$$
\frac{\partial\ell}{\partial s^+}=-1,
\qquad
\frac{\partial\ell}{\partial s^-}=1.
$$

Gradient descent increases the positive score and decreases the negative score. A strictly satisfied constraint has zero gradient.

Construct unit descriptors

$$
z_q=(1,0),
\quad
z_p=(4/5,3/5),
\quad
z_{\mathrm{easy}}=(0,1),
\quad
z_{\mathrm{hard}}=(3/5,4/5).
$$

Their norms are one since, for example, $$16/25+9/25=1$$. Use dot-product scores and margin $$\gamma=3/10$$:

| Candidate | Query dot product | Ranking loss |
| --- | --- | --- |
| Positive | $$4/5$$ | Used as the reference score |
| Easy negative | $$0$$ | $$\max(0,3/10-4/5)=0$$ |
| Harder negative | $$3/5$$ | $$\max(0,3/10-4/5+3/5)=1/10$$ |

The harder negative is already below the positive but is too close to satisfy the margin. Mining high-scoring eligible negatives targets such active constraints.

Random negatives are not inherently useless. They stop contributing to this hinge loss once their constraints are satisfied. If random sampling mostly finds those negatives, mining becomes useful. Normalising descriptors or otherwise constraining their scale also prevents satisfying an already-correct ranking merely by inflating vector norms.

A biomedical graph can similarly use two drug descriptors to score a proposed interaction edge. Different relation types may require different message transforms or decoders. An absent recorded edge is not automatically a confirmed negative, especially when mining plausible candidates.

For link evaluation, held-out target edges must not be supplied as message-passing evidence for the predictions being tested. Claims about unseen drugs also require holding out those nodes, rather than only some edges between already-observed drugs.

## Revision checklist

| Check | What I should reconstruct without looking |
| --- | --- |
| Learning target | Explain how a graph encoder produces fixed-width descriptors and how a loss trains them. |
| Relabelling | Derive $$F(PAP^{\mathsf T},PX)=PF(A,X)$$ and distinguish equivariance from invariant aggregation. |
| Lookup limitation | Count $$nd$$ table parameters and explain why a missing row has no trained value. |
| Layer construction | Derive the separate self and neighbour transforms, with consistent dimensions. |
| Aggregator choice | Calculate sum, mean and max, and exhibit information each can discard. |
| Numerical propagation | Recover the path example's first-layer states and $$h_a^{(2)}=(6,1)^{\mathsf T}$$. |
| Normalisation | Derive mean and symmetric weights and reproduce the star calculation. |
| Architecture | Explain self-loop GCN, separate-slot GraphSAGE, pooling, and the LSTM ordering exception. |
| Receptive field | Prove the hop-radius recursion and distinguish potential reach from actual influence. |
| Oversmoothing | Derive the contraction of the two-node difference under repeated averaging. |
| Induction | Count shared parameters and state the feature assumptions needed for a new node. |
| Sampling | Show an unbiased aggregate estimate whose nonlinear output is biased. |
| Ranking | Derive the margin loss and identify which constructed negative has a nonzero gradient. |
| Evaluation | Distinguish unseen edges from unseen nodes and exclude target-edge leakage. |

## Why it matters for my work

For a patient or biomedical graph, constructing an edge decides which observations may influence each other. I need to inspect that decision alongside feature availability, degree normalisation and the evaluation split. A compact shared encoder can still propagate an inappropriate relationship efficiently.

## What I have not resolved

For a concrete application, I still need to establish whether neighbourhood information adds value beyond node features, which missing edges can serve as negatives, and how predictions change under edge removal or neighbour resampling. Those are experiments to run, not benefits established by the architecture.
