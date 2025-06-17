"""Template for programming assignment: Find errors in logs"""
from typing import Tuple, List
import re


def parse_error_messages(log: str) -> List[Tuple[int, int, int, int, int, int, str]]:
    pattern = r"ERROR - (\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}) - (.+)"
    matches = re.findall(pattern, log)
    result = []
    for match in matches:
        year, month, day, hour, minute, second, message = match
        result.append((int(year), int(month), int(day), int(hour), int(minute), int(second), message))
    return result
