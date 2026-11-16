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
AGENT: The probabilistically resolvable time-varying tube-based stochastic model predictive control algorithm [73d0d617dbbd09f4f8c4].
- [73d0d617dbbd09f4f8c4] [CONTAINS GOLD EVIDENCE]: Abstract—This paper presents two stochastic model predictive
control methods for linear time-invariant systems subject to
unbounded additive uncertainties. The new methods are developed by formulating the chance constraints into deterministic
form, which are t

## q03 (answerable) — status: abstain
Q: How many datasets and how many offline reinforcement learning algorithms does the autonomous driving benchmark provide?
EXPECTED: 19 datasets, including real-world human driver datasets, and seven offline RL algorithms in three driving scenarios.
GOLD: 2404.02429v1 p1: "We provide 19 datasets, including realworld human driver’s datasets, and seven popular offline reinforcement learning algorithms in three realistic driving scen"
AGENT: Không đủ bằng chứng để trả lời.

## q04 (answerable) — status: answered
Q: How does the paper reframe offline RL so that the best behaviours can be stitched together from sub-optimal experts?
EXPECTED: It reformulates offline RL as an optimal transportation problem and learns a policy mapping states to a partial distribution of the best expert actions.
GOLD: 2410.14069v1 p1: "we rethink offline reinforcement learning as an optimal transportation problem."
AGENT: The paper reframes offline RL as an optimal transport (OT) problem between states and actions, using the action-value function and policy as components of the OT formulation [fb6011bde1dfcf5ef473]. Within this OT framework, the method applies partial optimal transport to select and stitch together the best expert actions for each given state, even when the dataset contains noisy or sub-optimal behaviors [fb6011bde1dfcf5ef473].
- [fb6011bde1dfcf5ef473]: In this paper, we have established the novel algorithm for offline reinforcement learning. Our work
introduces the concept using the action-value function and the policy as components of the OT
problem between states and actions. To demonstrate the potential o

## q05 (answerable) — status: abstain
Q: What is described as the main problem faced by all current offline model-based reinforcement learning methods?
EXPECTED: Distributional shift.
GOLD: 2305.03360v1 p1: "particularly their approaches in solving the issue of distributional shift, the main problem faced by all current offline model-based reinforcement learning met"
AGENT: Không đủ bằng chứng để trả lời.

## q06 (answerable) — status: answered
Q: How does the regret of the admission control algorithm scale with the maximal number of jobs in the network?
EXPECTED: Sub-linearly in the maximal number of jobs S.
GOLD: 2308.02391v1 p1: "a regret that only depends sub-linearly on the maximal number of jobs in the network, S."
AGENT: The regret of the admission control algorithm scales sub-linearly with the maximal number of jobs in the network, denoted S, as indicated by the regret bound Reg(T) ≤ ̃O(√S T) [f696acabb4fc32ee8aee]. This is explicitly stated to be a key contribution, where the regret depends only sub-linearly on S and does not depend on the diameter of the underlying MDP [36412c830e6b326a10b5].
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

## q07 (answerable) — status: abstain
Q: What does the DPE algorithm blend into a unified framework?
EXPECTED: Offline sequence modeling and offline reinforcement learning, with Double Policy Estimation.
GOLD: 2308.14897v1 p1: "we propose DPE: an RL algorithm that blends offline sequence modeling and offline reinforcement learning with Double Policy Estimation (DPE) in a unified framew"
AGENT: Không đủ bằng chứng để trả lời.

## q08 (answerable) — status: answered
Q: How is the classical reinforcement learning formulation made robust without changing the algorithm class?
EXPECTED: By adding standard deviation penalization of the objective, giving a risk-averse formulation.
GOLD: 2206.06841v1 p1: "We show that the classical Reinforcement Learning formulation can be robustified using standard deviation penalization of the objective."
AGENT: The classical reinforcement learning formulation is made robust without changing the algorithm class by incorporating a standard deviation penalization into the objective function. This approach approximates a robust reinforcement learning formulation constrained with a Φ-divergence using an approximate risk-averse formulation [7d126688a9e61a223e64].
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

