import re

def does_value_match_expression(value, pattern):
        return bool(re.compile(pattern).search(value))
    
def parse_passport_fields(passport):
    passport = passport.replace('\n', ' ').split(' ')
    passport_dict = {}
    for field in passport:
        key, value = field.split(":")
        passport_dict[key] = value
    return passport_dict

def has_required_fields(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for f in required_fields:
        if f not in passport.keys():
            return False
    return True

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
    return True if (has_required_fields(passport) and validate_fields(passport)) else False


if __name__ == "__main__":
    input_file = open("input.txt", "r")
    passports = input_file.read().split("\n\n")
    input_file.close()
    
    # Part 1
    passports = [parse_passport_fields(p) for p in passports]
    passports_with_all_required_fields = [has_required_fields(p) for p in passports]

    print("(Day 4: Part 1) Number of valid passports: " + str(passports_with_all_required_fields.count(True)))

    # Part 2
    valid_passports = [p for p in passports if is_passport_valid(p)]

    print("(Day 4: Part 2) Number of valid passports: " + str(len(valid_passports)))
