# [Python] Code style and best practices

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

- The principles of the Zen of Python
- Best practices from the PEP8 style guide

## Overview

The coding exercises cover the following practical problems:

- Fixing margins
- Fixing blank lines

## Coding exercises

### Exercise 1: Fixing margins

Your task is to implement a function that adds or removes indentation
whitespaces and removes trailing whitespaces in a Python script to satisfy
the PEP8 guidelines.

The requirements for the output script are the following:
1. Four whitespaces should be used per indentation level.
2. If tabs are used for indentation, they should be replaced
   with four whitespaces.
3. Trailing whitespaces should be removed.

Note that any number of whitespaces can be used to indent in Python.
You can assume that the inputs will be such that arguments of a function or
conditional statements always occupy one line.

```python
import os
from typing import Union

PathLike = Union[str, bytes, os.PathLike]

def fix_margins(input_path: PathLike, output_path: PathLike) -> None:
    """
    Adds or removes indentation whitespaces and removes trailing
    whitespaces in a Python script to satisfy the PEP8 guidelines.

    The requirements for the output script are the following:
    1. Four whitespaces should be used per indentation level.
    2. If tabs are used for indentation, they should be replaced
       with four whitespaces.
    3. Trailing whitespaces should be removed.

    Note that any number of whitespaces can be used to indent in
    Python. You can assume that the inputs will be such that arguments
    of a function or conditional statements always occupy one line.

    Args:
        input_path : Path-like
            A path to the input Python script (.py file)
        output_path : Path-like
            A path to the output Python script (.py file)

    Returns: None
    """
    pass
```

See the `tests/test_fix_margins.py` and `tests/util.py` files and the
`tests/resources/fix_margins/` folder for examples.

### Exercise 2: Fixing blank lines

Your task is to implement a function that adds or removes blank lines
in a Python script to satisfy the PEP8 guidelines.

The requirements for blank lines in the output script are
the following:
1. Top-level function and class definitions should be surrounded
   by two blank lines.
2. The rest of the code fragments can be separated by no more than
   one blank line.
3. The file should end with a blank line.

```python
import os
from typing import Union

PathLike = Union[str, bytes, os.PathLike]

def fix_blank_lines(input_path: PathLike, output_path: PathLike) -> None:
    """
    Adds or removes blank lines in a Python script to satisfy
    the PEP8 guidelines.

    The requirements for blank lines in the output script are
    the following:
    1. Top-level function and class definitions should be surrounded
       by two blank lines.
    2. The rest of the code fragments can be separated by no more than
       one blank line.
    3. The file should end with a blank line.

    Args:
        input_path : Path-like
            A path to the input Python script (.py file)
        output_path : Path-like
            A path to the output Python script (.py file)

    Returns: None
    """
    pass
```

See the `tests/test_fix_blank_lines.py` and `tests/util.py` files and the
`tests/resources/fix_blank_lines/` folder for examples.
