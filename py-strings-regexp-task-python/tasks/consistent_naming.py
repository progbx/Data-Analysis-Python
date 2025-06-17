"""Template for programming assignment: Make naming consistent"""
import re
import keyword


def make_naming_consistent(code: str) -> str:
    identifier_pattern = r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"
    identifiers = re.findall(identifier_pattern, code)

    snake_case_count = 0
    camel_case_count = 0

    for ident in identifiers:
        if keyword.iskeyword(ident):
            continue
        if '_' in ident:
            snake_case_count += 1
        elif re.search(r'[A-Z]', ident) or re.search(r'\d', ident):
            camel_case_count += 1

    to_snake_case = snake_case_count >= camel_case_count

    def camel_to_snake(s):
        s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
        s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
        s = re.sub(r'([A-Za-z])([0-9])', r'\1_\2', s)
        return s.lower()

    def snake_to_camel(s):
        parts = s.strip('_').split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])

    def replace_identifier(match):
        ident = match.group(0)
        if keyword.iskeyword(ident):
            return ident
        if to_snake_case and not ('_' in ident):
            return camel_to_snake(ident)
        elif not to_snake_case and ('_' in ident):
            return snake_to_camel(ident)
        return ident

    return re.sub(identifier_pattern, replace_identifier, code)