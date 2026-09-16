---
layout: study_note
title: "Deployment, Monitoring, and Human-AI Collaboration"
description: "Drift after deployment, safety monitoring, automation bias, and what changes with a clinician in the loop."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
subgroup: "Generative Systems, Agents & Deployment"
order: 7
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-08-04-medical-algorithmic-audit"
---

Deployment turns a predictor into part of a clinical process. Monitoring observes that process imperfectly, and clinicians can both correct and introduce errors when using its output.

## Core question and definition

The central question is:

> What can be established about the complete system from the signals available after deployment?

A deployed system includes:

- Data interfaces and examination matching.
- Preprocessing and model state.
- Calibration, aggregation, and thresholds.
- Displays and explanations.
- Users, workload, and escalation routes.
- Reference collection and outcome follow-up.
- Update and rollback procedures.

A favorable standalone model estimate addresses only part of this system.

Human involvement does not automatically create a safety mechanism. It changes the decision rule and therefore the object requiring evaluation.

## Key concepts

### 1. Define the deployed decision policy

Let $$X$$ be model input, $$C$$ other information available to the clinician, and $$M=f_\theta(X)$$ the model output.

An assisted action can be written as

$$
a=\pi(X,C,M,W),
$$

where $$W$$ includes workflow conditions such as presentation, available time, and resources.

The relevant risk is

$$
\boxed{
R_{\mathrm{system}}
=
\mathbb E[L(\pi(X,C,f_\theta(X),W),Y)].
}
$$

Changing the interface or escalation procedure can change $$\pi$$ even if $$\theta$$ is fixed.

Standalone model risk,

$$
\mathbb E[\ell(f_\theta(X),Y)],
$$

does not determine system risk without information about how outputs affect actions and consequences.

### 2. Separate directly observable signals from outcome-dependent quantities

| Signal | Available without verified outcomes? | What it can establish |
|---|---|---|
| Missing inputs and interface failures | Usually | Whether expected data reached the system |
| Latency and alert delivery | Usually | Whether outputs arrived under the recorded timing requirements |
| Scanner and acquisition metadata | Often | Whether documented acquisition conditions changed |
| Input or embedding distributions | Yes | A defined statistical change in observed inputs |
| Score and alert distributions | Yes | Changes in model outputs and workload |
| Clinician overrides | Often | Disagreement or changes in action |
| Sensitivity and specificity | No | Require disease status under an adequate reference |
| Calibration | No | Requires outcomes to compare with predicted risks |
| Clinical benefit | No | Requires consequences and an appropriate comparison |

An observable proxy can be useful without being a performance metric.

For example, a change in alert rate may indicate a prevalence change, a threshold error, a scanner change, or a different referral population. The alert rate alone does not identify which occurred.

### 3. Prove why unlabeled monitoring cannot certify correctness

Construct a population with

$$
\Pr(X=0)=\Pr(X=1)=\frac12
$$

and a fixed model

$$
f(X)=X.
$$

Consider two possible outcome relationships:

- World A: $$Y=X$$.
- World B: $$Y=1-X$$.

The input distribution is identical in both worlds. The score distribution, confidence, alert rate, and model version are also identical.

But model error is

$$
R_A=0,
$$

and

$$
R_B=1.
$$

Any monitor observing only inputs and model outputs receives the same information in both worlds. It cannot certify accuracy in both.

This construction is not a proposed clinical scenario. It establishes an information limit: an unseen change in the input-outcome relationship need not be detectable from input summaries.

### 4. Detected drift need not be harmful either

Let input contain a clinical signal and a nuisance variable:

$$
X=(Z,N).
$$

Suppose

$$
Y=Z,
\qquad
f(X)=Z.
$$

If the distribution of $$N$$ changes while $$Z$$ and the target relationship remain unchanged, an input monitor can detect a shift while model accuracy remains perfect.

Thus:

- A detected input shift is not proof of performance loss.
- An absence of detected input shift is not proof of stable performance.

