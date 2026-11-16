# Review draft

## q01 (answerable) — status: answered
Q: What does the paper propose instead of looking backwards and preserving prior regressor data?
EXPECTED: A procedure for the offline generation of a persistently exciting reference trajectory that perturbs the equilibrium.
GOLD: 2004.01625v2 p1: "Instead, we present a procedure for the offline generation of a persistently exciting reference trajectory perturbing the equilibrium."
AGENT: Instead of looking backwards and preserving prior regressor data, the paper proposes an adaptive model predictive control approach with conditions that guarantee a persistently exciting closed-loop sequence by only looking forward in time into the receding prediction horizon. It also presents a procedure for the offline generation of a persistently exciting reference trajectory that perturbs the equilibrium [37b7e41105248297da3b].
- [37b7e41105248297da3b] [CONTAINS GOLD EVIDENCE]: Forward-looking persistent excitation in model predictive

control

Sven Brüggemann a Robert R. Bitmead a

aMechanical & Aerospace Engineering Department, University of California, San Diego, CA 92093-0411, USA, (e-mails:

{sbruegge, rbitmead}@eng.ucsd.edu)

A

## q02 (answerable) — status: answered
Q: Which stochastic MPC algorithm is designed by using time-varying probabilistic reachable sets as the tubes?
EXPECTED: The probabilistically resolvable time-varying tube-based stochastic model predictive control algorithm.
GOLD: 2104.10383v1 p1: "Firstly, the probabilistically resolvable time-varying tube-based stochastic model predictive control algorithm is designed by employing the time-varying probab"
AGENT: The algorithm is the **probabilistically resolvable time-varying tube-based stochastic model predictive control (pTTSMPC)** algorithm. It is designed by employing **time-varying probabilistic reachable sets (PRS) as the tubes** [73d0d617dbbd09f4f8c4; 7d19a06f03d13e433fbe].
- [73d0d617dbbd09f4f8c4] [CONTAINS GOLD EVIDENCE]: Abstract—This paper presents two stochastic model predictive
control methods for linear time-invariant systems subject to
unbounded additive uncertainties. The new methods are developed by formulating the chance constraints into deterministic
form, which are t
- [7d19a06f03d13e433fbe]: • A new SMPC algorithm for the LTI system subject to
unbounded uncertainties termed as the probabilistically
resolvable time-varying tube-based SMPC (pTTSMPC)
is developed. In particular, the PRS built from the uncertainty propagation is treated as the tube, b

## q03 (answerable) — status: abstain
Q: How many datasets and how many offline reinforcement learning algorithms does the autonomous driving benchmark provide?
EXPECTED: 19 datasets, including real-world human driver datasets, and seven offline RL algorithms in three driving scenarios.
GOLD: 2404.02429v1 p1: "We provide 19 datasets, including realworld human driver’s datasets, and seven popular offline reinforcement learning algorithms in three realistic driving scen"
AGENT: Không đủ bằng chứng để trả lời.

## q04 (answerable) — status: answered
Q: How does the paper reframe offline RL so that the best behaviours can be stitched together from sub-optimal experts?
EXPECTED: It reformulates offline RL as an optimal transportation problem and learns a policy mapping states to a partial distribution of the best expert actions.
GOLD: 2410.14069v1 p1: "we rethink offline reinforcement learning as an optimal transportation problem."
AGENT: The paper reframes offline RL by viewing the entire offline RL problem as an optimal transport problem, rather than introducing a new OT-based regularization or reward function [6d748129f3dd2a58c361]. Its goal is to stitch the best trajectories rather than clone the behavior policy [6d748129f3dd2a58c361]. This matters because offline datasets can contain demonstrations from various experts, some incorrect or efficient only for certain parts of the environment, so cloning can limit policy improvement; stitching instead selects the best action for each state and recombines trajectories from multiple experts [6d748129f3dd2a58c361]. The method uses partial OT to handle sub-optimal trajectories by mapping states only to the most relevant parts of the action distribution with respect to the critic function Q, using inequality constraints instead of equality constraints [cff6e77be15ba4f350a8]. The paper describes using the action-value function and policy as components of the OT problem between states and actions, and applying partial optimal transport so the algorithm selects and maps the best expert actions for each state, enabling efficient policy extraction from noisy or sub-optimal datasets [fb6011bde1dfcf5ef473].
- [6d748129f3dd2a58c361]: As an example of BC loss, Optimal Transport (OT) [50] distance has been introduced for RL. This
application of OT is particularly relevant because by minimizing the OT distance between policies, we
can efficiently clone the behavior [52, 11, 40, 34, 20, 9, 35]
- [cff6e77be15ba4f350a8]: 3.2
Stitching with Partial OT

