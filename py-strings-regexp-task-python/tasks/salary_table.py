"""Template for programming assignment: Print salary table"""
from typing import Tuple, List


def make_salary_table_string(
        humans_and_salaries: List[Tuple[str, str, int]]) -> str:
    header = (
        f"{'#':>5} | {'Person Name':<20} | {'Annual Salary':^20} | {'Monthly Salary':^20}"
    )
    separator = '-' * len(header)
    rows = [header, separator]

    for idx, (first_name, last_name, annual_salary) in enumerate(humans_and_salaries, start=1):
        person_name = f"{last_name} {first_name[0]}."
        annual_str = f"{annual_salary:,}$"
        monthly_salary = round(annual_salary / 12, 1)
        monthly_str = f"{monthly_salary:,.1f}$"
        row = f"{idx:>5} | {person_name:<20} | {annual_str:^20} | {monthly_str:^20}"
        rows.append(row)

    return "\n".join(rows)
