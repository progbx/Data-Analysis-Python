import os
from typing import Union

PathLike = Union[str, bytes, os.PathLike]

def fix_blank_lines(input_path: PathLike, output_path: PathLike) -> None:
    """
    Adds or removes blank lines in a Python script to satisfy
    the PEP8 guidelines.

    The output script will have:
      1. Top-level function and class definitions surrounded by two blank lines.
      2. All other code fragments separated by no more than one blank line.
      3. The file ending with a blank line.

    Args:
        input_path : Path-like
            A path to the input Python script (.py file)
        output_path : Path-like
            A path to the output Python script (.py file)

    Returns: None
    """
    with open(input_path, "r", encoding="utf-8") as f:
        # Remove trailing whitespace from each line.
        lines = [line.rstrip() for line in f.readlines()]

    # First, collapse multiple consecutive blank lines into a single blank line.
    collapsed = []
    for line in lines:
        if line == "":
            if collapsed and collapsed[-1] == "":
                continue
        collapsed.append(line)

    output_lines = []
    for line in collapsed:
        # Identify a top-level function or class definition.
        if line and (line == line.lstrip()) and (line.startswith("def ") or line.startswith("class ")):
            # Remove any blank lines at the end of the current output.
            while output_lines and output_lines[-1] == "":
                output_lines.pop()
            # If not at the beginning of the file, ensure two blank lines precede the definition.
            if output_lines:
                output_lines.append("")
                output_lines.append("")
            output_lines.append(line)
        else:
            # For all other lines, do not allow more than one consecutive blank line.
            if line == "":
                if output_lines and output_lines[-1] == "":
                    continue
            output_lines.append(line)

    # Ensure the file ends with a blank line.
    if not output_lines or output_lines[-1] != "":
        output_lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        # The join will yield a trailing newline because the last element is blank.
        f.write("\n".join(output_lines))
