#codewars solutions

# 1. https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
    
#https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

def summation(num):
    sum = 0
    num = num + 1
    for i in range(num):
        num = num - 1
        sum = sum + num
    return sum
    
#https://www.codewars.com/kata/541629460b198da04e000bb9/train/python

#ver mivxvdi

#https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python

def greet(language):
    if language == "english":
        return "Welcome"
    elif language == "czech":
        return "Vitejte"
    elif language == "danish":
        return "Velkomst"
    elif language == "dutch":
        return "Welkom"
    elif language == "estonian":
        return "Tere tulemast"
    elif language == "finnish":
        return "Tervetuloa"
    elif language == "flemish":
        return "Welgekomen"
    elif language == "french":
        return "Bienvenue"
    elif language == "german":
        return "Willkommen"
    elif language == "irish":
        return "Failte"
    elif language == "italian":
        return "Benvenuto"
    elif language == "latvian":
        return "Gaidits"
    elif language == "lithuanian":
        return "Laukiamas"
    elif language == "polish":
        return "Witamy"
    elif language == "spanish":
        return "Bienvenido"
    elif language == "swedish":
        return "Valkommen"
    elif language == "welsh":
        return "Croeso"
    else:
        return "Welcome"
    