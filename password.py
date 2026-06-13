upper ,lower,digit,special = 0,0,0,0
s = input()
if(len(s)<8):
    print("Invalid Password")
else:
    for ch in s:
        if(ch.isupper()):
            upper+=1
        elif(ch.islower()):
            lower+=1
        elif(ch.isdigit()):
            digit+=1
        else:
            special+=1
    if(digit and special and lower and upper):
        print("Valid")

