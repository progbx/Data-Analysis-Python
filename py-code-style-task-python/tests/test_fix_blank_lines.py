"""Sample tests for programming assignment: Fix blank lines"""
from tasks.fix_blank_lines import fix_blank_lines
from tests.util import run_single_test_case


def test_fix_blank_lines():
    # Sample tests
    run_single_test_case(fix_blank_lines, 1)
    run_single_test_case(fix_blank_lines, 2)
    run_single_test_case(fix_blank_lines, 3)
