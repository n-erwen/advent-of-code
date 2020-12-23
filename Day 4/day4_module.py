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