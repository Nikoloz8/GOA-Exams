#Codewars solutions

#https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

def solution(string):
    right_string = ""
    counter = len(string)
    for i in range(len(string)):
        counter = counter - 1
        right_string = right_string + string[counter]
    return right_string

#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(st):
    string = ""
    for i in range(len(st) + 1):
        string = string + (st[i - 1] * i).capitalize()
        if i > 0 and i < len(st):
            string = string + "-"
        if i == i + 0:
            string + string + ""
            
    return string

# https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python

def paperwork(n, m):
    if n < 0:
        return 0
    elif m < 0:
        return 0
    else:
        return m * n
    
# https://www.codewars.com/kata/55d277882e139d0b6000005d/train/python

def find_average(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i] 
        average = sum / len(nums)
    return average
