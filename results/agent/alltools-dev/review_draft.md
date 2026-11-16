# Review draft

## q01 (answerable) — status: abstain
Q: What does the paper propose instead of looking backwards and preserving prior regressor data?
EXPECTED: A procedure for the offline generation of a persistently exciting reference trajectory that perturbs the equilibrium.
GOLD: 2004.01625v2 p1: "Instead, we present a procedure for the offline generation of a persistently exciting reference trajectory perturbing the equilibrium."
AGENT: Không đủ bằng chứng để trả lời.

## q02 (answerable) — status: answered
Q: Which stochastic MPC algorithm is designed by using time-varying probabilistic reachable sets as the tubes?
EXPECTED: The probabilistically resolvable time-varying tube-based stochastic model predictive control algorithm.
GOLD: 2104.10383v1 p1: "Firstly, the probabilistically resolvable time-varying tube-based stochastic model predictive control algorithm is designed by employing the time-varying probab"
AGENT: The probabilistically resolvable time-varying tube-based stochastic model predictive control (pTTSMPC) algorithm [73d0d617dbbd09f4f8c4, 7d19a06f03d13e433fbe].
- [73d0d617dbbd09f4f8c4] [CONTAINS GOLD EVIDENCE]: Abstract—This paper presents two stochastic model predictive
control methods for linear time-invariant systems subject to
unbounded additive uncertainties. The new methods are developed by formulating the chance constraints into deterministic
form, which are t
- [7d19a06f03d13e433fbe]: • A new SMPC algorithm for the LTI system subject to
unbounded uncertainties termed as the probabilistically
resolvable time-varying tube-based SMPC (pTTSMPC)
is developed. In particular, the PRS built from the uncertainty propagation is treated as the tube, b

## q03 (answerable) — status: answered
Q: How many datasets and how many offline reinforcement learning algorithms does the autonomous driving benchmark provide?
EXPECTED: 19 datasets, including real-world human driver datasets, and seven offline RL algorithms in three driving scenarios.
GOLD: 2404.02429v1 p1: "We provide 19 datasets, including realworld human driver’s datasets, and seven popular offline reinforcement learning algorithms in three realistic driving scen"
AGENT: The autonomous driving benchmark provides 19 datasets and 7 offline reinforcement learning algorithms [c099dfc8190fd395b1e5].
- [c099dfc8190fd395b1e5] [CONTAINS GOLD EVIDENCE]: AD4RL: Autonomous Driving Benchmarks for
Offline Reinforcement Learning with Value-based Dataset

Dongsu Lee†, Chanin Eom†, and Minhae Kwon†,∗

Abstract— Offline reinforcement learning has emerged as a
promising technology by enhancing its practicality through

## q04 (answerable) — status: answered
Q: How does the paper reframe offline RL so that the best behaviours can be stitched together from sub-optimal experts?
EXPECTED: It reformulates offline RL as an optimal transportation problem and learns a policy mapping states to a partial distribution of the best expert actions.
GOLD: 2410.14069v1 p1: "we rethink offline reinforcement learning as an optimal transportation problem."
AGENT: The paper reframes offline RL as an optimal transport (OT) problem between states and actions, where the action-value function and policy are treated as components of the OT formulation [fb6011bde1dfcf5ef473]. Unlike prior OT-based approaches that use OT for behavior cloning or regularization [6d748129f3dd2a58c361], the authors propose viewing the entire offline RL problem as an OT problem with the goal of *stitching* the best trajectories from sub-optimal experts. Specifically, they apply *partial optimal transport* to select and map the best expert actions for each state, effectively recombining trajectories from multiple experts rather than cloning a single behavior policy [fb6011bde1dfcf5ef473, 6d748129f3dd2a58c361]. This reframing enables the algorithm to avoid inefficient actions in the dataset and extract an improved policy by stitching together optimal segments from different experts.
- [6d748129f3dd2a58c361]: As an example of BC loss, Optimal Transport (OT) [50] distance has been introduced for RL. This
application of OT is particularly relevant because by minimizing the OT distance between policies, we
can efficiently clone the behavior [52, 11, 40, 34, 20, 9, 35]
- [fb6011bde1dfcf5ef473]: In this paper, we have established the novel algorithm for offline reinforcement learning. Our work
introduces the concept using the action-value function and the policy as components of the OT
problem between states and actions. To demonstrate the potential o

