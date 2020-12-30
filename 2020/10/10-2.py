import os

script_dir = os.path.dirname(__file__)


def solve_simpler(numbers):
    n_sorted = sorted(numbers)
    # Add the 0 and max+3 to either ends of the array
    n_sorted.append(n_sorted[-1] + 3)
    n_sorted.insert(0, 0)
    dp = {}

    def recur(i):
        if i == len(n_sorted) - 1:
            return 1
        if i in dp:
            return dp[i]

        prev = n_sorted[i]
        j = i + 1
        count = 0
        while j < len(n_sorted) and n_sorted[j] - prev <= 3:
            dp[j] = recur(j)
            count += dp[j]
            j += 1

        return count

    return recur(0)


# Avoids having to add 0 and max + 3 to the either ends of the array
# Although the above solve_simpler is far more obvious/readable
def solve(numbers):
    n_sorted = sorted(numbers)
    dp = {}

    def recur(i, prev=0):
        if i >= len(n_sorted):
            return 1
        if i in dp:
            return dp[i]
        j = i
        count = 0
        while j < len(n_sorted) and n_sorted[j] - prev <= 3:
            j += 1
            dp[j] = recur(j, n_sorted[j - 1])
            count += dp[j]
        return count

    return recur(0, 0)


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    numbers = [int(x) for x in reader.read().splitlines()]
    print(solve(numbers))
    print(solve_simpler(numbers))
