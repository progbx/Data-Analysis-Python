import os
import math
from typing import Union

PathLike = Union[str, bytes, os.PathLike]

def fix_margins(input_path: PathLike, output_path: PathLike) -> None:
    """
    Adds or removes indentation whitespaces and removes trailing
    whitespaces in a Python script to satisfy the PEP8 guidelines.

    The output script will have:
      1. Four whitespaces per indentation level.
      2. Tabs replaced by four whitespaces.
      3. Trailing whitespaces removed.

    Args:
        input_path : Path-like
            A path to the input Python script (.py file)
        output_path : Path-like
            A path to the output Python script (.py file)

    Returns: None
    """
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Replace tabs with four spaces and remove trailing whitespaces.
    processed_lines = [line.replace("\t", " " * 4).rstrip() for line in lines]

    # Collect indent counts for non-blank lines that start with a space.
    indent_counts = []
    for line in processed_lines:
        if line and line.startswith(" "):
            count = len(line) - len(line.lstrip(" "))
            indent_counts.append(count)
    
    # Determine the indent unit. If there are indented lines, compute the GCD of their indent counts.
    if indent_counts:
        unit = indent_counts[0]
        for count in indent_counts[1:]:
            unit = math.gcd(unit, count)
        # Fallback in the unlikely event that GCD is 0.
        if unit == 0:
            unit = min(indent_counts)
    else:
        unit = 1

    new_lines = []
    for line in processed_lines:
        if line:
            # Count the number of leading spaces.
            leading = len(line) - len(line.lstrip(" "))
            # Compute the indent level relative to the unit.
            level = (leading // unit) if leading else 0
            new_indent = " " * (level * 4)
            new_lines.append(new_indent + line.lstrip(" "))
        else:
            new_lines.append("")

    # Ensure the file ends with a newline.
    output_content = "\n".join(new_lines) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_content)
