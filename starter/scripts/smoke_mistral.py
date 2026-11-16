"""Smoke test: one Mistral tool-calling round trip."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agent import MistralClient, tool_schema  # noqa: E402


def main() -> None:
    client = MistralClient(model="mistral-small-latest")
    messages = [
        {"role": "system", "content": "You are a test assistant."},
        {"role": "user", "content": "What is 2+2? Use the calculator tool."},
    ]
    tools = [{
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Compute an arithmetic expression",
            "parameters": {"type": "object",
                          "properties": {"expression": {"type": "string"}},
                          "required": ["expression"]},
        },
    }]
    data = client.chat(messages, tools)
    message = data["choices"][0]["message"]
    print("finish_reason:", data["choices"][0].get("finish_reason"))
    print("tool_calls:", bool(message.get("tool_calls")))
    print("usage:", client.usage)
    print("model:", data.get("model"))


if __name__ == "__main__":
    main()
