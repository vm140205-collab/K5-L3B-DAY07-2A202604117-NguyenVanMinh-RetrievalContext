# Review draft

## q16 (answerable) — status: answered
Q: Which two meta-algorithms are proposed to obtain zero-shot generalization in offline reinforcement learning?
EXPECTED: Pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO).
GOLD: 2503.07988v1 p1: "We propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to g"
AGENT: The two meta-algorithms proposed are pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO) [171cf669fe6e1890ca0b, ecba1f4c9f0ddf8d8e70].
- [171cf669fe6e1890ca0b] [CONTAINS GOLD EVIDENCE]: Provable Zero-Shot Generalization in Offline Reinforcement

Learning

Zhiyong Wang ∗Chen Yang † John C.S. Lui ‡ Dongruo Zhou §

Abstract

In this work, we study offline reinforcement learning (RL) with zero-shot generalization
property (ZSG), where the agent h
- [ecba1f4c9f0ddf8d8e70]: 7
Conclusion and Future Work

In this work, we study the zero-shot generalization (ZSG) performance of offline reinforcement
learning (RL). We propose two offline RL frameworks, pessimistic empirical risk minimization and
pessimistic proximal policy optimizati

## q17 (answerable) — status: answered
Q: What does the acronym UCRL-M expand to?
EXPECTED: Upper Confidence Reinforcement Learning with several Modules.
GOLD: 2308.02391v1 p12: "Algorithm UCRL-M (Upper Confidence Reinforcement Learning with several Modules) is given in Algorithm 1."
AGENT: The acronym UCRL-M expands to **Upper Confidence Reinforcement Learning with several Modules** [4f41f102f0d1c50cfe6a].
- [4f41f102f0d1c50cfe6a] [CONTAINS GOLD EVIDENCE]: 4.3 UCRL-M: learning with τmix modules

Algorithm UCRL-M (Upper Confidence Reinforcement Learning with several Modules)
is given in Algorithm 1. First, the algorithm initializes the different modules. Here, for
each episode k and module m, it computes the empi

## q18 (answerable) — status: answered
Q: Why does SORL incorporate shortcut models into the training process?
EXPECTED: To add self-consistency so the policy can generate high quality samples under any inference budget.
GOLD: 2505.22866v1 p2: "Our key insight is to leverage shortcut models [Frans et al., 2024], a novel class of generative models, in order to incorporate self-consistency into the train"
AGENT: SORL incorporates shortcut models into the training process to regularize its policy to the behavior of the offline data, as proven through a novel theoretical analysis of shortcut models [23f02f5ff2b9eb4082f9]. This regularization is a key property enabling SORL's self-consistency and expressive inference under any compute budget [a5d8c9997ceec909b929]. The implementation details further highlight that training the shortcut model is a major change introduced in SORL compared to baseline methods [def7e63b8f703f1715b0].
- [23f02f5ff2b9eb4082f9]: 1. We introduce SORL, an efficient, one-stage training procedure for expressive policies that
can perform inference under any compute budget, including one-step inference. Despite
its efficiency, SORL’s policy is still able to capture complex, multi-modal data
- [a5d8c9997ceec909b929]: 7
Discussion

We introduce SORL: a simple, efficient one-stage training procedure for expressive policies in offline
RL. SORL’s key property is self-consistency, which enables expressive inference under any inference
budget, including one-step. Theoretically, 
- [def7e63b8f703f1715b0]: E.2
SORL Implementation Details

One of the strengths of SORL is its implementation simplicity. In order to implement SORL, we adapt
Park et al. [2025]’s open-source implementations of various offline RL algorithms (FQL, IFQL, IQL,
ReBRAC), which are adapted f

## q19 (answerable) — status: answered
Q: Among the 2025 papers, what does Sparse-Reg regularize when learning from small datasets?
EXPECTED: Model complexity, via sparse regularization.
GOLD: 2506.17155v2 p3: "We propose using sparse regularization to regularize model complexity when learning from small datasets."
AGENT: Sparse-Reg regularizes the sparsity of the learned policy or value function when learning from small datasets in offline reinforcement learning [cf12cac5882d85a30193, 7678c005ed27f50c1f11, 5f1560878c6e4159f091].
- [5f1560878c6e4159f091]: We take a batch of data from the offline training dataset D, calculate the gradient through forward
and backward propagation, and then use Equation (1) to generate masks for the neural networks.
Periodic update of sparsity is found to be more effective for RL 
- [7678c005ed27f50c1f11]: 1
Introduction

Reinforcement Learning (RL) is a powerful approach to solving complex problems, but its application
can be challenging due to the need for active interaction with the environment. In many scenarios,
collecting training data can be challenging o
- [cf12cac5882d85a30193]: arXiv:2506.17155v2 [cs.LG] 26 Jun 2025

Sparse-Reg: Improving Sample Complexity in Offline
Reinforcement Learning using Sparsity

Samin Yeasar Arnob1,2, Scott Fujimoto3, Doina Precup1,2

samin.arnob@mail.mcgill.ca

1Department of Computing Science, McGill Univ

## q20 (answerable) — status: answered
Q: Which structural condition on the latent dynamics is identified as enabling sample efficiency?
EXPECTED: Pushforward coverability.
GOLD: 2410.17904v1 p2: "We complement these negative findings with a positive result, identifying pushforward coverability as a general structural condition on the latent dynamics that"
AGENT: The structural condition identified as enabling sample efficiency is pushforward coverability [5ee52cd69d1a772343ec][2ddbe92d844603bb704b].
- [2ddbe92d844603bb704b] [CONTAINS GOLD EVIDENCE]: If a base MDP class is tractable when observed directly, is the corresponding latent-dynamics problem

tractable?

Statistical modularity adopts a minimax perspective by assuming that the base MDP lies in a given class, and
demands that the sample complexity o
- [5ee52cd69d1a772343ec]: This paper addresses the question of reinforcement learning under general latent dynamics from a
statistical and algorithmic perspective. On the statistical side, our main negative result shows that
most well-studied settings for reinforcement learning with fu

## u03 (UNANSWERABLE) — status: abstain
Q: Which GPU model and how many GPUs were used to train the models of the autonomous driving offline RL benchmark?
VERIFY (unanswerable): Scan over pages.jsonl: 'GPU'/'RTX' occur only in 2410.14069v1, 2505.22866v1, 2303.13117v1 - not in the AD4RL paper (2404.02429v1); 'A100'/'V100' 0 pages. AD4RL lists datasets and algorithms but states
AGENT: Không đủ bằng chứng để trả lời.

## u04 (UNANSWERABLE) — status: abstain
Q: On which real quadruped robot hardware was the tube-based stochastic MPC controller validated in experiments?
VERIFY (unanswerable): Scan over pages.jsonl: 'quadruped' only in 2505.22866v1 p29 (antmaze simulated tasks, not real hardware); 'ANYmal'/'Spot'/'robot dog' 0 pages. The tube-based stochastic MPC paper (2104.10383v1) is the
AGENT: Không đủ bằng chứng để trả lời.
