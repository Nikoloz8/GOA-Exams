# # Level 49:

# # 1. პროექტის აღწერა:
# პრობლემა: დაწერეთ პროგრამა, რომელიც ითვლის სტუდენტების ნიშნებს და განსაზღვრავს საუკეთესო სტუდენტს. მომხმარებელი შეიყვანს სტუდენტების სახელებსა და მათ ნიშანს, პროგრამა კი გამოთვლის საშუალო ნიშანს თითოეული სტუდენტისთვის და გამოაცხადებს საუკეთესოს.

def best_student(students, scores):
    students = []
    scores = []
    students_count = int(input("Please enter quantity of students: "))
    for i in range(students_count):
        students.append(input("Enter name of student: "))
        scores.append(int(input("Enter score of student: ")))
        max_score = max(scores)    
    return students[scores.index(max_score)] + " " + str(max_score)
(print(best_student([], []))) 

# # 2. პროექტის აღწერა:
# პრობლემა: შექმენით პროგრამა, რომელიც დაამუშავებს სტუდენტების ქულების სიას და მოიძებნის მაქსიმალურ, მინიმალურ და საშუალო ქულას.

def max_min_average():
    sum = 0
    scores = []
    students_count = int(input("Please enter quantity of students: "))
    for i in range(students_count):
        scores.append(int(input("Enter score of student: ")))
    for i in range(len(scores)):
        sum = sum + scores[i]
    max_score_count = max(scores)
    min_score_count = min(scores)
    average_score_count = sum / len(scores)
    max_score = str("Max score from this list is:" + " " + str(max_score_count))
    min_score= str("Minimum score from this list is:" + " " + str(min_score_count))
    average = str("Average of this scores is" + " " + str(average_score_count))
    return min_score, max_score, average
print(max_min_average())