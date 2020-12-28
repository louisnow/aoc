import os
import re

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


def validate(key, data):
    if key == "byr":
        value = int(data)
        return value >= 1920 and value <= 2020
    if key == "iyr":
        value = int(data)
        return value >= 2010 and value <= 2020
    if key == "eyr":
        value = int(data)
        return value >= 2020 and value <= 2030
    if key == "hgt":
        if not re.compile("^[0-9]*(in|cm)$").match(data):
            return False
        suffix = data[-2:]
        value = int(data[:-2])
        if suffix == "cm":
            return value >= 150 and value <= 193
        else:
            return value >= 59 and value <= 76
    if key == "hcl":
        return re.compile("^#[0-9,a-f]{6}$").match(data)
    if key == "ecl":
        valid_keys = {
            "amb": 1,
            "blu": 1,
            "brn": 1,
            "gry": 1,
            "grn": 1,
            "hzl": 1,
            "oth": 1,
        }
        return data in valid_keys
    if key == "pid":
        return re.compile("^[0-9]{9}$").match(data)


def solve(passport):
    data = passport.split()
    passport_req_keys = {x: False for x in required_keys}
    for item in data:
        key, value = item.split(":")
        if key in req_map:
            passport_req_keys[key] = validate(key, value)
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