A drift alert should initiate a defined investigation. Its meaning depends on the monitored feature and the clinical pathway.

Embedding stability is also model-dependent: an encoder may discard precisely the distinction that is changing. Agreement between several similar models can remain high if they share the same failure.

### 5. Delayed labels change which patients are visible to monitoring

Let patient $$i$$ arrive at time $$t_i$$ and have a reference delay $$D_i$$. At calendar time $$\tau$$, define

$$
V_i(\tau)
=
\mathbf1\{t_i+D_i\leq\tau
\text{ and reference obtained}\}.
$$

The observed error rate among completed references estimates

$$
\mathbb E[\ell\mid V(\tau)=1].
$$

The desired cohort risk is

$$
\mathbb E[\ell].
$$

They are equal only under an adequate relationship between reference completion and loss.

If errors are associated with delayed recognition or missing follow-up, the completed-reference subset can systematically underrepresent them.

If suspicious cases receive faster verification, the selection can operate differently. The direction cannot be inferred from delay alone.

### 6. A constructed delayed-reference example

Construct a cohort of 100 predictions:

| Eventual classification | Cases | References completed so far |
|---|---:|---:|
| Correct | 80 | 40 |
| Incorrect | 20 | 2 |
| Total | 100 | 42 |

True cohort error, once all outcomes are established, is

$$
\frac{20}{100}=\frac15.
$$

The current completed-reference dashboard reports

$$
\frac2{42}=\frac1{21}.
$$

As references mature, the apparent error rate can increase even though the predictions never changed.

This is a selection effect in outcome availability, not evidence of new model deterioration.

Monitoring should therefore distinguish:

- Calendar time when a label arrives.
- Cohort time when the prediction was made.
- Model and workflow version at prediction time.
- Follow-up completeness for that cohort.
- Which patients remain unverified.

A recent cohort with incomplete references should not be compared naively with a fully matured historical cohort.

### 7. Actions can change the future monitoring data

Deployment can alter the data-generating process:

$$
\text{model output}
\longrightarrow
\text{clinical action}
\longrightarrow
\text{verification and outcome}.
$$

An alert may increase the chance of further investigation. An unflagged case may be less likely to receive a definitive reference. Treatment can also change a future outcome the model was predicting.

Consequently:

- Post-deployment labels may be selectively observed.
- Observed prognosis may depend on model-induced treatment.
- Override rates may reflect workflow or user preferences rather than correctness.
- A declining complaint rate may reflect reduced reporting rather than fewer failures.

The monitoring analysis must preserve the action and reference process. Otherwise a feedback loop can make the dashboard appear stable while its interpretation changes.

### 8. Monitoring thresholds need a sampling interpretation

Suppose a fixed rule produces an alert with probability $$q$$ and a window contains $$n$$ independent cases. The observed alert fraction has variance

$$
\operatorname{Var}(\widehat q)=\frac{q(1-q)}{n}.
$$

Small windows can fluctuate substantially without a true change. Repeated observations from patients or services can add dependence.

Repeated testing also creates repeated opportunities for false alarms. Under a constructed independent sequence of $$T$$ null tests, each with false-alarm probability $$\alpha$$,

$$
\Pr(\text{at least one false alarm})
=
1-(1-\alpha)^T.
$$

A monitoring procedure should therefore specify windows, repeated-look behavior, and what action follows an alert. A fixed threshold applied indefinitely does not inherit the interpretation of one isolated hypothesis test.

Statistical alerts and operational limits also answer different questions. A broken interface can require action regardless of whether enough cases have accumulated for a statistical comparison.

### 9. Derive the general condition for human assistance to help

Let $$H$$ be the unaided human decision and $$A$$ the assisted decision. Define correctness indicators

$$
C_H=\mathbf1\{H=Y\},
\qquad
C_A=\mathbf1\{A=Y\}.
$$

Their difference is:

- One when assistance corrects an unaided error.
- Minus one when assistance overturns an unaided correct decision.
- Zero otherwise.

