animals = ["dog", "cat", "cow", "kitten", "dog", "cat", "cow", "kitten"]
print(animals[0:7:3])  #1 - ადგილი საიდანაც იწყება ჭრა, 4 - სადაც სრულდება ჭრა, 2 - ყოველი ელემენტის მერე 2 ელემენტის გამოტოვება. 

colors = ['red', 'green', 'blue', 'yellow']
print(colors[1:3]) #ჭრისას მითითებული პირველი ელემენტი იქნება უკვე ამოჭრილ სიაში, თუმცა ბოლო ელემენტი არა. 


#შექმენით 10 მთელი რიცხვების სია, რიცხვები, 1-დან 10-მდე.

integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#1. დაჭერით სია, რომ მიიღოთ პირველი 5 ელემენტი და დაბეჭდეთ ისინი.

print(integers[0:5])

#2. დაჭერით სია ბოლო 3 ელემენტის მისაღებად და დაბეჭდეთ ისინი.

print(integers[7:10])

#3. დაჭერით სია, რომ მიიღოთ ყოველი მეორე ელემენტი სიიდან და დაბეჭდეთ იგი.

print(integers[0:9:2])




#შექმენით 6 სტრიქონის სია, რომლებიც წარმოადგენენ სხვადასხვა ხილს: ['ვაშლი', 'ბანანი', 'ალუბალი', 'თარიღი', 'ლეღვი', 'ყურძენი']. 

ხილი = ['ვაშლი', 'ბანანი', 'ალუბალი', 'თარიღი', 'ლეღვი', 'ყურძენი']

# შეცვალეთ სია ჭრის გამოყენებით და ამობეჭდეთ შებრუნებული სია.

print(ხილი[6:0:-1]) #როცა step ჩავა 0 - მდე ის აღარ გამოაკლებს 1-ს და ბოლო ელემენტიც არ დაიბეჭდება. 

print(ხილი[::-1]) #ამით პითონი სტანდარტულად უთითებს start-end-ს, ხოლო step - 1 ით სია დაიბეჭდება მარჯვნიდან მარცხნივ.

# შეცვალეთ შუა ორი ხილი ['კივი', 'ცაცხვი'] სიის ჭრის გამოყენებით და დაბეჭდეთ განახლებული სია.

ხილი[2:4] = ["კივი", "ცაცხვი"]
print(ხილი)
