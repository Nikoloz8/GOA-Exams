#Codewars solutions

# https://www.codewars.com/kata/555a67db74814aa4ee0001b5

def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False
    
#https://www.codewars.com/kata/5ce9c1000bab0b001134f5af

def quarter_of(month):
    if 0 < month <= 3:
        return 1
    elif 3 < month <= 6:
        return 2 
    elif 6 < month <= 9:
        return 3 
    else:
        return 4

# https://www.codewars.com/kata/55cbd4ba903825f7970000f5

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
    
# https://www.codewars.com/kata/53369039d7ab3ac506000467

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
# https://www.codewars.com/kata/56dec885c54a926dcd001095

def opposite(number):
    return number * -1 

# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python

def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"
    
# https://www.codewars.com/kata/55685cd7ad70877c23000102

def make_negative( number ):
    if number > 0:
        return number * -1 
    else:
        return number