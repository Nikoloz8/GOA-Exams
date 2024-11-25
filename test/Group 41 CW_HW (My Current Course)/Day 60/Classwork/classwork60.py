#codewars solutions

#1 https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

def grow(arr):
    result = 1
    for i in arr:
        result = result * i
    return result

#2 https://www.codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    binary = ""
    for i in range(len(x)):
        if int((x[i])) < 5:
            binary = binary + "0"
        else:
            binary = binary + "1"
    return binary

#3 https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python

def hero(bullets, dragons):
    if dragons * 2 <= bullets:
        return True 
    elif dragons * 2 > bullets:
        return False
