"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt.
"""

from pathlib import Path

LINE = "I tell you I'm thinking when I'm actually just waiting for you to finish typing."


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
