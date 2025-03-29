# Task 4: Check if a Number is Positive, Negative, or Zero
# Instructions:
# Write a function number_type(n) that returns:
# "Positive" if n > 0
# "Negative" if n < 0
# "Zero" if n == 0
# Test Cases:
# assert number_type(10) == "Positive"
# assert number_type(-5) == "Negative"
# assert number_type(0) == "Zero"

def number_type(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"
    
print(number_type(-5)) 