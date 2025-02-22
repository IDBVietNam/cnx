#!/usr/bin/env python
import re
import sys


def check_for_print_statements(files):
    """Checks if the given files contain print statements."""
    print_usage_pattern = re.compile(r"^\s*print\(")

    has_print = False
    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    if print_usage_pattern.search(line):
                        print(f"Print statement found in {file} at line {line_no}")
                        has_print = True
        except Exception as e:
            print(f"⚠️ Could not read file {file}: {e}")

    return has_print


if __name__ == "__main__":
    files_to_check = sys.argv[1:]
    if check_for_print_statements(files_to_check):
        print("Commit rejected! Remove print statements before committing.")
        sys.exit(1)
    sys.exit(0)
