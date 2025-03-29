# Instructions:
# Write a function find_max(lst) that takes a list of numbers and returns the maximum value. The function should:
# Accept a list of numbers as input.
# Return the maximum number in the list.
# Test Cases:
# assert find_max([1, 2, 3, 4, 5]) == 5 
# assert find_max([-10, -5, -1]) == -1 
# assert find_max([100, 50, 75]) == 100 
# assert find_max([7]) == 7 
# assert find_max([0, 0, 0]) == 0


def find_max(lst):
    return max(lst)

print(find_max([1, 2, 3, 4, 5]))