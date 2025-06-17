"""Sample tests for programming assignment: Fix margins"""
from tasks.fix_margins import fix_margins
from tests.util import run_single_test_case


def test_fix_margins():
    # Sample tests
    run_single_test_case(fix_margins, 1)
    run_single_test_case(fix_margins, 2)
    run_single_test_case(fix_margins, 3)
