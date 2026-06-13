def func(n):
    cnt_o=0
    cnt=0
    sum=0
    sum_o=0
    if(n == 0):
        return
    else:
        if(n%2!=0 ):
            print(n,"is odd")
            func(n - 1)
            cnt_o+=1
            if(n==1):
                print(n,"is odd")
        else:
            print(n,"is even")
            func(n//2)
            cnt+=1
        sum+=cnt
        sum_o+=cnt_o
        print(sum,sum_o)
func(int(input()))
