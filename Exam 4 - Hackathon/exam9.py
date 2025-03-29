# Task 9: Factorial Calculation
# Instructions:
# Write a function factorial(n) that takes a non-negative integer and returns its factorial. The function should:
# Accept an integer as input.
# Return the factorial of the number.
# Handle the case where n = 0, which has a factorial of 1.
# Test Cases:
# assert factorial(0) == 1 
# assert factorial(1) == 1 
# assert factorial(5) == 120 
# assert factorial(7) == 5040 
# assert factorial(3) == 6

def factorial(n):
    num = 1
    for i in range(n):
        num *= i + 1
    return num
print(factorial(5))
