# Review draft

## q16 (answerable) — status: answered
Q: Which two meta-algorithms are proposed to obtain zero-shot generalization in offline reinforcement learning?
EXPECTED: Pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO).
GOLD: 2503.07988v1 p1: "We propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to g"
AGENT: The two meta-algorithms proposed are pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO) [171cf669fe6e1890ca0b].
- [171cf669fe6e1890ca0b] [CONTAINS GOLD EVIDENCE]: Provable Zero-Shot Generalization in Offline Reinforcement

Learning

Zhiyong Wang ∗Chen Yang † John C.S. Lui ‡ Dongruo Zhou §

Abstract

In this work, we study offline reinforcement learning (RL) with zero-shot generalization
property (ZSG), where the agent h

## q17 (answerable) — status: answered
Q: What does the acronym UCRL-M expand to?
EXPECTED: Upper Confidence Reinforcement Learning with several Modules.
GOLD: 2308.02391v1 p12: "Algorithm UCRL-M (Upper Confidence Reinforcement Learning with several Modules) is given in Algorithm 1."
AGENT: The acronym UCRL-M expands to **Upper Confidence Reinforcement Learning with several Modules** [4f41f102f0d1c50cfe6a].
- [4f41f102f0d1c50cfe6a] [CONTAINS GOLD EVIDENCE]: 4.3 UCRL-M: learning with τmix modules

Algorithm UCRL-M (Upper Confidence Reinforcement Learning with several Modules)
is given in Algorithm 1. First, the algorithm initializes the different modules. Here, for
each episode k and module m, it computes the empi

## q18 (answerable) — status: abstain
Q: Why does SORL incorporate shortcut models into the training process?
EXPECTED: To add self-consistency so the policy can generate high quality samples under any inference budget.
GOLD: 2505.22866v1 p2: "Our key insight is to leverage shortcut models [Frans et al., 2024], a novel class of generative models, in order to incorporate self-consistency into the train"
AGENT: Không đủ bằng chứng để trả lời.

## q19 (answerable) — status: error
Q: Among the 2025 papers, what does Sparse-Reg regularize when learning from small datasets?
EXPECTED: Model complexity, via sparse regularization.
GOLD: 2506.17155v2 p3: "We propose using sparse regularization to regularize model complexity when learning from small datasets."
AGENT: 
ERROR: ConnectTimeout: HTTPSConnectionPool(host='api.mistral.ai', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by ConnectTimeoutError(<HTTPSConnection(host='api.mistral.ai', port=44

## q20 (answerable) — status: abstain
Q: Which structural condition on the latent dynamics is identified as enabling sample efficiency?
EXPECTED: Pushforward coverability.
GOLD: 2410.17904v1 p2: "We complement these negative findings with a positive result, identifying pushforward coverability as a general structural condition on the latent dynamics that"
AGENT: Không đủ bằng chứng để trả lời.

## u03 (UNANSWERABLE) — status: abstain
Q: Which GPU model and how many GPUs were used to train the models of the autonomous driving offline RL benchmark?
VERIFY (unanswerable): Scan over pages.jsonl: 'GPU'/'RTX' occur only in 2410.14069v1, 2505.22866v1, 2303.13117v1 - not in the AD4RL paper (2404.02429v1); 'A100'/'V100' 0 pages. AD4RL lists datasets and algorithms but states
AGENT: Không đủ bằng chứng để trả lời.

## u04 (UNANSWERABLE) — status: abstain
Q: On which real quadruped robot hardware was the tube-based stochastic MPC controller validated in experiments?
VERIFY (unanswerable): Scan over pages.jsonl: 'quadruped' only in 2505.22866v1 p29 (antmaze simulated tasks, not real hardware); 'ANYmal'/'Spot'/'robot dog' 0 pages. The tube-based stochastic MPC paper (2104.10383v1) is the
AGENT: Không đủ bằng chứng để trả lời.