In many real-world applications, collecting high-quality datasets may be costly or impractical.
Therefore, offline RL algorithms need to select the best actions provided by the experts and ignore
sub-optimal ones. Our idea is tha
- [fb6011bde1dfcf5ef473]: In this paper, we have established the novel algorithm for offline reinforcement learning. Our work
introduces the concept using the action-value function and the policy as components of the OT
problem between states and actions. To demonstrate the potential o

## q05 (answerable) — status: answered
Q: What is described as the main problem faced by all current offline model-based reinforcement learning methods?
EXPECTED: Distributional shift.
GOLD: 2305.03360v1 p1: "particularly their approaches in solving the issue of distributional shift, the main problem faced by all current offline model-based reinforcement learning met"
AGENT: The main problem is **distributional shift**. The survey states that current offline model-based reinforcement learning methods are particularly concerned with solving distributional shift, described as “the main problem faced by all current offline model-based reinforcement learning methods” [c6a0bc25e4dd91330b99]. It also says distributional shift “remains the most influential problem” in offline model-based RL and that no approach has provided a theoretically provable, data-non-reliant absolute performance guarantee because of it [1dda3e750f9589ffb178]. The paper further notes that offline model-based RL grapples with distributional shifts in both state and action distributions, exacerbated by model exploitation [11370be916e3beb0055a].
- [11370be916e3beb0055a]: 2
Offline Model-Based Reinforcement Learning

The intersection of the two previously discussed concepts defines offline model-based reinforcement learning. Analogous to online model-based RL methods, offline model-based RL approaches
initially estimate state t
- [1dda3e750f9589ffb178]: 3
Challenges and Future Work

Distributional shift remains the most influential problem in offline model-based reinforcement learning, and warrants further research. Even though the discussed relevant work have proposed various
methods to mitigate this problem
- [c6a0bc25e4dd91330b99] [CONTAINS GOLD EVIDENCE]: Model-based approaches are becoming increasingly popular in the field of offline
reinforcement learning, with high potential in real-world applications due to the
model’s capability of thoroughly utilizing the large historical datasets available
with supervise

## q07 (answerable) — status: abstain
Q: What does the DPE algorithm blend into a unified framework?
EXPECTED: Offline sequence modeling and offline reinforcement learning, with Double Policy Estimation.
GOLD: 2308.14897v1 p1: "we propose DPE: an RL algorithm that blends offline sequence modeling and offline reinforcement learning with Double Policy Estimation (DPE) in a unified framew"
AGENT: Không đủ bằng chứng để trả lời.

## q08 (answerable) — status: answered
Q: How is the classical reinforcement learning formulation made robust without changing the algorithm class?
EXPECTED: By adding standard deviation penalization of the objective, giving a risk-averse formulation.
GOLD: 2206.06841v1 p1: "We show that the classical Reinforcement Learning formulation can be robustified using standard deviation penalization of the objective."
AGENT: The classical RL formulation is robustified by adding a standard-deviation penalization to the objective, i.e., using a mean–standard-deviation risk-averse formulation. This approximates a Robust Distributional RL heuristic with Φ-divergence constraints. The resulting algorithms are based on Distributional Reinforcement Learning, with one for discrete and one for continuous action spaces [7d126688a9e61a223e64][4830cc6970b8e873c143]. The approach requires little additional parameter tuning; only the mean–standard deviation trade-off must be chosen carefully [4830cc6970b8e873c143].
- [4830cc6970b8e873c143]: In this paper, we show that it is possible to approximate
a Robust Distributional Reinforcement Learning heuristic
with Φ-divergence constraints into a Risk-averse formulation, using a formulation based on mean-standard deviation
optimization. Moreover, we foc
- [7d126688a9e61a223e64] [CONTAINS GOLD EVIDENCE]: Robust Reinforcement Learning with Distributional Risk-averse formulation

Pierre Clavier 1 2 Stéphanie Allassonnière 2 Erwan Le Pennec 1

Abstract

Robust Reinforcement Learning tries to make predictions more robust to changes in the dynamics
or rewards of th

## q09 (answerable) — status: abstain
Q: What training speedup was reported after re-implementing the Attention Model and training it with PPO in CleanRL?
EXPECTED: At least 8 times speed up in training time.
GOLD: 2303.13117v1 p1: "we re-implemented the Attention Model and trained it with Proximal Policy Optimization in CleanRL, showing at least 8 times speed up in training time."
AGENT: Không đủ bằng chứng để trả lời.