## q10 (answerable) — status: abstain
Q: What kind of regularization does Sparse-Reg use to mitigate overfitting on small offline datasets?
EXPECTED: A sparsity-based regularization technique that regularizes model complexity.
GOLD: 2506.17155v2 p1: "we introduce "Sparse-Reg": a regularization technique based on sparsity to mitigate overfitting in offline reinforcement learning, enabling effective learning i"
AGENT: Không đủ bằng chứng để trả lời.

## q11 (answerable) — status: answered
Q: What class of generative models does SORL leverage to scale both training and inference?
EXPECTED: Shortcut models.
GOLD: 2505.22866v1 p1: "we introduce Scalable Offline Reinforcement Learning (SORL), a new offline RL algorithm that leverages shortcut models—a novel class of generative models—to sca"
AGENT: SORL leverages diffusion models to scale both training and inference [23f02f5ff2b9eb4082f9].
- [23f02f5ff2b9eb4082f9]: 1. We introduce SORL, an efficient, one-stage training procedure for expressive policies that
can perform inference under any compute budget, including one-step inference. Despite
its efficiency, SORL’s policy is still able to capture complex, multi-modal data

## q12 (answerable) — status: answered
Q: In which space is the infinitesimal generator of controlled diffusion processes learned?
EXPECTED: In a reproducing kernel Hilbert space.
GOLD: 2511.10383v2 p1: "we represent our world model in terms of the infinitesimal generator of controlled diffusion processes learned in a reproducing kernel Hilbert space."
AGENT: The infinitesimal generator of controlled diffusion processes is learned in a space with sufficient Sobolev regularity, denoted D(G) [c12b084a32033d12c119].
- [c12b084a32033d12c119]: V. STATISTICAL LEARNING OF WORLD MODELS
To build an infinitesimal world model and solve the HJB
via a simple dynamic programming recursion (P3), we seek
a data-driven approximation of the infinitesimal generator
G : D(G) →L2

η, with D(G) a space with sufficie

## q13 (answerable) — status: answered
Q: According to the negative result, what happens to well-studied reinforcement learning settings with function approximation when they are composed with rich observations?
EXPECTED: They become intractable.
GOLD: 2410.17904v1 p1: "our main negative result shows that most well-studied settings for reinforcement learning with function approximation become intractable when composed with rich"
AGENT: According to the negative result, most well-studied reinforcement learning settings with function approximation become intractable when composed with rich observations [5ee52cd69d1a772343ec].
- [5ee52cd69d1a772343ec] [CONTAINS GOLD EVIDENCE]: This paper addresses the question of reinforcement learning under general latent dynamics from a
statistical and algorithmic perspective. On the statistical side, our main negative result shows that
most well-studied settings for reinforcement learning with fu

## q14 (answerable) — status: abstain
Q: In the 2024 paper that reformulates offline RL with optimal transport, on which benchmark suite is the algorithm evaluated?
EXPECTED: The D4RL suite (continuous control problems).
GOLD: 2410.14069v1 p1: "We evaluate the performance of our algorithm on continuous control problems from the D4RL suite and demonstrate improvements over existing methods."
AGENT: Không đủ bằng chứng để trả lời.

## q15 (answerable) — status: answered
Q: In the eess.SY papers, what is combined with adaptive model predictive control to obtain exponential convergence of nonlinear systems despite bounded noise?
EXPECTED: A recursive least squares identifier with forgetting factor.
GOLD: 2004.01625v2 p1: "With the new approach we demonstrate exponential convergence of nonlinear systems under the influence of the adaptive model predictive control combined with a r"
AGENT: Forward-looking persistent excitation is combined with adaptive model predictive control to obtain exponential convergence of nonlinear systems despite bounded noise [37b7e41105248297da3b].
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