## q05 (answerable) — status: answered
Q: What is described as the main problem faced by all current offline model-based reinforcement learning methods?
EXPECTED: Distributional shift.
GOLD: 2305.03360v1 p1: "particularly their approaches in solving the issue of distributional shift, the main problem faced by all current offline model-based reinforcement learning met"
AGENT: The main problem faced by all current offline model-based reinforcement learning methods is described as the issue of distributional shift [c6a0bc25e4dd91330b99, a440776b6b0d2cdd9d03, 1dda3e750f9589ffb178].
- [1dda3e750f9589ffb178]: 3
Challenges and Future Work

Distributional shift remains the most influential problem in offline model-based reinforcement learning, and warrants further research. Even though the discussed relevant work have proposed various
methods to mitigate this problem
- [a440776b6b0d2cdd9d03]: arXiv:2305.03360v1 [cs.LG] 5 May 2023

A Survey on Offline Model-Based Reinforcement

Learning

Haoyang He
Electrical and Computer Engineering

Carnegie Mellon University

Pittsburgh, PA 15213
hhe2@andrew.cmu.edu

Abstract
- [c6a0bc25e4dd91330b99] [CONTAINS GOLD EVIDENCE]: Model-based approaches are becoming increasingly popular in the field of offline
reinforcement learning, with high potential in real-world applications due to the
model’s capability of thoroughly utilizing the large historical datasets available
with supervise

## q06 (answerable) — status: answered
Q: How does the regret of the admission control algorithm scale with the maximal number of jobs in the network?
EXPECTED: Sub-linearly in the maximal number of jobs S.
GOLD: 2308.02391v1 p1: "a regret that only depends sub-linearly on the maximal number of jobs in the network, S."
AGENT: The regret of the admission control algorithm scales logarithmically with the maximal number of jobs in the network, S. Specifically, as the number of jobs S scales multiplicatively, the regret increases in log(S) [36412c830e6b326a10b5,13dd2d1fb2dc2a687e43]. This is much slower than square root bounds reported under strong assumptions, indicating a sub-linear dependence on S [36412c830e6b326a10b5].
- [13dd2d1fb2dc2a687e43]: 0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Time-steps
×107

0.0

0.5

1.0

1.5

2.0

Regret

×106

Regret with 3 queues per tier
Regret with 6 queues per tier
Regret with 12 queues per tier
Regret with 24 queues per tier

Parameter
Value

S
10
3 n

λ
0.99

μ
- [36412c830e6b326a10b5] [CONTAINS GOLD EVIDENCE]: a regret that only depends sub-linearly on the maximal number of jobs in the
network, S. In particular, in contrast with existing regret analyses, our regret
bound does not depend on the diameter of the underlying Markov Decision
Process (MDP), which in most q

## q07 (answerable) — status: answered
Q: What does the DPE algorithm blend into a unified framework?
EXPECTED: Offline sequence modeling and offline reinforcement learning, with Double Policy Estimation.
GOLD: 2308.14897v1 p1: "we propose DPE: an RL algorithm that blends offline sequence modeling and offline reinforcement learning with Double Policy Estimation (DPE) in a unified framew"
AGENT: The DPE algorithm blends the behavior policy and the target policy into a unified framework by jointly estimating both policies and using them to compute the DPE cumulative density ratio [3d0a1e37780442cbc5cb]. Specifically, it obtains the maximum likelihood estimates of the behavior policy π̂b(η) and the evaluation (target) policy π̂t(ψ), then uses these estimates to approximate the target policy and correct sampling errors in sequence-modeling-based reinforcement learning [3d0a1e37780442cbc5cb].
- [3d0a1e37780442cbc5cb]: 4
Methodology

In this section, we present the primary focus of our work: double policy estimation (DPE) importance
sampling that corrects for sampling error in sequence modeling-based reinforcement learning. The
key idea is to obtain the maximum likelihood es

