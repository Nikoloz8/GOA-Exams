# Level 47:

# # 1. სიტყვის რიცხვი ტექსტში
# შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და გამოითვლის, რამდენი სიტყვაა ამ ტექსტში.

def word_count(string):
        return string.count(" ") + 1
print(word_count("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"))

# # 2.  პირობითი ოპერაცია რიცხვის დადებითობის შემოწმებისთვის
# შექმენი პროგრამა, რომელიც იფუნქციონირებს შემდეგნაირად: მომხმარებლის შეყვანილი რიცხვი იქნება დადებითი, უარყოფითი, ან ნულოვანი, და შესაბამისი შეტყობინება უნდა გამოიტანოს.

def negative_zero_positive(x):
    if x > 0:
        return "Positive"
    elif x == 0:
        return "Zero"
    else:
        return "Negative"
x = int(input("Enter number: "))
print(negative_zero_positive(x))

# # 3. მომხმარებლის ასაკის კატეგორიზაცია
#  შექმენი პროგრამა, რომელიც მიიღებს მომხმარებლის ასაკს და დააბრუნებს შეტყობინებას იმის მიხედვით, თუ რომელ ასაკობრივ კატეგორიაშია მომხმარებელი.

def user_age(age):
    if 0 < age < 12:
          return "You are kid"
    elif 18 > age > 12:
         return "You are teenager"
    elif age > 18:
         return "You are adult"
    elif age < 0:
         return "You are not even born"
    else:
         return "Error"
age = int(input("Enter your age: "))
print(user_age(age))
     

# # 4.  ლუწი და კენტ რიცხვთა სიის პოვნა
# შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ორ ცალკე სიას – ერთში იქნებიან ლუწი რიცხვები, ხოლო მეორეში კენტი რიცხვები.

def odd_even_list(numbers):
    odds = []
    evens = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
        else:
            odds.append(numbers[i])
    return odds, evens
print(odd_even_list([1, 4, 7, 1, 9 ,2, 14, 57, 69, 22]))

# # 5. საშუალო რიცხვის პოვნა ფუნქციით
# შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სიის საშუალო რიცხვს.

def average(numbers_list):
    sum = 0
    for i in range(len(numbers_list)):
        sum = sum + numbers_list[i]
    return sum / len(numbers_list)
print(average([5, 8, 26, 69]))