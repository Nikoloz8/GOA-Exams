# 1)შემქნით ფუნცქცია რომელიც არგუმენტად მიიღებს ინტეჯერს, ამ ფუნქციის დავალებაა რომ აიღოს ეს ინტეჯერი და დაგვიბრუნოს გაორმაგებული

def  double(integer):
    return integer*2 
print(double(5))

# 2)დაწერე ფუნქცია greet(name), რომელიც იღებს ადამიანის სახელს და აბრუნებს მისალმების ტექსტს

def greet(name):
    return "Hello " + name
print(greet("Nikoloz"))

# 3)შექმენით ფუნქცია is_even(num), რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი, თუ ლუწია, აბრუნებს True, სხვა შემთხვევაში False.

def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even(5))

# 4)შექმენით მარტივი ფუნქცია თქვენი სურვილით რომელსაც მისცემთ default valueს

def  double(integer):
    return integer / 2 
print(double(5))

# 5)შექმენით ფუნქცია nickname(name), რომელიც არგუმენტად იღებს სახელს და აბრუნებს პირველი სამი ასო(გამოიყენეთ slicingი)

def nickname(name):
    return name[0:3]
print(nickname("Nika"))