## q08 (answerable) — status: answered
Q: How is the classical reinforcement learning formulation made robust without changing the algorithm class?
EXPECTED: By adding standard deviation penalization of the objective, giving a risk-averse formulation.
GOLD: 2206.06841v1 p1: "We show that the classical Reinforcement Learning formulation can be robustified using standard deviation penalization of the objective."
AGENT: The classical reinforcement learning formulation is made robust without changing the algorithm class by incorporating a standard deviation penalization into the objective, i.e., using a mean-standard deviation optimization approach. This transforms the problem into a risk-averse formulation that approximates a robust distributional reinforcement learning heuristic with Φ-divergence constraints [4830cc6970b8e873c143]. The approach is demonstrated to be robust to changes in dynamics while remaining within the distributional reinforcement learning framework, requiring only careful selection of the mean-standard deviation trade-off parameter [4830cc6970b8e873c143, 7d126688a9e61a223e64].
- [4830cc6970b8e873c143]: In this paper, we show that it is possible to approximate
a Robust Distributional Reinforcement Learning heuristic
with Φ-divergence constraints into a Risk-averse formulation, using a formulation based on mean-standard deviation
optimization. Moreover, we foc
- [7d126688a9e61a223e64] [CONTAINS GOLD EVIDENCE]: Robust Reinforcement Learning with Distributional Risk-averse formulation

Pierre Clavier 1 2 Stéphanie Allassonnière 2 Erwan Le Pennec 1

Abstract

Robust Reinforcement Learning tries to make predictions more robust to changes in the dynamics
or rewards of th

## q09 (answerable) — status: answered
Q: What training speedup was reported after re-implementing the Attention Model and training it with PPO in CleanRL?
EXPECTED: At least 8 times speed up in training time.
GOLD: 2303.13117v1 p1: "we re-implemented the Attention Model and trained it with Proximal Policy Optimization in CleanRL, showing at least 8 times speed up in training time."
AGENT: The training of the Attention Model was reported to be sped up by 8 times after re-implementing it with PPO in CleanRL (e.g., 25 hours → 3 hours) [ad8b0c365edc368819a6].
- [ad8b0c365edc368819a6]: We performed experiments on several RL platforms and find that CleanRL
(Huang et al., 2022b) has the lowest overhead and thus the highest efficiency..

We introduce the RLOR framework, which consists of four parts: model, algorithm, environment,
and search. Th

## q10 (answerable) — status: answered
Q: What kind of regularization does Sparse-Reg use to mitigate overfitting on small offline datasets?
EXPECTED: A sparsity-based regularization technique that regularizes model complexity.
GOLD: 2506.17155v2 p1: "we introduce "Sparse-Reg": a regularization technique based on sparsity to mitigate overfitting in offline reinforcement learning, enabling effective learning i"
AGENT: Sparse-Reg uses a regularization technique based on sparsity to mitigate overfitting in offline reinforcement learning [cf12cac5882d85a30193, 7678c005ed27f50c1f11].
- [7678c005ed27f50c1f11]: 1
Introduction

Reinforcement Learning (RL) is a powerful approach to solving complex problems, but its application
can be challenging due to the need for active interaction with the environment. In many scenarios,
collecting training data can be challenging o
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
AGENT: SORL leverages diffusion or flow generative models to scale both training and inference [a67341d4c59200ef8d3c].
- [a67341d4c59200ef8d3c]: Generative models such as diffusion and flow models inherently support inference-time sequential
scaling by varying the number of denoising steps [Sohl-Dickstein et al., 2015, Lipman et al., 2024],
and recent work extends their inference-time scaling capabilit

## q12 (answerable) — status: answered
Q: In which space is the infinitesimal generator of controlled diffusion processes learned?
EXPECTED: In a reproducing kernel Hilbert space.
GOLD: 2511.10383v2 p1: "we represent our world model in terms of the infinitesimal generator of controlled diffusion processes learned in a reproducing kernel Hilbert space."
AGENT: The infinitesimal generator of controlled diffusion processes is learned in a reproducing kernel Hilbert space (RKHS) [d7c6c4009ef1689927f1][c12b084a32033d12c119][2cc7138443b9d32e443d].
- [2cc7138443b9d32e443d]: Our nonparametric kernel formulation avoids
grid-based state discretization by approximating the value
function in a sample-induced subspace of a Reproducing
Kernel Hilbert Space (RKHS), with computational aspects
discussed in Section VIII.
Contributions. In t
- [c12b084a32033d12c119]: V. STATISTICAL LEARNING OF WORLD MODELS
To build an infinitesimal world model and solve the HJB
via a simple dynamic programming recursion (P3), we seek
a data-driven approximation of the infinitesimal generator
G : D(G) →L2

