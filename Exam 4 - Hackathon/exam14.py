# Task 14: Find Missing Number in an Array
# Instructions:
# Write a function find_missing_number(nums, n) that finds the missing number in an array containing numbers from 1 to n.
# The array contains n-1 distinct numbers (one number is missing).
# Test Cases:
# assert find_missing_number([3, 7, 1, 2, 8, 4, 5], 8) == 6
# assert find_missing_number([1, 2, 3, 5], 5) == 4
# assert find_missing_number([2, 3, 4], 4) == 1
# assert find_missing_number([1], 2) == 2


def find_missing_number(nums, n):
    nums.sort()
    for i in range(1, n + 1):
        if nums[i] != i + 1:
            return i + 1
print(find_missing_number([3, 7, 1, 2, 8, 4, 5], 8))

print(find_missing_number([1, 2, 3, 5], 5))