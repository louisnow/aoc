import os
import re
import math

script_dir = os.path.dirname(__file__)

# prefer euclids instead of a brute force
# works since our modulo inputs are small
def get_inverse(n, modulo):
    for i in range(1, modulo):
        if (n * i) % modulo == 1:
            return i


def solve(bus_list):
    buses = []
    remainders = []
    product = 1
    for index, bus_id in enumerate(bus_list):
        if bus_id == "x":
            continue
        product *= bus_id
        remainders.append((bus_id - index) % bus_id)
        buses.append(bus_id)

    ans = 0
    # Chinese Remainder Theorem
    for index, bus in enumerate(buses):
        bus_product = product // bus
        inverse_product = get_inverse(bus_product, bus)
        ans += remainders[index] * bus_product * inverse_product

    return ans % product


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    line = reader.read().splitlines()[1]
    bus_list = [x if x == "x" else int(x) for x in line.split(",")]
    print(solve(bus_list))
