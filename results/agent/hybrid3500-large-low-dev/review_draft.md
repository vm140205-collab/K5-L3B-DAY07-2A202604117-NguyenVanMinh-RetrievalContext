# Review draft

## q01 (answerable) — status: answered
Q: What does the paper propose instead of looking backwards and preserving prior regressor data?
EXPECTED: A procedure for the offline generation of a persistently exciting reference trajectory that perturbs the equilibrium.
GOLD: 2004.01625v2 p1: "Instead, we present a procedure for the offline generation of a persistently exciting reference trajectory perturbing the equilibrium."
AGENT: Instead of looking backwards and preserving prior regressor data, the paper proposes a procedure for the offline generation of a persistently exciting reference trajectory perturbing the equilibrium [37b7e41105248297da3b].
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
AGENT: The probabilistically resolvable time-varying tube-based stochastic model predictive control algorithm (pTTSMPC) is designed by employing the time-varying probabilistic reachable sets as the tubes [73d0d617dbbd09f4f8c4][7d19a06f03d13e433fbe].
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
AGENT: The autonomous driving benchmark provides 19 datasets (including real-world human driver datasets) and seven popular offline reinforcement learning algorithms [c099dfc8190fd395b1e5].
- [c099dfc8190fd395b1e5] [CONTAINS GOLD EVIDENCE]: AD4RL: Autonomous Driving Benchmarks for
Offline Reinforcement Learning with Value-based Dataset

Dongsu Lee†, Chanin Eom†, and Minhae Kwon†,∗

Abstract— Offline reinforcement learning has emerged as a
promising technology by enhancing its practicality through

## q04 (answerable) — status: answered
Q: How does the paper reframe offline RL so that the best behaviours can be stitched together from sub-optimal experts?
EXPECTED: It reformulates offline RL as an optimal transportation problem and learns a policy mapping states to a partial distribution of the best expert actions.
GOLD: 2410.14069v1 p1: "we rethink offline reinforcement learning as an optimal transportation problem."
AGENT: The paper reframes offline RL by viewing the entire problem as an optimal transport (OT) problem rather than as behavior cloning [6d748129f3dd2a58c361]. Instead of cloning the behavior policy—which limits improvement when the dataset contains sub-optimal or incorrect expert demonstrations—the approach aims to stitch the best trajectories by selecting the best action for each state and recombining different trajectories from multiple experts [6d748129f3dd2a58c361]. Specifically, it formulates the action-value function and the policy as components of an OT problem between states and actions, and uses partial optimal transport to map each state to a partial distribution of the best expert actions, effectively ignoring sub-optimal actions [fb6011bde1dfcf5ef473][3b617af7d62397a7dfaa][cff6e77be15ba4f350a8].
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
AGENT: The main problem faced by all current offline model-based reinforcement learning methods is **distributional shift** (specifically, distributional shifts in both state and action distributions) [c6a0bc25e4dd91330b99]. This is described as the most influential problem in the field, where the model is derived from data collected by another policy with a distributional shift relative to the deployment environment, and no exploration is available to rectify the model [11370be916e3beb0055a][1dda3e750f9589ffb178].
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

## q06 (answerable) — status: answered
Q: How does the regret of the admission control algorithm scale with the maximal number of jobs in the network?
EXPECTED: Sub-linearly in the maximal number of jobs S.
GOLD: 2308.02391v1 p1: "a regret that only depends sub-linearly on the maximal number of jobs in the network, S."
AGENT: The regret scales sub-linearly with the maximal number of jobs in the network, S. Specifically, the algorithm achieves a regret bound of Reg(T) ≤ ̃O(√ST) [f696acabb4fc32ee8aee], meaning the dependence on S is √S (the square root of S) [36412c830e6b326a10b5].
- [36412c830e6b326a10b5] [CONTAINS GOLD EVIDENCE]: a regret that only depends sub-linearly on the maximal number of jobs in the
network, S. In particular, in contrast with existing regret analyses, our regret
bound does not depend on the diameter of the underlying Markov Decision
Process (MDP), which in most q
- [f696acabb4fc32ee8aee]: 1.2 Contribution and methodology

