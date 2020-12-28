import os
import re

script_dir = os.path.dirname(__file__)

who_pattern = re.compile("([a-z\s]+)\sbags?\scontain\s")
bags_pattern = re.compile("(\d+)\s([a-z\s]*)\sbags?")
main_bag = "shiny gold"


def get_rule(rule):
    who = who_pattern.match(rule).group(1)
    bags = bags_pattern.findall(rule)
    return who, bags


def create_graph(rules):
    graph = {main_bag: {}}
    for rule in rules:
        who, bags = get_rule(rule)
        if who not in graph:
            graph[who] = {}

        for item in bags:
            count, bag = item
            if bag not in graph:
                graph[bag] = {}
            graph[who][bag] = count
    return graph


def count_paths(graph):
    count = 0
    lookup_table = {}

    def has_main_node(bag_node):
        for bag in graph[bag_node].keys():
            if bag == main_bag or has_main_node(bag):
                lookup_table[bag] = True
                return lookup_table[bag]

        lookup_table[bag_node] = False
        return lookup_table[bag_node]

    for bag in graph.keys():
        if bag not in lookup_table:
            if has_main_node(bag):
                count += 1
        else:
            if lookup_table[bag]:
                count += 1
    return count


def solve(rules):
    graph = create_graph(rules)
    return count_paths(graph)


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    rules = reader.read().splitlines()
    print(solve(rules))


# rules = [
#     "light red bags contain 1 bright white bag, 2 muted yellow bags.",
#     "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
#     "bright white bags contain 1 shiny gold bag.",
#     "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
#     "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
#     "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
#     "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
#     "faded blue bags contain no other bags.",
#     "dotted black bags contain no other bags.",
# ]
#
# # color to outer
# {
#     "shiny gold": {"bright white": 1, "muted yellow": 2},
#     "light red": {},
#     "bright white": {"light red": 1, "dark orange": 3},
#     "muted yellow": {"light red": 2, "dark orange": 4},
#     "dark orange": {},
#     "faded blue": {"muted yellow": 9, "dark olive": 3, "vibrant plum": 5},
#     "dark olive": {"shiny gold": 1},
#     "vibrant plum": {"shiny gold": 2},
#     "dotted black": {"dark olive": 4, "vibrant plum": 6},
# }
# # color to inner
# {
#     "shiny gold": {"dark olive": 1, "vibrant plum": 2},
#     "light red": {"bright white": 1, "muted yellow": 2},
#     "bright white": {"shiny gold": 1},
#     "muted yellow": {"shiny gold": 2, "faded blue": 9},
#     "dark orange": {"bright white": 3, "muted yellow": 4},
#     "faded blue": {},
#     "dark olive": {"faded blue": 3, "dotted black": 4},
#     "vibrant plum": {"faded blue": 5, "dotted black": 6},
#     "dotted black": {},
# }
