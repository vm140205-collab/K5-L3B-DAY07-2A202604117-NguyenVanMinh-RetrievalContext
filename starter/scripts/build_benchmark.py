"""Build the Day 7 benchmark from the Day 6 question set + new unanswerable questions.

Schema (Day 7 contract):
- answerable:   id, split, question, expected_answer, answerable=true,
                gold: [{source_id, page, evidence}]   (from Day 6 gold fields)
- unanswerable: id, split, question, answerable=false, verification
                (how the absence of evidence was checked in this corpus)

Every gold evidence must be a substring of one strategy-C chunk with matching
source/page (same rule as the starter baseline `hit`), validated below.
Unanswerable questions are NOT counted in retrieval metric denominators.
"""
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from store import Day6Store  # noqa: E402

DAY6_QUESTIONS = REPO_ROOT / "day6" / "questions_day6.jsonl"
OUTPUT = REPO_ROOT / "benchmark" / "questions.jsonl"

# Unanswerable questions: near the corpus topics (RL / MPC / offline RL) but with
# no supporting evidence in the 14 documents. `verification` records the check:
# keyword scan over all 264 pages (data/pages.jsonl) + dense/BM25 top-10 review.
UNANSWERABLE = [
    {
        "id": "u01", "split": "dev", "answerable": False,
        "question": "Which theorem in the corpus establishes a polynomial-time algorithm for computing the optimal policy in partially observable MDPs?",
        "verification": "Scan over pages.jsonl: 'polynomial-time algorithm' 0 pages; 'polynomial in' appears only as a statistical-complexity statement in 2511.10383v2, not a POMDP policy theorem. 'partially observable' occurs only in 2308.02391v1 (queueing networks, regret bounds, no such theorem). Dense/BM25 top-10 reviewed: no chunk states this theorem.",
    },
    {
        "id": "u02", "split": "dev", "answerable": False,
        "question": "What is the exact numerical Lipschitz constant that the papers derive for the contraction mapping of the Q-learning operator?",
        "verification": "Scan over pages.jsonl: 'Lipschitz constant' only in 2511.10383v2 pp.14-16 (symbol L, no numerical value); 'contraction' 1 page (2511.10383v2 p15, HJB-level estimate, not Q-learning); no paper derives a numerical contraction constant for a Q-learning operator.",
    },
    {
        "id": "u03", "split": "test", "answerable": False,
        "question": "Which GPU model and how many GPUs were used to train the models of the autonomous driving offline RL benchmark?",
        "verification": "Scan over pages.jsonl: 'GPU'/'RTX' occur only in 2410.14069v1, 2505.22866v1, 2303.13117v1 - not in the AD4RL paper (2404.02429v1); 'A100'/'V100' 0 pages. AD4RL lists datasets and algorithms but states no training hardware.",
    },
    {
        "id": "u04", "split": "test", "answerable": False,
        "question": "On which real quadruped robot hardware was the tube-based stochastic MPC controller validated in experiments?",
        "verification": "Scan over pages.jsonl: 'quadruped' only in 2505.22866v1 p29 (antmaze simulated tasks, not real hardware); 'ANYmal'/'Spot'/'robot dog' 0 pages. The tube-based stochastic MPC paper (2104.10383v1) is theoretical with no hardware experiments.",
    },
]


def squash(text: str) -> str:
    """Whitespace-insensitive form used for evidence matching (same rule as Day 6)."""
    return re.sub(r"\s+", " ", text).strip().lower()


# Day 6 q06's original quote spans a paragraph boundary under strategy-C
# chunking (head in the intro chunk, tail in the abstract chunk). The abstract
# chunk alone supports the answer, so the evidence is narrowed to that span
# (alternative valid evidence on the same gold page, recorded per BENCHMARK.md).
EVIDENCE_OVERRIDES = {
    "q06": "a regret that only depends sub-linearly on the maximal number of jobs in the network, S.",
}


def convert_day6(q: dict) -> dict:
    pages = q.get("gold_pages") or [q.get("gold_page")]
    evidence = EVIDENCE_OVERRIDES.get(q["id"], q["evidence_quote"])
    gold = [{"source_id": q["gold_source_id"], "page": p, "evidence": evidence}
            for p in pages]
    out = {
        "id": q["id"], "split": q["split"], "question": q["question"],
        "expected_answer": q["expected_answer"], "answerable": True, "gold": gold,
    }
    if q.get("filter"):
        out["filter"] = q["filter"]
    if q.get("notes"):
        out["notes"] = q["notes"]
    return out


def main() -> None:
    store = Day6Store()
    chunks = store.scroll_chunks()
    by_key: dict[tuple[str, int], list[str]] = {}
    for c in chunks:
        by_key.setdefault((c["document_id"], c["page"]), []).append(c["text"])

    questions = []
    for line in DAY6_QUESTIONS.read_text(encoding="utf-8").splitlines():
        q = convert_day6(json.loads(line))
        for g in q["gold"]:
            texts = by_key.get((g["source_id"], g["page"]), [])
            if not any(squash(g["evidence"]) in squash(t) for t in texts):
                raise SystemExit(f"{q['id']}: evidence not found in strategy-C chunk "
                                 f"({g['source_id']} p{g['page']})")
        questions.append(q)
    questions.extend(UNANSWERABLE)

    dev_a = sum(1 for q in questions if q["split"] == "dev" and q["answerable"])
    dev_u = sum(1 for q in questions if q["split"] == "dev" and not q["answerable"])
    test_a = sum(1 for q in questions if q["split"] == "test" and q["answerable"])
    test_u = sum(1 for q in questions if q["split"] == "test" and not q["answerable"])
    assert (dev_a, dev_u, test_a, test_u) == (15, 2, 5, 2), (dev_a, dev_u, test_a, test_u)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        for q in questions:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print(f"wrote {len(questions)} questions -> {OUTPUT}")
    print(f"dev: {dev_a} answerable + {dev_u} unanswerable; "
          f"test: {test_a} answerable + {test_u} unanswerable")


if __name__ == "__main__":
    main()
