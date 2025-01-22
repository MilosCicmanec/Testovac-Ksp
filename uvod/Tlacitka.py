def akc1(string):
    string = string + "ABD"
    return string
def akc2(string):
    string = string + "ACD"
    return string
def akc3(string):
    string = string + "ACCCCCD"
    return string
def akc4(string):
    string = string + "A"
    string = akc2(string)
    string = string + "D"
    return string
def akc5(string):
    string = string + "A"
    string = akc3(string)
    string = string + "C"
    for i in range(5):
        string = akc1(string)
    string = string + "D"
    return string
def akc6(string):
    string = string + "A"
    string = akc5(string)
    string = string + "C" 
    string = string + "BBBBB"
    for i in range(5):
        string = akc4(string)
    string = string + "D"
    return string

inp = int(input())
s = ""
if inp == 1:
    print(akc1(s))
elif inp == 2:
    print(akc2(s))
elif inp == 3:
    print(akc3(s))
elif inp == 4:
    print(akc4(s))
elif inp == 5:
    print(akc5(s))
elif inp == 6:
    print(akc6(s))
