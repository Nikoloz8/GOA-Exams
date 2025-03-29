# Task 13: Count Word Frequency in a String
# Instructions:
# Write a function word_frequency(text) that takes a string and returns a dictionary with words as keys and their frequency as values. The function should:
# Accept a string as input.
# Ignore punctuation and case.
# Return a dictionary with word counts.
# Test Cases:
# assert word_frequency("Hello world hello") == {"hello": 2, "world": 1}
# assert word_frequency("Python is great, and Python is fun!") == {"python": 2, "is": 2, "great": 1, "and": 1, "fun": 1}


# არვიცი dictionary

def word_frequency(text):
    text = text.lower()
    list1 = text.split(" ")
    dict1 = {}
    for i in range(len(list1)):
        dict1[list1[i]] = list1.count(list1[i])

    return dict1
    
print(word_frequency("Hello world hello"))

