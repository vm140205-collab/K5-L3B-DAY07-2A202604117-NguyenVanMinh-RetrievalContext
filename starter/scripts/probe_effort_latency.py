"""Measure latency and reasoning tokens per reasoning_effort level on one question.

Answers "is the model slow, or is it the network?" with numbers instead of a guess.
"""
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import requests  # noqa: E402

from agent import LLM_API_KEY, LLM_BASE_URL  # noqa: E402

MODEL = "deepseek-v4-1-flash-1017"
EFFORTS = [None, "none", "low", "high", "xhigh"]
PROMPT = (
    "A paper reports: 'a regret that only depends sub-linearly on the maximal number "
    "of jobs in the network, S'. Explain in two sentences how the regret scales with S, "
    "and cite the chunk id [36412c830e6b326a10b5]."
)


def main() -> None:
    for effort in EFFORTS:
        payload = {"model": MODEL, "messages": [{"role": "user", "content": PROMPT}],
                   "temperature": 0.0, "top_p": 1, "max_tokens": 4000}
        if effort:
            payload["reasoning_effort"] = effort
        started = time.time()
        try:
            r = requests.post(f"{LLM_BASE_URL}/chat/completions",
                              headers={"Authorization": f"Bearer {LLM_API_KEY}"},
                              json=payload, timeout=300)
            elapsed = time.time() - started
            if r.status_code != 200:
                print(f"effort={str(effort):6s} HTTP {r.status_code} after {elapsed:.1f}s "
                      f"{r.text[:90]}")
                continue
            usage = r.json()["usage"]
            details = usage.get("completion_tokens_details") or {}
            print(f"effort={str(effort):6s} {elapsed:6.1f}s  "
                  f"completion={usage['completion_tokens']:5d}  "
                  f"reasoning={details.get('reasoning_tokens', 0):5d}")
        except requests.RequestException as exc:
            print(f"effort={str(effort):6s} {type(exc).__name__} after "
                  f"{time.time() - started:.1f}s")


if __name__ == "__main__":
    main()