Therefore,

$$
\boxed{
\Pr(A=Y)-\Pr(H=Y)
=
\Pr(H\neq Y,A=Y)
-
\Pr(H=Y,A\neq Y).
}
$$

Assistance improves accuracy when corrections exceed newly introduced errors.

The model's standalone accuracy does not appear in this identity. It matters through which recommendations are available and how people respond to them.

### 10. Separate opportunity to help from susceptibility to harm

For a simplified binary setting, suppose the assisted decision chooses between the original human answer and the model answer.

Use the joint table:

| | Model correct | Model wrong |
|---|---:|---:|
| Human correct | $$a$$ | $$c$$ |
| Human wrong | $$b$$ | $$d$$ |

Let

$$
r=\Pr(\text{assistance corrects the answer}\mid
\text{human wrong, model correct}),
$$

and

$$
u=\Pr(\text{assistance makes the answer wrong}\mid
\text{human correct, model wrong}).
$$

If both-correct and both-wrong cases retain those outcomes under this restricted choice model, assisted accuracy is

$$
\frac{a+c+rb-uc}{n}.
$$

The change from unaided accuracy is

$$
\boxed{\Delta_{\mathrm{team}}=\frac{rb-uc}{n}.}
$$

The model exceeds human standalone accuracy when

$$
b>c.
$$

The team improves only when

$$
rb>uc.
$$

These are different inequalities.

If users followed the model with the same probability on every discordant case, then $$r=u$$ and a more accurate model would help in this simplified setting. Harm becomes possible through selective reliance, failure to recognize incorrect advice, or additional workflow effects.

### 11. A more accurate model can make the team worse

Construct 100 cases:

| | Model correct | Model wrong |
|---|---:|---:|
| Human correct | 70 | 5 |
| Human wrong | 20 | 5 |

Unaided human accuracy is

$$
\frac{70+5}{100}=\frac34.
$$

Model accuracy is

$$
\frac{70+20}{100}=\frac9{10}.
$$

Now stipulate that assistance corrects only two of the 20 human errors where the model is right:

$$
r=\frac1{10}.
$$

Also stipulate that users accept all five incorrect model recommendations when their original answer was correct:

$$
u=1.
$$

Assisted correctness becomes

$$
75+2-5=72.
$$

Thus,

$$
\boxed{
\operatorname{Accuracy}_{\mathrm{team}}
=
\frac{72}{100}
=
\frac{18}{25}
<
\frac34.
}
$$

The model is correct more often than the unaided human, but the team's use of it is harmful in this construction.

These response probabilities are chosen examples, not empirical estimates of clinician behavior.

Real teams may seek new information or produce answers different from either initial decision. The general corrections-minus-introduced-errors identity still applies; the simplified table would need additional pathways.

### 12. Automation bias concerns reliance behavior

Automation bias can involve accepting incorrect advice or failing to act because no automated prompt appeared.

An explanation or confidence display may affect both:

- The probability of accepting a useful correction.
- The probability of accepting an incorrect recommendation.

Increasing trust is therefore not the same as improving decision quality.

An evaluation should inspect:

- Whether users detect incorrect recommendations.
- Whether absence of an alert suppresses independent review.
- Whether explanations help identify errors.
- Whether behavior changes with workload and familiarity.
- Whether different users benefit or lose performance.
- Whether assistance changes reading of unflagged regions.

The desired outcome is appropriate reliance, measured through actions and consequences.

### 13. Review capacity creates another system constraint

Let $$Q_t$$ be the review backlog, $$A_t$$ new alerts, and $$C_t$$ review capacity during interval $$t$$.

A simple queue evolves as

$$
\boxed{
Q_{t+1}=\max\{0,Q_t+A_t-C_t\}.
}
$$

Because the maximum is at least its second argument,

$$
Q_T\geq Q_0+\sum_{t=0}^{T-1}(A_t-C_t).
$$

If expected arrivals exceed expected capacity by a persistent amount, expected backlog cannot remain bounded under this model.

