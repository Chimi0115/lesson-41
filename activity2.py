def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    
num=int(input("Enter a number"))
if num<0:
    print("factorial does not exist for negative numbers")
elif num==0:
    print("factorial for 1 is 1")
else:
    print("factorail of",num," is ",fact(num))