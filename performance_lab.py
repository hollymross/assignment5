# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    count = {}

    for num in numbers:
        count[num] = count.get(num,0) + 1

    max = 0
    most_common = None

    for num, count in count.items():
        if count > max:
            max = count
            most_common = num
    
    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case:O(n)
- Average-case:O(n)
- Space complexity: O(n)
- Why this approach? This approach is the best because it avoids nested loops and used a dictionary for clean lookups
- Could it be optimized? No
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    dupe = set()
    numbers = []
    for num in nums:
        if num not in dupe:
            dupe.add(num)
            numbers.append(num)


    return numbers

print(remove_duplicates([4,5,4,6,5,7]))

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? This approach keeps the original order of the numbers that are put in and avoids any nested loops
- Could it be optimized? No
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)
    
    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? 
- Could it be optimized? No
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    pass

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
- What is the worst-case for a single append?
- What is the amortized time per append overall?
- Space complexity:
- Why does doubling reduce the cost overall?
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = []
    sum = 0

    for num in nums:
        sum = sum + num
        total.append(sum)
    
    return total

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
- Could it be optimized? No
"""
