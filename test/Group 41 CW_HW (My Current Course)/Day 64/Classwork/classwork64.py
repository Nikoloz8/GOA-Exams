#codewars solutions! 

#https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python

def say_hello(name):
    return "Hello, " + name

#https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python

def array_plus_array(arr1,arr2):
    sum = 0
    for i in range(len(arr1)):
        sum = sum + arr1[i]
    for i in range(len(arr2)):
        sum = sum + arr2[i]
    return sum

#https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python

def monkey_count(n):
    list = []
    n = n + 1
    for i in range(n):
            n = n - 1
            if n > 0:
                list.append(n)
            list.sort()
    return list

#https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

def reverse_seq(n):
    list = []
    n = n + 1
    for i in range(n):
        n = n - 1
        if n != 0:
            list.append(n)
    return list

