def deconstruct_policy_string(policy):
    positions, char = policy.split(" ")
    pos1, pos2 = positions.split("-")
    return { 
    "char": char,
    "pos1": int(pos1),
    "pos2": int(pos2)
    }

def does_password_match_policy(password, policy):
    pos1_chars_match = password[policy["pos1"] - 1] == policy["char"]
    pos2_chars_match = password[policy["pos2"] - 1] == policy["char"]
    is_password_valid = (pos1_chars_match and not pos2_chars_match) or (not pos1_chars_match and pos2_chars_match)
    if is_password_valid:
        return True
    return False

if __name__ == "__main__":
    input_file = open("input.txt","r")
    passwords = input_file.read().split("\n")
    input_file.close()

    valid_passwords = 0
    for p in passwords:
        policy_string, password = p.split(": ")
        policy = deconstruct_policy_string(policy_string)
        if does_password_match_policy(password, policy):
            valid_passwords += 1

    print("Valid passwords: " + str(valid_passwords))
