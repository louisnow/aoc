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
            graph[who][bag] = int(count)
    return graph


def count_bags(graph):
    lookup_table = {}

    def get_count(bag_node):
        # You can count every bag for itself existing except for the main bag
        count = 0 if bag_node == main_bag else 1
        for bag in graph[bag_node].keys():
            if bag not in lookup_table:
                lookup_table[bag] = get_count(bag)
            count += graph[bag_node][bag] * lookup_table[bag]

        return count

    return get_count(main_bag)


def solve(rules):
    graph = create_graph(rules)
    return count_bags(graph)


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    rules = reader.read().splitlines()
    print(solve(rules))