Construct ten new alerts and capacity for six reviews each day, starting from zero:

| Day | Backlog after review |
|---|---:|
| 0 | 0 |
| 1 | 4 |
| 2 | 8 |
| 3 | 12 |

A useful prediction delivered into an unmanageable queue can fail to produce a timely action.

Arrival rates below capacity are not alone a complete guarantee of acceptable delays; variability, priorities, and scheduling matter. The calculation establishes why workload belongs in system evaluation rather than being treated as an implementation detail.

### 14. Evaluate the team and the workflow

A team evaluation should specify the policy being compared:

$$
\pi_{\mathrm{unaided}},
\qquad
\pi_{\mathrm{assisted}}.
$$

For a clinically relevant loss,

$$
\Delta_R
=
\mathbb E[L(\pi_{\mathrm{assisted}},Y)]
-
\mathbb E[L(\pi_{\mathrm{unaided}},Y)].
$$

The study should measure this difference under a design that supports the intended comparison.

Relevant outcomes include:

- Missed and unnecessary actions.
- Severity-weighted errors.
- Appropriate escalation.
- Reading and response time.
- Workload and queue effects.
- Failures to deliver or interpret outputs.
- Patient consequences where the design can observe them.

Reader studies must account for case difficulty, reader sampling, and order effects. Showing the same case first unaided and then assisted can introduce recall and additional deliberation. Randomization and counterbalancing help address these issues, but the design must still match the claim.

Comparative clinical use evaluates the complete policy. If shared resources create interference between patients, the assignment and analysis unit should reflect that workflow.

### 15. Version the intervention being monitored

The relevant version includes more than model weights:

$$
V=
(\text{input rules},
\text{preprocessing},
\text{model state},
\text{calibration},
\text{threshold},
\text{interface},
\text{workflow}).
$$

A threshold change can alter workload. An interface change can alter reliance. A preprocessing change can alter predictions. All can change system risk.

Monitoring records should link each prediction to:

- The correct patient and examination.
- The inputs available at that moment.
- The complete version.
- The output and delivery time.
- The user response.
- The reference and its later revisions.
- Any subsequent update or rollback.

Mixing outcomes from several versions without attribution can obscure both the cause of a problem and whether a correction worked.

### 16. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What is the deployed system's risk? | Loss under the full action policy, including users and workflow |
| What can be monitored without labels? | Inputs, outputs, process failures, workload, and user actions |
| Why are these proxies insufficient? | Identical unlabeled observations can coexist with different correctness |
| Does detected drift imply harm? | No; irrelevant input components can change |
| Why do delayed labels distort dashboards? | Completed references may select a different error distribution |
| When does assistance improve accuracy? | When corrected human errors exceed newly introduced errors |
| Can a more accurate model worsen the team? | Yes; selective reliance can satisfy $$rb<uc$$ despite $$b>c$$ |
| Why does review capacity matter? | Excess arrivals create an accumulating backlog |
| What should a team evaluation compare? | Defined assisted and comparator policies under an appropriate design |
| What must be versioned? | The complete prediction-and-action pipeline |

In the ontology, monitoring methods assess particular observable properties. Proxy stability does not establish clinical validity or utility. The clinical target sets requirements for detection, escalation, workload, and the consequences of human-AI interaction.

## Why it matters for my work

For gallbladder AI, clinical faithfulness audits could help explain a change in behavior, but monitoring must also establish what clinicians saw and did. A prediction supported by appropriate evidence can still fail through timing, routing, or inappropriate reliance.

## What I have not resolved

- Which proxies are useful enough to trigger investigation before outcomes mature?
- Which presentation helps users recognize incorrect advice?
- Which outcomes and capacity measures capture the complete workflow's benefit?

---

Sources: Independent study; the monitoring counterexamples, delayed-reference example, team-performance identities, and queue calculations are constructed and derived above. They are not empirical estimates of clinician behavior or clinical service capacity. These are study notes for research purposes, not clinical guidance.
