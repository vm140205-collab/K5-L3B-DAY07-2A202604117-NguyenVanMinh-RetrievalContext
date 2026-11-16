"""Draft human-review files from agent traces: answer vs expected + cited chunk
excerpts, so a person can grade 0/1/2, citation support and abstention.

Outputs per run directory:
- review_draft.md   : one section per question with everything needed to grade
- reviews_draft.json: machine-readable skeleton (grades null; filled by hand or
                       by applying the reviewer's decisions)
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
    parser = argparse.ArgumentParser(description="Soạn hồ sơ đánh giá thủ công")
    parser.add_argument("--traces", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    questions = {q["id"]: q for q in (
        json.loads(l) for l in
        (REPO_ROOT / "benchmark" / "questions.jsonl").read_text(encoding="utf-8").splitlines())}
    # chunk text lookup from the trace search results themselves
    chunk_text: dict[str, str] = {}
    traces = [json.loads(l) for l in args.traces.read_text(encoding="utf-8").splitlines()]

    lines = ["# Review draft\n"]
    reviews = []
    for t in traces:
        q = questions[t["query_id"]]
        for s in t.get("searches", []):
            for r in s["results"]:
                chunk_text.setdefault(r["id"], r["text"])
        lines.append(f"## {t['query_id']} ({'answerable' if q['answerable'] else 'UNANSWERABLE'}) "
                     f"— status: {t['status']}")
        lines.append(f"Q: {q['question']}")
        if q["answerable"]:
            lines.append(f"EXPECTED: {q['expected_answer']}")
            lines.append(f"GOLD: {q['gold'][0]['source_id']} p{q['gold'][0]['page']}: "
                         f"\"{q['gold'][0]['evidence'][:160]}\"")
        else:
            lines.append(f"VERIFY (unanswerable): {q.get('verification', '')[:200]}")
        lines.append(f"AGENT: {t.get('answer', '')}")
        if t["status"] == "answered":
            for cid in t["citations"]:
                excerpt = chunk_text.get(cid, "(not found in trace)")
                gold_hit = ""
                if q["answerable"]:
                    gold_hit = " [CONTAINS GOLD EVIDENCE]" if any(
                        squash(g["evidence"]) in squash(excerpt) for g in q["gold"]) else ""
                lines.append(f"- [{cid}]{gold_hit}: {excerpt[:260]}")
        elif t["status"] == "error":
            lines.append(f"ERROR: {t.get('error', '')[:200]}")
        lines.append("")
        reviews.append({
            "query_id": t["query_id"],
            "answer_grade": None if q["answerable"] else None,
            "citation_support": [None] * len(t.get("citations", [])),
            "abstention_correct": None,
            "_status": t["status"],
            "_answerable": q["answerable"],
        })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "review_draft.md").write_text("\n".join(lines), encoding="utf-8")
    skeleton = [{k: v for k, v in r.items() if not k.startswith("_")} for r in reviews]
    (args.output_dir / "reviews_draft.json").write_text(
        json.dumps(skeleton, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output_dir / 'review_draft.md'} ({len(traces)} questions)")


if __name__ == "__main__":
    main()
