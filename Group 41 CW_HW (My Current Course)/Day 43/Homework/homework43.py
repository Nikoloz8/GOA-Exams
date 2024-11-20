# # Task 2: String Formatting

# Create a string named template with the following content: "Hello, {name}. Welcome to {place}."

template = "Hello, {name}. Welcome to {place}."

# Use the format() function to replace {name} with "Alice" and {place} with "Wonderland". Store the result in a variable named formatted_string and print it.

formated_string = template.format(name="Alice", place="Wonderland") # {} - ეს არის ეგრედწოდებული სლოტი, რომელშიც შეიძლება ჩავსვათ სხადასხვა ელემენტი. format ფუნქცია გამოიყენება string-ების გასაუმჯობესებლად, რაც გამოიხატება "სლოტებში" ჩასმით.

#მეორე გზა:

name = "Alice"
place = "Wonderland"
template = f"Hello, {name}. Welcome to {place}."

print(formated_string)
print(template)

# # Task 3: Joining Strings

# Create a list named words that contains the following strings: "apple", "banana", "cherry".

# Use the join() function to combine these words into a single string, separated by a comma and a space ", ". Store the result in a variable named fruit_string and print it.

words = ["apple", "banana", "cherry"]

#join function use example:
# words = ["Hello", "world", "from", "Python"]
# sentence = " ".join(words)
# print(sentence)

fruit_string = " ".join(words)
print(fruit_string)

# # Task 4: Splitting a String

# Create a string named sentence with the following content: "The quick brown fox jumps over the lazy dog."

sentence = "The quick brown fox jumps over the lazy dog"

# Use the split() function to split the sentence into a list of words. Store the result in a variable named words_list and print it.

words_list = sentence.split() #split join-ის საწინააღმდეგოა. იგი გამოიყენება სტრინგის "დასაჭრელად".
print(words_list)

# # Task 5: Replacing Substrings

# Create a string named quote with the following content: "To be or not to be, that is the question."

quote = "To be or not to be, that is the question"
 
# Use the replace() function to replace the word "be" with "code". Store the result in a variable named modified_quote and print it.

modified_quote = quote.replace("be", "code") #ეს ფუნქცია გამოიყენება ელემენტების ჩასანაცვლებლად. არგუმენტად პირველი იწერება ელემენტი რომლის ჩანაცვლებაც გვინდა, ხოლო მეორე - რითიც ვანაცვლებთ. 
print(modified_quote)

# # Task 6: Converting to Lowercase

# Create a string named mixed_case with the following content: "PyThOn Is AwEsOmE!"

mixed_case = "PyThOn Is AwEsOmE!"

# Use the lower() function to convert the entire string to lowercase. Store the result in a variable named lowercase_string and print it.

lowercase_string = mixed_case.lower() #ფუნქცია გამოიყენება სტრინგში ყველა ასოს პატარა ასოებად ქცევისთვის. 
print(lowercase_string)

# # Task 7: Converting to Uppercase

# Create a string named greeting with the following content: "good morning"

greeting = "good morning"

# Use the upper() function to convert the entire string to uppercase. Store the result in a variable named uppercase_greeting and print it.

uppercase_greeting = greeting.upper() #ფუნქცია სტრინგში ყველა ასოს აქცევს დიდად. 
print(uppercase_greeting)