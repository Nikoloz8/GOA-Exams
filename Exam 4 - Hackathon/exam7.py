# Task 7: Reverse a String
# Instructions:
# Write a function reverse_string(s) that takes a string and returns its reverse. The function should:
# Accept a string as input.
# Return the reversed string.
# Test Cases:
# assert reverse_string("hello") == "olleh" 
# assert reverse_string("Python") == "nohtyP" 
# assert reverse_string("") == "" 
# assert reverse_string("a") == "a" 
# assert reverse_string("racecar") == "racecar"

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))