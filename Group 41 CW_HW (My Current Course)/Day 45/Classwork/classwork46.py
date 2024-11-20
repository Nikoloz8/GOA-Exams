#1

def printBill(customer_name):
    print(customer_name)
customer_name = input("Enter your name: ")
printBill(customer_name)

#2

def welcome(name):
    print(f"Welcome {name}")

#3

def area(x, y):
    return x * y
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

#4 

def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res
