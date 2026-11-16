"""Probe which thinking/reasoning-effort parameters the Mistral API accepts.

Tries several parameter shapes on a trivial request and reports status codes,
so the agent can use the supported one as a configurable thinking level.
"""
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
KEY = os.environ["MISTRAL_API_KEY"]
URL = "https://api.mistral.ai/v1/chat/completions"

PARAM_SHAPES = {
    "thinking.level=low": {"thinking": {"level": "low"}},
    "thinking.level=medium": {"thinking": {"level": "medium"}},
    "reasoning_effort=low": {"reasoning_effort": "low"},
    "reasoning_effort=medium": {"reasoning_effort": "medium"},
}

MODELS = ["mistral-small-latest", "mistral-medium-latest", "mistral-large-latest",
          "magistral-small-latest"]


def main() -> None:
    for model in MODELS:
        for name, extra in PARAM_SHAPES.items():
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": "Reply with the single word: ok"}],
                "max_tokens": 2000,
                **extra,
            }
            try:
                r = requests.post(URL, headers={"Authorization": f"Bearer {KEY}"},
                                  json=payload, timeout=60)
                if r.status_code == 200:
                    data = r.json()
                    content = data["choices"][0]["message"].get("content")
                    ctype = type(content).__name__
                    print(f"ACCEPTED  {model:24s} {name:24s} (content type {ctype})")
                else:
                    detail = r.text[:120].replace("\n", " ")
                    print(f"rejected  {model:24s} {name:24s} -> {r.status_code} {detail}")
            except requests.RequestException as exc:
                print(f"error     {model:24s} {name:24s} -> {type(exc).__name__}")
        print()


if __name__ == "__main__":
    main()
