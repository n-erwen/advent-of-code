import re
    
def load_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().split('\n')

def parse_rules(bag_rules):
    def parse_contained_bag(bag):
        regex = r"([1-9]+) (.*) bags?"
        quantity, color = re.search(regex, bag).groups()
        return {"quantity": int(quantity), "color": color}
    
    rules_dict = {}
    for r in bag_rules:
        color, contained_bags = r.split(" bags contain ")
        if contained_bags.rstrip(".") == "no other bags":
            rules_dict[color] = []
        else:
            rules_dict[color]= [parse_contained_bag(b) for b in contained_bags.rstrip(".").split(", ")]
    return rules_dict

# Part 1
def can_color_contain_shiny_gold_bag(color, rules):
    for b in rules[color]:
        if b["color"] == "shiny gold" or can_color_contain_shiny_gold_bag(b["color"], rules):
            return True
    return False

def colors_containing_shiny_gold_bag(rules):
    return [color for color in rules.keys() if can_color_contain_shiny_gold_bag(color, rules)]

# Part 2

def total_num_bags(bags):
    return sum([b["quantity"] for b in bags])

def how_many_bags_must_color_contain(color,rules):
    return total_num_bags(rules[color]) + \
        sum([how_many_bags_must_color_contain(b["color"], rules)*b["quantity"] for b in rules[color]])


rules = parse_rules(load_input('./input.txt'))
print("(Day 7 Part 1): {} different colored bags can eventually contain a shiny gold bag.".format(
    len(colors_containing_shiny_gold_bag(rules)))
)
print("(Day 7 Part 2): A single shiny bag must contain {} other bags.".format(
    how_many_bags_must_color_contain("shiny gold", rules)
))