In this paper, we propose a learning algorithm for the optimal job-admission policy
in a partially observable queueing network with regret Reg(T) ≤ ̃O(

√

ST). Thus, our
main contribution is a learning algorithm with a regret

## q07 (answerable) — status: answered
Q: What does the DPE algorithm blend into a unified framework?
EXPECTED: Offline sequence modeling and offline reinforcement learning, with Double Policy Estimation.
GOLD: 2308.14897v1 p1: "we propose DPE: an RL algorithm that blends offline sequence modeling and offline reinforcement learning with Double Policy Estimation (DPE) in a unified framew"
AGENT: DPE blends offline sequence modeling and offline reinforcement learning with Double Policy Estimation (DPE) in a unified framework [47d2a15a8ecae90cd43d].
- [47d2a15a8ecae90cd43d] [CONTAINS GOLD EVIDENCE]: Offline reinforcement learning aims to utilize datasets of previously gathered
environment-action interaction records to learn a policy without access to the
real environment. Recent work has shown that offline reinforcement learning
can be formulated as a seq

## q08 (answerable) — status: answered
Q: How is the classical reinforcement learning formulation made robust without changing the algorithm class?
EXPECTED: By adding standard deviation penalization of the objective, giving a risk-averse formulation.
GOLD: 2206.06841v1 p1: "We show that the classical Reinforcement Learning formulation can be robustified using standard deviation penalization of the objective."
AGENT: The classical Reinforcement Learning formulation is made robust by using standard deviation penalization of the objective, which approximates the Robust RL formulation constrained with a Φ-divergence into a Risk-averse mean-standard deviation optimization, while keeping the same algorithm class (Distributional Reinforcement Learning) [7d126688a9e61a223e64][4830cc6970b8e873c143].
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
AGENT: Sparse-Reg uses a regularization technique based on **sparsity** in the parameter space of neural networks to mitigate overfitting on small offline datasets [cf12cac5882d85a30193]. Specifically, it induces sparsity in the neural network to reduce the complexity of the parameter space, drawing from techniques developed for pruning neural networks [c65459a5bd66b7805d37]. This targeted regularization of the parameter space through sparsity proves more effective for learning with limited data compared to other regularization methods [92e87828ff6d3545b81c].
- [92e87828ff6d3545b81c]: 6
Discussion

We explore the use of small datasets within the realm of offline RL for continuous control tasks.
While many standard offline RL benchmarks involve datasets containing well over a million data
points, it is important to recognize that numerous ap
- [c65459a5bd66b7805d37]: Offline RL algorithms fail with small datasets: Prior work in offline RL exhibits overfitting (Agarwal et al., 2019; Kumar et al., 2021; Arnob et al., 2021a), i.e., their performance starts to deteriorate
after a certain number of gradient updates and this iss
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
AGENT: SORL leverages **shortcut models**, which are described as a novel class of generative models, to scale both training and inference [b0e12c3edb7c000680c6][e2634a4e45cbb2808075].
- [b0e12c3edb7c000680c6] [CONTAINS GOLD EVIDENCE]: Diffusion and flow models have emerged as powerful generative approaches capable of modeling diverse and multimodal behavior. However, applying these models
to offline reinforcement learning (RL) remains challenging due to the iterative
nature of their noise s
- [e2634a4e45cbb2808075]: In this paper, we tackle the question of how to achieve efficient training, while maintaining expressivity, and scale with greater inference-time compute. We introduce Scalable Offline Reinforcement
Learning (SORL): a simple, efficient one-stage training proce

