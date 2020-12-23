def parse_passport(passport):
    passport = passport.replace('\n', ' ').split(' ')
    passport_dict = {}
    for field in passport:
        key, value = field.split(":")
        passport_dict[key] = value
    return passport_dict

def is_passport_valid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for f in required_fields:
        if f not in passport.keys():
            return False
    return True

input_file = open("input.txt", "r")
passports = input_file.read().split("\n\n")
input_file.close()

passports = list(map(parse_passport, passports))

valid_passports = list(map(is_passport_valid, passports))
print("Valid passports: " + str(valid_passports.count(True)))
