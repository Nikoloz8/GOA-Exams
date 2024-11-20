# # Classwork 2: Basic List Operations
# Create a list named fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the entire list.

print(fruits)

# Access and print the first and last items in the list.

print(fruits[0], fruits[4])

# Add a new fruit "fig" to the list.

fruits.append("fig")

# Remove "banana" from the list.

fruits.remove("banana")

# Change the value of the second item to "blueberry".

fruits[1] = "blueberry"

# Print the length of the list.

print(len(fruits))




# # 3)Classwork 3: List Functions and Methods

# Create a list named numbers that contains the following integers: 10, 20, 30, 40, 50, 60, 70, 80, 90.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Use the append() function to add the number 100 to the end of the list.

numbers.append(100) #გამოიყენება ლისთში ელემენტების ჩასამაყებლად(ბოლოში)

# Use the insert() function to add the number 5 at the beginning of the list.

numbers.insert(1, 5)  #ესეც გამოიყენება ლისთში ელემენტების დასამატებლად, თუმცა ამ ფუნქციით შეგვიძლია ელემენტი დავამატოთ იმ ადგილას სადაც ჩვენ გვჭირდება. ჯერ ინდექსი, შემდეგ ელემენტი.

# Use the remove() function to remove the number 30 from the list.

numbers.remove(30) #გამოიყენება list იდან ელემენტების ამოსაღებად. 

# Use the sort() function to sort the list in ascending order.

numbers.sort() #გამოიყენება სიის დასალაგებლად, default-ად მაღლიდან დაბლა მიმდევრობით. 
 
# Use the reverse() function to reverse the order of the list.

numbers.reverse() #გამოიყენება სიის შემოსაბრუნებლად. 

# Use the index() function to find the index of the number 50.

numbers.index(50) #გამოიყენება კონკრეტული ელემენტის ინდექსის გასაგებად.

# Use the count() function to count how many times 20 appears in the list.

print(numbers.count(20)) #ეს ფუნქცია ითვლის იმას, თუ რამდენჯერ არის მოთავსებული სიაში ფუნქციის ფრჩხილებში მყოფი ელემენტი.