#1)მომხმარებელს შემოატანინე თავისი სახელი, შემდეგ შემატანინეთ მეგობრის გვარი და დაბეჭდეთ ისინი კონკატინაციის მეშვეობით.

username = input("My name is ")
friends_last_name = input("My friend's last name is ")
print(username + " " + friends_last_name)

#2)მომხმარებელს შემოატანინეთ მისი ასაკი და დაუბეჭდეთ რამდენი წლის იქნება 10 წელში.

user_age = int(input("My age is "))
print("My age in ten years will be" , user_age + 10)

#3)მომხმარებელს შემოატანინეთ 5 რიცხვი და დაითვალეთ ამ რიცხვების საშუალო არითმეტიკული.

print("Say five random numbers")
first_random_number = int(input("First: "))
second_random_number = int(input("Second: "))
third_random_number = int(input("Third: "))
fourth_random_number = int(input("Fourth: "))
fifth_random_number = int(input("Fifth: "))
print("Arithmetic mean of this numbers is" , first_random_number + second_random_number + third_random_number + fourth_random_number + fifth_random_number / 5)

#4)კომენტარის სახით ახსენით რა არის Case Sensitive + რა არის Snake Case.

#Case Sensitive ნიშნავს იმას, რომ დიდი და პატარა ასოები სხვადასხვა სიმბოლოებად ითვლება.
#Snake Case არის ტექსტის წერის სტილი, სადაც ყველა სიტყვა იწერება პატარა ასოთი და ერთმანეთისგან დაშორება გამოიხატება ქვედატირეებით.

#5)დაუშვით 5 შეცდომა და გვერდით კომენტარის სახით მიუწერეთ სწორი ვერსია (ახსენით რა არის Debugging)

# print("hello world)      
# # print("hello world")

# my variable = 21 
# #my_variable = 21

# my_name -> Nika
# #my_name = Nika

# print('quotes")
# #print("quotes") or print('quotes')

# print(5 ++ 5)
# #print(5 + 5)

#Debugging არის პროცესი, რომელიც მოიცავს კოდში არსებული შეცდომების პოვნასა და მათ აღმოფხვრას. 