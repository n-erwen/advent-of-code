import re

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

def validate_height(height):
    height_format = re.compile(r"\d+(cm|in)")
    if height_format.search(height):
        h = int(height[:-2])
        unit = height[-2:]
        height_validation = {"cm": (h >= 150 and h <= 193), "in":(h >= 59 and h <= 76),}
        return height_validation[unit]
    

def validate_fields(passport):
    is_byr_valid = int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002
    is_iyr_valid = int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
    is_eyr_valid = int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030
    is_hgt_valid = validate_height(passport["hgt"])
    is_hcl_valid = bool(re.compile(r"#[0-9a-f]{6}").search(passport["hcl"]))
    is_ecl_valid = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    is_pid_valid = bool(re.compile(r"\d{9}").search(passport["pid"]))
    return is_byr_valid and is_iyr_valid and is_eyr_valid and is_hgt_valid and is_hcl_valid and is_ecl_valid and is_pid_valid

def is_passport_valid(passport):
    if has_required_fields(passport):
        return validate_fields(passport)
    return False

input_file = open("input.txt", "r")
passports = input_file.read().split("\n\n")
input_file.close()

passports = list(map(parse_passport_fields, passports))

valid_passports = list(map(is_passport_valid, passports[:]))
print("Valid passports: " + str(valid_passports.count(True)))

<hr>

""" 
Wrong Answers: 128
"""
