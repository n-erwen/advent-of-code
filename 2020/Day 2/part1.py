import re

def deconstruct_policy_string(policy):
    occurences, char = policy.split(" ")
    minimum, maximum = occurences.split("-")
    return { 
    "char": char,
    "min_occurences": int(minimum),
    "max_occurences": int(maximum)
    }

def does_password_match_policy(password, policy):

    policy_regex_str = r"^([^{0}]*{0}){{{1},{2}}}[^{0}]*$".format(policy["char"], policy["min_occurences"], policy["max_occurences"]) # regex pattern copied from https://stackoverflow.com/a/56185755
    policy_regex = re.compile(policy_regex_str)
    if policy_regex.search(password):
        return True
    return False

if __name__ == "__main__":
    input_file = open("input.txt","r")
    passwords_input = input_file.read().split("\n")
    input_file.close()

    valid_passwords = 0
    for p in passwords_input:
        policy_string, password = p.split(": ")
        policy = deconstruct_policy_string(policy_string)
        if does_password_match_policy(password, policy):
            valid_passwords += 1

    print("Valid passwords: " + str(valid_passwords))
