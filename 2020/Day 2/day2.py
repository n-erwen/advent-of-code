import re

def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n")

def parse_password_policy(policy):
    limits, char = policy.split(" ")
    return [char] + [int(i) for i in limits.split("-")]

def day2_part1(pwds):
    """Day 2 Part 1: Find the number of valid passwords according to how many times a character occurs in them"""
    valid_passwords = 0
    for p in pwds:
        policy_str, password = p.split(": ")
        policy = parse_password_policy(policy_str)
        policy_regex = re.compile(
            r"^([^{0}]*{0}){{{1},{2}}}[^{0}]*$".format(
                policy[0], policy[1], policy[2]
            )
        )
        if policy_regex.match(password):
            valid_passwords += 1
    return valid_passwords

def day2_part2(pwds):
    """Day 2 Part 2: Find the number of valid passwords according to whether a character occurs in only one of two positions"""
    valid_passwords = 0
    for p in pwds:
        policy_str, password = p.split(": ")
        policy = parse_password_policy(policy_str)
        pos1_chars_match = password[policy[1] - 1] == policy[0]
        pos2_chars_match = password[policy[2] - 1] == policy[0]
        if (pos1_chars_match and not pos2_chars_match) or (not pos1_chars_match and pos2_chars_match):
            valid_passwords += 1
    return valid_passwords

if __name__ == "__main__":
    passwords_input = load_input("./input.txt")
    print("(Day 2 Part 1) Number of valid passwords: " + str(day2_part1(passwords_input)))
    print("(Day 2 Part 2) Valid passwords: " + str(day2_part2(passwords_input)))
