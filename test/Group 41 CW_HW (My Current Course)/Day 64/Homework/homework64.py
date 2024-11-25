#codewars solutions!

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

#https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

def reverse_words(s):
    splited_s = s.split()
    splited_s.reverse()
    reversed_s = ""
    for i in range(len(splited_s)):
        if i > 0:
            reversed_s = reversed_s + " " + splited_s[i]
        if i == 0:
            reversed_s = reversed_s + splited_s[i]
    return reversed_s

#https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return False
    else:
        return True
    