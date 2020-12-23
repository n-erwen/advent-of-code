from day4_module import parse_passport_fields, has_required_fields

def is_passport_valid(passport):
    return has_required_fields(passport)

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    passports = input_file.read().split("\n\n")
    input_file.close()
    
    passports = [parse_passport_fields(p) for p in passports]
    valid_passports = [is_passport_valid(p) for p in passports]
    
    print("Valid passports: " + str(valid_passports.count(True)))
