# # 2. ფუნქცია: რაოდენობის დათვლა

# 1. შექმენი ფუნქცია count_items(item_list, item), რომელიც მიიღებს ორ პარამეტრს:
# 2. item_list - ელემენტების სია.
# 3. item - ელემენტი, რომლის დათვლაც გსურს სიაში.
# 4. ფუნქციამ უნდა დააბრუნოს, რამდენჯერ გვხვდება ეს ელემენტი სიაში.

def count_items(item_list, item):
    return item_list.count(item)

# # 3. ფუნქცია: ჯამის გამოთვლა

# 1. შექმენი ფუნქცია sum_of_list(num_list), რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სიაში არსებული ყველა რიცხვის ჯამს.
# 2. ფუნქცია უნდა გამოიყენოს for ციკლი.

def sum_of_list(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum = sum + num_list[i]
    return sum

# # 4. ფუნქცია: საშუალო მნიშვნელობის გამოთვლა

# 1. შექმენი ფუნქცია average_of_list(num_list), რომელიც იღებს რიცხვების სიას და აბრუნებს ამ რიცხვების საშუალო მნიშვნელობას.
# 2. გამოიყენე სიის ჯამის გამოთვლა და ელემენტების რაოდენობის გაყოფა.

def average_of_list(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum = sum + num_list[i]
    return sum / len(num_list)

# # 5. ფუნქცია: სიის გადაბრუნება
# შექმენი ფუნქცია reverse_list(items), რომელიც დააბრუნებს გადაბრუნებულ სიას (სიის ბოლო ელემენტი პირველზე იქნება, პირველი კი ბოლო).

def reverse_list(items):
    items.reverse()
    return items