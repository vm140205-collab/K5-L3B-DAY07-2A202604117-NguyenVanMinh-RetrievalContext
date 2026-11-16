"""Apply human review labels (answer_grade 0-2, citation_support, abstention_correct)
to a run directory, producing reviews.json for starter/agent_metrics.py.

Labels were assigned by reading each answer against the expected answer and the
full cited chunk text (review_draft.md + full-text checks in traces.jsonl).
Drafted with AI assistance; the student verified each label before submission.
Grade rules (BENCHMARK.md): 0 = wrong or missing evidence; 1 = partially correct;
2 = correct and complete. Abstaining on an answerable question = 0.
citation_support: cited chunk is in context AND its text supports the claim.
"""
import argparse
import json
from pathlib import Path

# Per run: query_id -> (answer_grade | None, citation_support list, abstention_correct | None)
LABELS = {
    "dense800-dev": {
        "q01": (0, [], None), "q02": (2, [True], None), "q03": (0, [], None),
        "q04": (2, [True], None), "q05": (0, [], None),
        "q06": (2, [True, True], None), "q07": (0, [], None), "q08": (2, [True], None),
        "q09": (0, [], None), "q10": (0, [], None), "q11": (0, [False], None),
        "q12": (1, [True], None), "q13": (2, [True], None), "q14": (0, [], None),
        "q15": (1, [False], None),
        "u01": (None, [], True), "u02": (None, [], True),
    },
    "hybrid3500-dev": {
        "q01": (2, [True], None), "q02": (2, [True, True], None),
        "q03": (0, [False, False], None), "q04": (2, [True, True], None),
        "q05": (2, [False, True, True], None), "q06": (2, [True], None),
        "q07": (1, [True], None), "q08": (2, [True, True], None),
        "q09": (0, [False], None), "q10": (2, [True], None),
        "q11": (2, [True, True], None), "q12": (2, [True], None),
        "q13": (2, [True], None), "q14": (2, [True, False], None),
        "q15": (2, [True], None),
        "u01": (None, [], True), "u02": (None, [], True),
    },
    "alltools-dev": {
        "q01": (0, [], None), "q02": (2, [True, True], None), "q03": (2, [True], None),
        "q04": (2, [True, True], None), "q05": (2, [True, False, True], None),
        "q06": (1, [False, True], None), "q07": (1, [True], None),
        "q08": (2, [True, True], None), "q09": (2, [True], None),
        "q10": (2, [False, True], None), "q11": (0, [False], None),
        "q12": (2, [True, True, True], None), "q13": (2, [True], None),
        "q14": (2, [True], None), "q15": (2, [True, True], None),
        "u01": (None, [], True), "u02": (None, [], True),
    },
    "hybrid3500-medium-dev": {
        "q01": (2, [True], None), "q02": (2, [True, True], None), "q03": (2, [True], None),
        "q04": (2, [True, True, True], None), "q05": (2, [False, True, True], None),
        "q06": (2, [True], None), "q07": (0, [], None), "q08": (2, [True, True], None),
        "q09": (0, [False], None), "q10": (2, [False, False, True], None),
        "q11": (2, [True], None), "q12": (2, [True, True], None), "q13": (2, [True], None),
        "q14": (2, [True, False], None), "q15": (2, [True], None),
        "u01": (None, [False], False),  # answered an unanswerable question (hallucinated theorem)
        "u02": (None, [], True),
    },
    # ---- test split ----
    "dense800-test": {
        "q16": (2, [True], None), "q17": (2, [True], None), "q18": (0, [], None),
        "q19": (None, [], None),  # provider error (ConnectTimeout); excluded from quality metrics
        "q20": (0, [], None),
        "u03": (None, [], True), "u04": (None, [], True),
    },
    "hybrid3500-test": {
        "q16": (2, [True, True], None), "q17": (2, [True], None),
        "q18": (1, [True, True, False], None), "q19": (1, [True, False, True], None),
        "q20": (2, [True, True], None),
        "u03": (None, [], True), "u04": (None, [], True),
    },
    "hybrid3500-large-low-test": {
        "q16": (2, [True, True], None), "q17": (2, [True], None),
        "q18": (1, [True, True], None), "q19": (0, [], None), "q20": (2, [True, True], None),
        "u03": (None, [], True), "u04": (None, [], True),
    },
    "hybrid3500-large-low-dev": {
        "q01": (2, [True], None), "q02": (2, [True, True], None), "q03": (2, [True], None),
        "q04": (2, [True, True, True, True], None), "q05": (2, [False, True, True], None),
        "q06": (2, [True, True], None), "q07": (2, [True], None), "q08": (2, [True, True], None),
        "q09": (0, [], None), "q10": (2, [True, False, True], None),
        "q11": (2, [True, True], None), "q12": (2, [True, True, True], None),
        "q13": (2, [True], None), "q14": (2, [True, False], None), "q15": (2, [True], None),
        "u01": (None, [], True), "u02": (None, [], True),
    },
    "alltools-medium-dev": {
        "q01": (2, [True], None), "q02": (2, [True, True], None), "q03": (0, [], None),
        "q04": (2, [True, True], None), "q05": (2, [False, True, True], None),
        "q06": (2, [False, True], None), "q07": (2, [True], None),
        "q08": (2, [True, True], None), "q09": (0, [], None),
        "q10": (2, [False, False, True, True], None), "q11": (2, [True, True], None),
        "q12": (2, [True, True], None), "q13": (2, [True], None),
        "q14": (2, [True, False, True], None), "q15": (2, [True], None),
        "u01": (None, [], True), "u02": (None, [], True),
    },
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Ghi nhãn đánh giá cho một run")
    parser.add_argument("--run", required=True, help="tên run, vd hybrid3500-dev")
    parser.add_argument("--run-dir", required=True, type=Path)
    args = parser.parse_args()

    labels = LABELS[args.run]
    traces = [json.loads(l) for l in
              (args.run_dir / "traces.jsonl").read_text(encoding="utf-8").splitlines()]
    reviews = []
    for t in traces:
        qid = t["query_id"]
        grade, support, abstain = labels[qid]
        n_citations = len(t.get("citations", []))
        if len(support) != n_citations:
            raise SystemExit(f"{qid}: {len(support)} support labels for "
                             f"{n_citations} citations in {args.run}")
        review = {"query_id": qid, "citation_support": support}
        if t.get("answerable"):
            review["answer_grade"] = grade
        else:
            review["abstention_correct"] = abstain
        reviews.append(review)

    (args.run_dir / "reviews.json").write_text(
        json.dumps(reviews, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.run_dir / 'reviews.json'} ({len(reviews)} labels)")


if __name__ == "__main__":
    main()
