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

numbers.append(100) #გამოიყენება ლისთში ელემენტების ჩასამატებლად(ბოლოში)

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

# # 4)Classwork 3: Slicing and List Comprehensions

# 1. Create a list named numbers that contains the integers from 1 to 10.

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Use list slicing to create a new list named first_half that contains the first five elements from numbers.

first_half = integers[0:5]

# 3. Use list slicing to create another list named second_half that contains the last five elements from numbers.

second_half = integers[5:11]

# 4. Use a list comprehension to create a new list named squares that contains the squares of each number in the numbers list.

squares = [i**2 for i in numbers] #[მოქმედება რაც გვინდა შევასრულოთ თითოეულ ელემენტზე, for, საიტერაციო ცვლადი, in და სია რომელზეც გვინდა მოქმედების შესრულება.]


# 5. Print all three lists: first_half, second_half, and squares.

print(first_half, second_half, squares)

# # 5) Classwork 5: List Manipulation and Aggregation

# 1. Create a list named temperatures that contains the following values representing daily temperatures: [72, 68, 75, 70, 78, 74, 71].

temperatures = [72, 68, 75, 70, 78, 74, 71]

# 2. Calculate and print the highest temperature using the max() function.

print(max(temperatures))  #ფუნქცია გამოიყენება სიიდან მნიშვნელობით ყველაზე მაღალი ელემენტის ამოსაღებად.

# 3. Calculate and print the lowest temperature using the min() function.

print(min(temperatures)) #ფუნქცია გამოიყენება სიიდან მნიშვნელობით ყველაზე დაბალი ელემენტის ამოსაღებად.

# 4. Calculate and print the average temperature using the sum() function divided by the length of the list.

print(sum(temperatures)) #ფუნქცია აჯამებს სიაში მყოფ ელემენტებს.

print(sum(temperatures) / len(temperatures))

# 5. Use a list comprehension to create a new list named above_70 that contains only the temperatures above 70 degrees.

above_70 = [temp for temp in temperatures if temp > 70]

# 6. Print the above_70 list.

print(above_70)