## q12 (answerable) — status: answered
Q: In which space is the infinitesimal generator of controlled diffusion processes learned?
EXPECTED: In a reproducing kernel Hilbert space.
GOLD: 2511.10383v2 p1: "we represent our world model in terms of the infinitesimal generator of controlled diffusion processes learned in a reproducing kernel Hilbert space."
AGENT: The infinitesimal generator of controlled diffusion processes is learned in a reproducing kernel Hilbert space (RKHS) [d7c6c4009ef1689927f1]. The paper restricts the approximating value function and policy to reproducing kernel Hilbert spaces for computational tractability, while the generator itself is approximated as an operator into L2_η with domain D(G) having sufficient Sobolev regularity [c12b084a32033d12c119]; the nonparametric kernel formulation approximates quantities in a sample-induced subspace of an RKHS [2cc7138443b9d32e443d].
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
AGENT: According to the paper's main negative result, most well-studied settings for reinforcement learning with function approximation become intractable when composed with rich observations [5ee52cd69d1a772343ec].
- [5ee52cd69d1a772343ec] [CONTAINS GOLD EVIDENCE]: This paper addresses the question of reinforcement learning under general latent dynamics from a
statistical and algorithmic perspective. On the statistical side, our main negative result shows that
most well-studied settings for reinforcement learning with fu

## q14 (answerable) — status: answered
Q: In the 2024 paper that reformulates offline RL with optimal transport, on which benchmark suite is the algorithm evaluated?
EXPECTED: The D4RL suite (continuous control problems).
GOLD: 2410.14069v1 p1: "We evaluate the performance of our algorithm on continuous control problems from the D4RL suite and demonstrate improvements over existing methods."
AGENT: The algorithm is evaluated on the D4RL benchmark suite (specifically on continuous control problems from the D4RL suite) [3b617af7d62397a7dfaa][7379339c6a4febb68224].
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
- [7379339c6a4febb68224]: between state and actions distribution (M3). By utilizing the Q-function as a transport cost and the
policy as an optimal transport map, we formalize offline reinforcement learning as a Maximin OT
optimization problem. This opens doors for applying recent adva

## q15 (answerable) — status: answered
Q: In the eess.SY papers, what is combined with adaptive model predictive control to obtain exponential convergence of nonlinear systems despite bounded noise?
EXPECTED: A recursive least squares identifier with forgetting factor.
GOLD: 2004.01625v2 p1: "With the new approach we demonstrate exponential convergence of nonlinear systems under the influence of the adaptive model predictive control combined with a r"
AGENT: A recursive least squares identifier with forgetting factor is combined with adaptive model predictive control to obtain exponential convergence of nonlinear systems despite bounded noise [37b7e41105248297da3b].
- [37b7e41105248297da3b] [CONTAINS GOLD EVIDENCE]: Forward-looking persistent excitation in model predictive

control

Sven Brüggemann a Robert R. Bitmead a

aMechanical & Aerospace Engineering Department, University of California, San Diego, CA 92093-0411, USA, (e-mails:

{sbruegge, rbitmead}@eng.ucsd.edu)

A

## u01 (UNANSWERABLE) — status: abstain
Q: Which theorem in the corpus establishes a polynomial-time algorithm for computing the optimal policy in partially observable MDPs?
VERIFY (unanswerable): Scan over pages.jsonl: 'polynomial-time algorithm' 0 pages; 'polynomial in' appears only as a statistical-complexity statement in 2511.10383v2, not a POMDP policy theorem. 'partially observable' occur
AGENT: Không đủ bằng chứng để trả lời.

## u02 (UNANSWERABLE) — status: abstain
Q: What is the exact numerical Lipschitz constant that the papers derive for the contraction mapping of the Q-learning operator?
VERIFY (unanswerable): Scan over pages.jsonl: 'Lipschitz constant' only in 2511.10383v2 pp.14-16 (symbol L, no numerical value); 'contraction' 1 page (2511.10383v2 p15, HJB-level estimate, not Q-learning); no paper derives 
AGENT: Không đủ bằng chứng để trả lời.
