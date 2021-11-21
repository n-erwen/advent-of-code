
import re
    
def load_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().split('\n')

def parse_rules(bag_rules):
    def parse_contained_bag(bag):
        regex = r"([1-9]+) (.*) bags?"
        quantity, color = re.search(regex, bag).groups()
        return {"quantity": quantity, "color": color}
    
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

rules = parse_rules(load_input('./input.txt'))
print("(Day 7 Part 1): {} different colored bags can eventually contain a shiny gold bag.".format(
    len(colors_containing_shiny_gold_bag(rules)))
)