η, with D(G) a space with sufficie
- [d7c6c4009ef1689927f1] [CONTAINS GOLD EVIDENCE]: ABSTRACT Continuous-time stochastic processes underlie many natural and engineered systems. In
healthcare, autonomous driving, and industrial control, direct interaction with the environment is often
unsafe or impractical, motivating offline reinforcement lear

## q13 (answerable) — status: answered
Q: According to the negative result, what happens to well-studied reinforcement learning settings with function approximation when they are composed with rich observations?
EXPECTED: They become intractable.
GOLD: 2410.17904v1 p1: "our main negative result shows that most well-studied settings for reinforcement learning with function approximation become intractable when composed with rich"
AGENT: According to the negative result, most well-studied reinforcement learning settings with function approximation become intractable when composed with rich observations [5ee52cd69d1a772343ec].
- [5ee52cd69d1a772343ec] [CONTAINS GOLD EVIDENCE]: This paper addresses the question of reinforcement learning under general latent dynamics from a
statistical and algorithmic perspective. On the statistical side, our main negative result shows that
most well-studied settings for reinforcement learning with fu

## q14 (answerable) — status: answered
Q: In the 2024 paper that reformulates offline RL with optimal transport, on which benchmark suite is the algorithm evaluated?
EXPECTED: The D4RL suite (continuous control problems).
GOLD: 2410.14069v1 p1: "We evaluate the performance of our algorithm on continuous control problems from the D4RL suite and demonstrate improvements over existing methods."
AGENT: The algorithm is evaluated on the D4RL suite [3b617af7d62397a7dfaa].
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

## q15 (answerable) — status: answered
Q: In the eess.SY papers, what is combined with adaptive model predictive control to obtain exponential convergence of nonlinear systems despite bounded noise?
EXPECTED: A recursive least squares identifier with forgetting factor.
GOLD: 2004.01625v2 p1: "With the new approach we demonstrate exponential convergence of nonlinear systems under the influence of the adaptive model predictive control combined with a r"
AGENT: In the eess.SY papers, adaptive model predictive control is combined with a recursive least squares identifier with forgetting factor to obtain exponential convergence of nonlinear systems despite bounded noise [37b7e41105248297da3b, 9091a8c0eb5e652e2ce2].
- [37b7e41105248297da3b] [CONTAINS GOLD EVIDENCE]: Forward-looking persistent excitation in model predictive

control

Sven Brüggemann a Robert R. Bitmead a

aMechanical & Aerospace Engineering Department, University of California, San Diego, CA 92093-0411, USA, (e-mails:

{sbruegge, rbitmead}@eng.ucsd.edu)

A
- [9091a8c0eb5e652e2ce2]: 7.1
Convergence under bounded noise

The following theorem states that under sufficient conditions, if the disturbance is bounded and the initial state
and the initial parameter estimate are within a neighborhood of the periodic PE reference trajectory and the

## u01 (UNANSWERABLE) — status: abstain
Q: Which theorem in the corpus establishes a polynomial-time algorithm for computing the optimal policy in partially observable MDPs?
VERIFY (unanswerable): Scan over pages.jsonl: 'polynomial-time algorithm' 0 pages; 'polynomial in' appears only as a statistical-complexity statement in 2511.10383v2, not a POMDP policy theorem. 'partially observable' occur
AGENT: Không đủ bằng chứng để trả lời.

## u02 (UNANSWERABLE) — status: abstain
Q: What is the exact numerical Lipschitz constant that the papers derive for the contraction mapping of the Q-learning operator?
VERIFY (unanswerable): Scan over pages.jsonl: 'Lipschitz constant' only in 2511.10383v2 pp.14-16 (symbol L, no numerical value); 'contraction' 1 page (2511.10383v2 p15, HJB-level estimate, not Q-learning); no paper derives 
AGENT: Không đủ bằng chứng để trả lời.
