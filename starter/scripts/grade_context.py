"""Context grading 0/1/2 for test answerable questions (BENCHMARK.md section 2).

0 = no valid evidence in the final context sent to the model.
1 = evidence retrieved but cut out of the packed context (budget) or only
    partial (e.g. evidence chunk retrieved but source/page conditions missing).
2 = a chunk containing valid evidence (right source, right page, evidence
    substring) is inside the final packed context, with its source header.

The mechanical evidence check mirrors the retrieval `hit` rule; the source is
always part of the packed block header ([id | source | page]), so a hit inside
context_ids implies grade 2. Output is a table for human verification.
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--traces", required=True, type=Path)
    parser.add_argument("--run", required=True)
    args = parser.parse_args()

    questions = {q["id"]: q for q in (
        json.loads(l) for l in
        (REPO_ROOT / "benchmark" / "questions.jsonl").read_text(encoding="utf-8").splitlines())
        if q["split"] == "test" and q["answerable"]}

    rows = []
    for line in args.traces.read_text(encoding="utf-8").splitlines():
        t = json.loads(line)
        q = questions.get(t["query_id"])
        if not q:
            continue
        if t["status"] == "error":
            rows.append((t["query_id"], "error", "-", "provider error, no context"))
            continue
        chunk_text = {}
        for s in t.get("searches", []):
            for r in s["results"]:
                chunk_text[r["id"]] = r["text"]

        def evidence_in(cid: str) -> bool:
            return any(g["source_id"] == q["gold"][0]["source_id"]
                       and squash(g["evidence"]) in squash(chunk_text.get(cid, ""))
                       for g in q["gold"])

        retrieved_hits = [cid for cid in t.get("retrieved_ids", []) if evidence_in(cid)]
        context_ids = set(t.get("context_ids", []))
        in_context = [cid for cid in retrieved_hits if cid in context_ids]
        if in_context:
            grade, why = 2, f"evidence chunk {in_context[0]} in final context"
        elif retrieved_hits:
            grade, why = 1, f"evidence chunk {retrieved_hits[0]} retrieved but cut from context"
        else:
            grade, why = 0, "no valid evidence retrieved"
        rows.append((t["query_id"], grade, len(t.get("context_ids", [])), why))

    print(f"== {args.run} (context grading, test answerable) ==")
    counts = {0: 0, 1: 0, 2: 0}
    for qid, grade, n_ctx, why in rows:
        print(f"  {qid}: grade {grade}  (context chunks: {n_ctx})  {why}")
        if isinstance(grade, int):
            counts[grade] += 1
    print(f"  counts: 0={counts[0]} 1={counts[1]} 2={counts[2]}")


if __name__ == "__main__":
    main()
