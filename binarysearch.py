s = "aaaabbbccc"
count_a=0
count_b=0
count_c=0
for char in s:
    if(char == "a"):
        count_a+=1
        a1 = str(count_a)
    elif(char == "b"):
        count_b+=1
        b1 = str(count_b)
    elif(char=="c"):
        count_c+=1
        c1 = str(count_c)
        d = "a"+a1+"b"+b1+"c"+c1
print(d)