## q10 (answerable) — status: answered
Q: What kind of regularization does Sparse-Reg use to mitigate overfitting on small offline datasets?
EXPECTED: A sparsity-based regularization technique that regularizes model complexity.
GOLD: 2506.17155v2 p1: "we introduce "Sparse-Reg": a regularization technique based on sparsity to mitigate overfitting in offline reinforcement learning, enabling effective learning i"
AGENT: Sparse-Reg uses **sparsity-based regularization**—specifically, sparse regularization of the model/parameter space—to mitigate overfitting on small offline datasets [cf12cac5882d85a30193] [92e87828ff6d3545b81c]. It selects a subset of parameters using a mask derived from a gradient-based connection-sensitivity measure, identifying “top-k” important parameters [cd707f0f3cf4807fb4c1] [848c44ec968ebb902fb4].
- [848c44ec968ebb902fb4]: We apply Sparse-Reg by selecting a subset of parameters f(x, θ ⊙m) by using a mask m ∈{0, 1}|θ|

derived through Equation (1). The regularization is governed by sparsity, which refers to the
proportion of parameters that are pruned and set to zero. By increasi
- [92e87828ff6d3545b81c]: 6
Discussion

We explore the use of small datasets within the realm of offline RL for continuous control tasks.
While many standard offline RL benchmarks involve datasets containing well over a million data
points, it is important to recognize that numerous ap
- [cd707f0f3cf4807fb4c1]: 4
Sparse-Reg: Sparse Regularization for Offline RL

We propose using sparse regularization to regularize model complexity when learning from small
datasets. We use a gradient-based method proposed in Lee et al. (2018) that identifies important
parameters by us
- [cf12cac5882d85a30193] [CONTAINS GOLD EVIDENCE]: arXiv:2506.17155v2 [cs.LG] 26 Jun 2025

Sparse-Reg: Improving Sample Complexity in Offline
Reinforcement Learning using Sparsity

Samin Yeasar Arnob1,2, Scott Fujimoto3, Doina Precup1,2

samin.arnob@mail.mcgill.ca

1Department of Computing Science, McGill Univ

## q11 (answerable) — status: answered
Q: What class of generative models does SORL leverage to scale both training and inference?
EXPECTED: Shortcut models.
GOLD: 2505.22866v1 p1: "we introduce Scalable Offline Reinforcement Learning (SORL), a new offline RL algorithm that leverages shortcut models—a novel class of generative models—to sca"
AGENT: SORL leverages **shortcut models**, described as "a novel class of generative models," to scale both training and inference [b0e12c3edb7c000680c6].
- [b0e12c3edb7c000680c6] [CONTAINS GOLD EVIDENCE]: Diffusion and flow models have emerged as powerful generative approaches capable of modeling diverse and multimodal behavior. However, applying these models
to offline reinforcement learning (RL) remains challenging due to the iterative
nature of their noise s

## q12 (answerable) — status: answered
Q: In which space is the infinitesimal generator of controlled diffusion processes learned?
EXPECTED: In a reproducing kernel Hilbert space.
GOLD: 2511.10383v2 p1: "we represent our world model in terms of the infinitesimal generator of controlled diffusion processes learned in a reproducing kernel Hilbert space."
AGENT: The infinitesimal generator of controlled diffusion processes is learned in a reproducing kernel Hilbert space (RKHS) [d7c6c4009ef1689927f1]. The value function is approximated in a sample-induced subspace of an RKHS [2cc7138443b9d32e443d].
- [2cc7138443b9d32e443d]: Our nonparametric kernel formulation avoids
grid-based state discretization by approximating the value
function in a sample-induced subspace of a Reproducing
Kernel Hilbert Space (RKHS), with computational aspects
discussed in Section VIII.
Contributions. In t
- [d7c6c4009ef1689927f1] [CONTAINS GOLD EVIDENCE]: ABSTRACT Continuous-time stochastic processes underlie many natural and engineered systems. In
healthcare, autonomous driving, and industrial control, direct interaction with the environment is often
unsafe or impractical, motivating offline reinforcement lear

## q13 (answerable) — status: answered
Q: According to the negative result, what happens to well-studied reinforcement learning settings with function approximation when they are composed with rich observations?
EXPECTED: They become intractable.
GOLD: 2410.17904v1 p1: "our main negative result shows that most well-studied settings for reinforcement learning with function approximation become intractable when composed with rich"
AGENT: According to the paper's main negative result, most well-studied settings for reinforcement learning with function approximation become intractable when composed with rich observations [5ee52cd69d1a772343ec].
- [5ee52cd69d1a772343ec] [CONTAINS GOLD EVIDENCE]: This paper addresses the question of reinforcement learning under general latent dynamics from a
statistical and algorithmic perspective. On the statistical side, our main negative result shows that
most well-studied settings for reinforcement learning with fu

