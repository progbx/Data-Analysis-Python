from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable


def run_single_test_case(function: Callable, index: int) -> None:
    TESTS_ROOT = Path('tests', 'resources') / function.__name__

    test_path = TESTS_ROOT / f'case_{index}.py'
    expected_path = TESTS_ROOT / f'expected_{index}.py'

    with TemporaryDirectory() as tempdir:
        output_path = Path(tempdir) / f'output_{index}.py'
        function(test_path, output_path)

        with open(expected_path, 'r') as fe, open(output_path, 'r') as fo:
            assert fe.read() == fo.read()
