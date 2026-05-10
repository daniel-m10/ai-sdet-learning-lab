import re
import sys
from pathlib import Path


STATUSES = ("passed", "failed", "skipped")


def count_results(text):
    counts = dict.fromkeys(STATUSES, 0)
    summary_lines = [line for line in text.splitlines() if " in " in line]

    for line in summary_lines[-1:]:
        for number, status in re.findall(r"(\d+)\s+(passed|failed|skipped)\b", line):
            counts[status] = int(number)

    return counts


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/pytest_summary.py <pytest-output.txt>")
        return 1

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"File not found: {path}")
        return 1

    counts = count_results(path.read_text(encoding="utf-8"))
    for status in STATUSES:
        print(f"{status}: {counts[status]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
