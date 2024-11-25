    # https://www.codewars.com/kata/583710ccaa6717322c000105/train/python

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
    # https://www.codewars.com/kata/57089707fe2d01529f00024a/train/python

def check_alive(health):
    if health > 0:
        return True
    else:
        return False
    
    # https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/python

def triangular(n):
    sum = 0
    n = n + 1
    for i in range(n):
        n = n - 1
        sum = sum + n
    return sum

# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

def positive_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            sum = sum + arr[i]
    return sum