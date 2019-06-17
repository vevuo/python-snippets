"""
Recursive staircase problem

- Staircase with N steps.
- Your are either going step by step or skipping one between.

How many different ways to climb the staircase?
"""

def num_ways(n):
    nums = []
    nums.insert(0, 1)
    nums.insert(1, 1)

    for i in range(2, n + 1):
        nums.insert(i, nums[i - 1] + nums [i - 2])

    return nums[n]

print(f"Staircase with 2 steps. Ways to climb: {num_ways(2)}")
print(f"Staircase with 3 steps. Ways to climb: {num_ways(3)}")
print(f"Staircase with 4 steps. Ways to climb: {num_ways(4)}")
print(f"Staircase with 5 steps. Ways to climb: {num_ways(5)}")
print(f"Staircase with 10 steps. Ways to climb: {num_ways(10)}")
