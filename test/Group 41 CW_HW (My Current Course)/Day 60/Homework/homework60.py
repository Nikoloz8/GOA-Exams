#codewars solutions 

#1 https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

def reverse_seq(n):
    list = []
    n = n + 1
    for i in range(n):
        n = n - 1
        if n != 0:
            list.append(n)
    return list

#2 https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

def grow(arr):
    result = 1
    for i in arr:
        result = result * i
    return result

#3 https://www.codewars.com/kata/54edbc7200b811e956000556/train/python

def count_sheeps(sheep):
    sum = 0
    count = []
    for i in range(len(sheep)):
        if sheep[i] == True:
            count.append(sheep)
    return len(count)

#4 https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    string = string.upper()  # Convert to uppercase to ignore case
    return len(set(string)) == len(string)

#5 https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

def get_middle(s):
    middle1 = ""
    middle2 = ""
    if len(s) % 2 == 0:
        middle1 = s[len(s) // 2 - 1]
        middle2 = s[(len(s) // 2)]
        return middle1 + middle2
    else:
        return s[len(s) // 2]
    
    