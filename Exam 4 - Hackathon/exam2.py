# Task 2: Check Even or Odd
# Instructions:
# Write a function is_even(n) that returns True if n is even, otherwise False.
# Test Cases:
# assert is_even(4) == True
# assert is_even(7) == False
# assert is_even(0) == True

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(4))