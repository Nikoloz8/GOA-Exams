# ==

# განსაზღვრეთ ფუნქცია სახელწოდებით simple_calculator, რომელიც იღებს სამ არგუმენტს:

# num1: პირველი რიცხვი (მთლიანი ან float).
# num2: მეორე რიცხვი (მთლიანი ან float).

# ოპერაცია: სტრიქონი, რომელიც განსაზღვრავს შესასრულებლად ოპერაციას. ის შეიძლება იყოს „დამატება“, „გამოკლება“, „გამრავლება“ ან „გაყოფა“.
# ფუნქციის შიგნით,

# გამოიყენეთ if და elif განცხადებები, რათა დაადგინოთ რომელი ოპერაცია უნდა შეასრულოთ ოპერაციის არგუმენტის მნიშვნელობიდან გამომდინარე.

# ფუნქციამ უნდა დააბრუნოს ოპერაციის შედეგი.

# თუ ოპერაცია არის „გაყოფა“ და num2 არის 0, ფუნქციამ უნდა დააბრუნოს „შეცდომა: ნულზე გაყოფა შეუძლებელია“.
# ჩაწერეთ კოდი, რომ გამოიძახოთ ფუნქცია სხვადასხვა ოპერაციებით და დაბეჭდოთ შედეგები.

num1 = int(input("Enter value1 for calculation: "))
operator = input("Enter operator: ")
num2 = int(input("Enter value2 for calculation: "))

def simply_calculator(num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif:
             if num2 == 0:
                  return "Error: Divide on 0 is impossible!"
             else:
                return num1 / num2
        else:
             return "Error!"
print(simply_calculator(num1, num2, operator))