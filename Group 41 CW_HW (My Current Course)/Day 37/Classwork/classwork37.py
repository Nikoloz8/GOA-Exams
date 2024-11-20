# # 1. Task: Format a String

# Write a Python program that takes a user's name and age as input. Use the format() function to create a sentence that says, "Hello, [Name]! You are [Age] years old."

sentence = "Hello {name}! You are {age} years old."
formated_sentence = sentence.format(name = input("Enter your name: "), age = int(input("Enter your age: ")))
print(formated_sentence)

# # 2. Task: Join a List of Strings

# Given a list of words ["Python", "is", "fun"], use the join() function to combine them into a single string, separated by spaces. The result should be "Python is fun".

words = ["Python", "is", "fun"]
seperated_string = " ".join(words)
print(seperated_string)

# # 3. Task: Split a String

# Write a program that asks the user to input a sentence. Use the split() function to break the sentence into a list of words. Print the list of words.

input_sentence = input("Enter sentence: ")
input_sentence_splitted = input_sentence.split()
print(input_sentence_splitted)

# # 4. Task: Replace Substrings

# Create a program that asks the user for a sentence and a word to replace. Then, ask for the new word to replace it with. Use the replace() function to make the substitution and print the modified sentence.

input_sentence = input("Enter sentence: ")
replace_word = input("Enter the word which you want to replace: ")
replace_new_word = input("Enter new word: ")

replaced = input_sentence.replace(replace_word, replace_new_word)

print(replaced)

# # 5. Task: Convert to Lowercase

# Write a Python script that takes a mixed-case string and converts it entirely to lowercase using the lower() function.

mixed_string = "i LIkE PyThOn"
print(mixed_string.lower())

# # 6.Task: Convert to Uppercase

# Create a program that asks the user to input a sentence and then converts the entire sentence to uppercase using the upper() function.

mixed_string = "i LIkE PyThOn"
print(mixed_string.upper())
