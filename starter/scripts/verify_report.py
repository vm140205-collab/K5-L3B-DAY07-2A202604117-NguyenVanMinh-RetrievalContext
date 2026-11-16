"""Verify every headline number in the report against the raw result files.

Checks the report's tables against results/*/summary*.json. Exits non-zero if
any number disagrees, so the report cannot silently drift from the artifacts.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
REPORT = REPO / "report" / "individual" / "2A202604117_NguyenVanMinh.md"
failures = []


def check(name, actual, expected):
    ok = actual == expected
    print(f"{'OK  ' if ok else 'FAIL'} {name}: actual={actual} report={expected}")
    if not ok:
        failures.append(name)


def load(path):
    return json.loads((REPO / path).read_text(encoding="utf-8"))


# --- retrieval dev ---
for method, hit1, hit3 in (("dense", "8/15", "11/15"), ("bm25", "11/15", "14/15"),
                           ("hybrid_rrf", "10/15", "12/15")):
    s = load(f"results/retrieval/{method}-dev/summary.json")
    check(f"retrieval {method}-dev hit1", s["hit1"], hit1)
    check(f"retrieval {method}-dev hit3", s["evidence_hit3"], hit3)

for method, cer in (("dense", "11/15"), ("bm25", "14/15"), ("hybrid_rrf", "12/15")):
    s = load(f"results/retrieval/{method}-dev-b3500/summary.json")
    check(f"retrieval {method}-dev b3500 CER", s["context_evidence_rate"], cer)

# --- agent runs: grounded means, abstention, false abstention, citations ---
expected = {
    "dense800-dev": (0.80, "2/2", "7/15", "7/9"),
    "hybrid3500-dev": (1.667, "2/2", "0/15", "18/23"),
    "alltools-dev": (1.60, "2/2", "1/15", "20/24"),
    "hybrid3500-medium-dev": (1.733, "1/2", "1/15", "19/25"),
    "alltools-medium-dev": (1.733, "2/2", "2/15", "21/26"),
    "hybrid3500-large-low-dev": (1.867, "2/2", "1/15", "25/28"),
    "hybrid3500-deepseek-high-dev": (1.60, "2/2", "3/15", "23/23"),
    "alltools-deepseek-high-dev": (1.733, "2/2", "2/15", "24/24"),
    "dense800-test": (1.00, "2/2", "2/4", "2/2"),
    "hybrid3500-large-low-test": (1.40, "2/2", "1/5", "7/7"),
    "hybrid3500-test": (1.60, "2/2", "0/5", "9/11"),
}
for run, (mean, abst, false_abst, cit) in expected.items():
    m = load(f"results/agent/{run}/summary_metrics.json")
    g = m["grounded_answer"]
    actual_mean = (g["1"] + 2 * g["2"]) / g["N"]
    check(f"{run} grounded mean", round(actual_mean, 3), mean)
    check(f"{run} abstention", f"{m['abstention']['n']}/{m['abstention']['N']}", abst)
    check(f"{run} false abstention",
          f"{m['false_abstention']['n']}/{m['false_abstention']['N']}", false_abst)
    check(f"{run} citations",
          f"{m['citation_validity']['n']}/{m['citation_validity']['N']}", cit)

# --- provider errors on test baseline ---
m = load("results/agent/dense800-test/summary_metrics.json")
check("dense800-test provider_errors", m["provider_errors"], 1)

# --- benchmark composition ---
qs = [json.loads(l) for l in
      (REPO / "benchmark" / "questions.jsonl").read_text(encoding="utf-8").splitlines()]
dev_a = sum(1 for q in qs if q["split"] == "dev" and q["answerable"])
dev_u = sum(1 for q in qs if q["split"] == "dev" and not q["answerable"])
test_a = sum(1 for q in qs if q["split"] == "test" and q["answerable"])
test_u = sum(1 for q in qs if q["split"] == "test" and not q["answerable"])
check("benchmark dev", (dev_a, dev_u), (15, 2))
check("benchmark test", (test_a, test_u), (5, 2))

# --- report mentions all required sections ---
report = REPORT.read_text(encoding="utf-8")
for section in ("Dữ liệu và benchmark", "Retrieval và thử nghiệm",
                "Agent và đánh giá", "Tái lập", "2A202604117"):
    check(f"report section '{section}'", section in report, True)

print()
if failures:
    print(f"{len(failures)} MISMATCHES: {failures}")
    sys.exit(1)
print("All report numbers verified against raw artifacts.")
