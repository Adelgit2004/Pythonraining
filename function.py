
#def countdown(k,t=-0):

    #count =0
    #if(k%2==0):
        #print(k,end="")
    #if(k>2):
        #return countdown(k,t+2) #
#countdown(int(input('Enter the nbr')))

# def countdown(k, o=None):
#     if(o==None):
#         o = k
#     print(k,end = "")
#     if(k>1):
#         return countdown(k-1,o)
#     else:
#         return countdown(k+1,o)
# countdown(int(input("Enter the nbr")))
# def fun(n):
#     if(n==0):
#         return
#     print(n)
#     return fun(n-1)
# fun(int(input("Enter the nbr")))

# def func(n):
#     if(n==0):
#         return
#     elif(n%2==0):
#         print(n)
#         return func(n-2)
#     else:
#         return 0
# func(int(input("Enter the input ")))
# def func(n):
#     if(n==0):
#         return
#     elif(n%2==0):
#         print(n)
#         return func(n-2)
#     else:
#         return 0
# func(int(input("Enter the input ")))
# def funcn(n):
#     if(n==0):
#         return
#     funcn(n-1)
#     print(n,end ="")
# funcn(int(input("Enter the nbr")))
# def fync(n):
#     if(n==0):
#         return
#     print(n,end=" ")
#     fync(n-1)
# fync(int(input("Enter the nbr")))

# def funct(n):
#     if(n==0):
#         return 200
#     t = funct(n-1)
#     print(n ,end = ' ')
#     return t
# n= 5
# print(funct(n))

# def fun(n):
#     if n == 0:
#         return
#     print(n,end=" ")
#     fun(n - 1)
#     print(n,end=" ")
#
# fun(3)
def func(n):
    if(n==0):
        return
    func(n-1)
    print(n, end=" ")
func(5)