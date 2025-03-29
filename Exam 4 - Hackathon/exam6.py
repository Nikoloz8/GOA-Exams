# Task 6: Count Vowels in a String
# Instructions:
# Write a function count_vowelsads(s) that takes a string and returns the number of vowels (a, e, i, o, u, both uppercase and lowercase) in it. The function should:
# Accept a string as input.
# Ignore case when counting vowels.
# Test Cases:
# assert count_vowels("hello") == 2 
# assert count_vowels("AEIOU") == 5 
# assert count_vowels("Python") == 1 
# assert count_vowels("bcd") == 0 
# assert count_vowels("The Quick Brown Fox") == 5


def count_vowels(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "u" or s[i] == "o":
            count += 1
    return count

print(count_vowels("hello"))

