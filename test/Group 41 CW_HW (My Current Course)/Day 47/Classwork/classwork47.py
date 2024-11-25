# 1. სიტყვის რიცხვი ტექსტში
# შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და გამოითვლის, რამდენი სიტყვაა ამ ტექსტში.

def word_count(string):
        return string.count(" ") + 1
print(word_count("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"))

# 2. პირობითი ოპერაცია რიცხვის დადებითობის შემოწმებისთვის
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

# 3. მომხმარებლის ასაკის კატეგორიზაცია
# შექმენი პროგრამა, რომელიც მიიღებს მომხმარებლის ასაკს და დააბრუნებს შეტყობინებას იმის მიხედვით, თუ რომელ ასაკობრივ კატეგორიაშია მომხმარებელი.

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