## q14 (answerable) — status: answered
Q: In the 2024 paper that reformulates offline RL with optimal transport, on which benchmark suite is the algorithm evaluated?
EXPECTED: The D4RL suite (continuous control problems).
GOLD: 2410.14069v1 p1: "We evaluate the performance of our algorithm on continuous control problems from the D4RL suite and demonstrate improvements over existing methods."
AGENT: The algorithm is evaluated on continuous control problems from the D4RL suite [3b617af7d62397a7dfaa].
- [3b617af7d62397a7dfaa] [CONTAINS GOLD EVIDENCE]: Rethinking Optimal Transport in

Offline Reinforcement Learning

Arip Asadulaev1,2 Rostislav Korst4 Alexander Korotin3,1

Vage Egiazarian5,6 Andrey Filchenkov2 Evgeny Burnaev3,1

1AIRI
2ITMO
3Skoltech
4MIPT
5Yandex
6HSE University
aripasadulaev@airi.net

Abstr

## u01 (UNANSWERABLE) — status: abstain
Q: Which theorem in the corpus establishes a polynomial-time algorithm for computing the optimal policy in partially observable MDPs?
VERIFY (unanswerable): Scan over pages.jsonl: 'polynomial-time algorithm' 0 pages; 'polynomial in' appears only as a statistical-complexity statement in 2511.10383v2, not a POMDP policy theorem. 'partially observable' occur
AGENT: Không đủ bằng chứng để trả lời.

## u02 (UNANSWERABLE) — status: abstain
Q: What is the exact numerical Lipschitz constant that the papers derive for the contraction mapping of the Q-learning operator?
VERIFY (unanswerable): Scan over pages.jsonl: 'Lipschitz constant' only in 2511.10383v2 pp.14-16 (symbol L, no numerical value); 'contraction' 1 page (2511.10383v2 p15, HJB-level estimate, not Q-learning); no paper derives 
AGENT: Không đủ bằng chứng để trả lời.

## q06 (answerable) — status: answered
Q: How does the regret of the admission control algorithm scale with the maximal number of jobs in the network?
EXPECTED: Sub-linearly in the maximal number of jobs S.
GOLD: 2308.02391v1 p1: "a regret that only depends sub-linearly on the maximal number of jobs in the network, S."
AGENT: The admission control algorithm’s regret depends only sub-linearly on the maximal number of jobs in the network, \(S\). In contrast with existing regret analyses, the bound does not depend on the diameter of the underlying MDP, which in most queueing systems is at least exponential in \(S\) [36412c830e6b326a10b5].
- [36412c830e6b326a10b5] [CONTAINS GOLD EVIDENCE]: a regret that only depends sub-linearly on the maximal number of jobs in the
network, S. In particular, in contrast with existing regret analyses, our regret
bound does not depend on the diameter of the underlying Markov Decision
Process (MDP), which in most q

## q15 (answerable) — status: answered
Q: In the eess.SY papers, what is combined with adaptive model predictive control to obtain exponential convergence of nonlinear systems despite bounded noise?
EXPECTED: A recursive least squares identifier with forgetting factor.
GOLD: 2004.01625v2 p1: "With the new approach we demonstrate exponential convergence of nonlinear systems under the influence of the adaptive model predictive control combined with a r"
AGENT: Adaptive model predictive control is combined with a recursive least squares identifier with forgetting factor to obtain exponential convergence of nonlinear systems despite bounded noise [37b7e41105248297da3b]. The same paper also describes bringing in the parameter estimator as recursive least squares with forgetting factor [683e46a9d7af18c40ac4].
- [37b7e41105248297da3b] [CONTAINS GOLD EVIDENCE]: Forward-looking persistent excitation in model predictive

control

Sven Brüggemann a Robert R. Bitmead a

aMechanical & Aerospace Engineering Department, University of California, San Diego, CA 92093-0411, USA, (e-mails:

{sbruegge, rbitmead}@eng.ucsd.edu)

A
- [683e46a9d7af18c40ac4]: 5i) Apply reference tracking MPC of Köhler et al.
(2018) to the period-M reference above. This guarantees exponential convergence to the PE reference
from an open set of initial conditions, when there is
no state disturbance and known parameter. With a
suitabl
