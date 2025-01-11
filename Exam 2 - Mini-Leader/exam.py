#Reversed Words

def reverse_words(s):
    list = s.split()
    list.reverse()
    string = ""
    for i in range(len(list)):
        if i > 0:
            string = string + " " + list[i]
        else:
            string = string + list[i]
    return string


# Total amount of points

def points(games):
    string = ""
    sum = 0
    for i in range(len(games)):
        string = games[i]
        if string[0] > string[2]:
            sum = sum + 3
        elif string[0] > string[2]:
            sum = sum + 0
        elif string[0] == string[2]:
            sum = sum + 1
    return sum

