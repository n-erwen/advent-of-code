import re
from day4_module import parse_passport_fields, has_required_fields

def does_value_match_expression(value, pattern):
    return bool(re.compile(pattern).search(value))

def validate_fields(passport):
    field_patterns = {
        "byr": r"^19[2-9][0-9]$|^200[0-2]$",
        "iyr": r"^201[0-9]$|^2020$",
        "eyr": r"^202[0-9]$|^2030$",
        "hgt": r"^1([5-8][0-9]|9[0-3])cm$|^(59|6[0-9]|7[0-6])in$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^\d{9}$"
    }
    all_fields_checked = [
        does_value_match_expression(passport[f], field_patterns[f]) for f in field_patterns.keys()
    ]
    return all(field for field in all_fields_checked)

def is_passport_valid(passport):
    if has_required_fields(passport):
        return passport if validate_fields(passport) else None
    return None

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    passports = input_file.read().split("\n\n")
    input_file.close()

    passports = [parse_passport_fields(p) for p in passports]

    valid_passports = [is_passport_valid(p) for p in passports if is_passport_valid(p)]

    print("Valid passports: " + str(len(valid_passports)))
