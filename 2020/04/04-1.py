import os

script_dir = os.path.dirname(__file__)

required_keys = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]
req_map = {x: True for x in required_keys}


def solve(passport):
    data = passport.split()
    passport_req_keys = {x: False for x in required_keys}
    for item in data:
        key, value = item.split(":")
        if key in req_map:
            passport_req_keys[key] = True
    for key, value in passport_req_keys.items():
        if not value:
            return False
    return True


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    passports = reader.read().split("\n\n")
    count = 0
    for passport in passports:
        if solve(passport):
            count += 1
    print(count)
