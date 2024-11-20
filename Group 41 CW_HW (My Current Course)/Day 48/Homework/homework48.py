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

# https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/python

#ამ Kata-ს აქვს პრობლემები, ერრორებს არ აჩვენებს სწორად. ნახევრად დასრულებული: 

def triangular(n):
    sum = 0
    n = n + 1
    if n < 0:
        return 0
    else:
        for i in range(n):
            n = n - 1
            sum = sum + n
    return sum

#https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return False
    else:
        return True
    
# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(human_years):
    list = [0 , 0 , 0]
    list[0] = human_years
    for i in range(human_years):
        human_years = human_years - 1
        if human_years > 2:
            list[1] = list[1] + 5
        elif human_years == 2:
            list[1] = list[1] + 9
        elif human_years == 1:
            list[1] = list[1] + 15
    for i in range(human_years):
        human_years = human_years - 1
        if human_years > 2:
            list[2] = list[2] + 4
        elif human_years == 2:
            list[2] = list[2] + 9
        elif human_years == 1:
            list[2] = list[2] + 15
    return list  #ესეც დაუსრულებელია გაუგებრობის გამო. 
            
print(human_years_cat_years_dog_years(5))