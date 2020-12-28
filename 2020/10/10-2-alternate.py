import os

script_dir = os.path.dirname(__file__)

#
# My goal was to reduce it to O(n) excluding the sorting step
#
# Sorted Arr [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
# Count list [1, 1, 3, 2, 1, 1, 2, 1, 1, 1, 1]
#
# Sorted Arr [1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]
# Count list [3, 3, 2, 1, 1, 3, 3, 2, 1, 1, 1, 3, 2, 1, 1, 2, 1, 1, 1, 3, 3, 2, 1, 1, 1, 1, 1, 3, 3, 2, 1]
#
# Assuming no duplicates are present
#
# If you work it out the following cannot occur in a contiguous fashion,
# You can try finding numbers that do it, you'll see it's impossible (no duplicates allowed)
#
# "3, 3, 3" , "3,1"  , "2,2" , "2,3"
#
# Therefore
#  -> 3 will always be followed by either exactly one more 3 or a 2
#  -> 2 is always followed by a 1 and hence the pattern will always end with a 1
#
# Now you can work out how many possible ways each of the subgroups can be arranged
# 3, 3, 2, 1 -> 7 ways
# 3, 2, 1    -> 4 ways
# 2, 1       -> 2 ways
#
#  Also based on the rules, no other patterns besides the ones above can exist
#
def calculate(arr):
    p = 1
    prev = arr[0]
    i = 1
    while i < len(arr):
        n = arr[i]
        # the values I multiply with can be worked out on paper
        if prev == 3 and n == 3:
            p *= 7
            i += 2
        elif prev == 1 and n == 2:
            p *= 2
        elif prev == 3 and n == 2:
            p *= 4
            i += 1
        prev = arr[i]
        i += 1
    return p


def solve(numbers):
    n_sorted = sorted(numbers)
    prev = 0
    count_list = []
    for i in range(len(n_sorted)):
        n = n_sorted[i]
        j = i
        count = 0
        while j < len(n_sorted) and n_sorted[j] - prev <= 3:
            count += 1
            j += 1
        count_list.append(count)
        prev = n
        i += 1
    return calculate(count_list)


with open(os.path.join(script_dir, "in1.txt"), "r") as reader:
    numbers = [int(x) for x in reader.read().splitlines()]
    print(solve(numbers))
