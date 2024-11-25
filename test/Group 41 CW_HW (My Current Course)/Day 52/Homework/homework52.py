#Codewars solutions

#https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

#https://www.codewars.com/kata/59f11118a5e129e591000134/train/python

def repeats(arr):
    list = []
    sum = 0
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            list.append(arr[i])
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

#https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python

def area_or_perimeter(l, w):
    if l == w:
        return l * w  
    else:
        return 2 * (l + w)
    
#რომელიღაც 2 კატის ლინკს ჰქონდა პრობლემა.