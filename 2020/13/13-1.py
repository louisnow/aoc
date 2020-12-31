import os
import re
import math

script_dir = os.path.dirname(__file__)


def solve(depart, buses):
    nearest = None
    bus_id = None
    for bus in buses:
        bus_depart = bus * math.ceil(depart / bus)
        wait_time = bus_depart - depart
        if nearest is None or nearest > wait_time:
            nearest = wait_time
            bus_id = bus
    return nearest * bus_id


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    lines = [[int(x) for x in re.findall("\d+", l)] for l in reader.read().splitlines()]
    depart = lines[0][0]
    buses = lines[1]
    print(solve(depart, buses))
