def sum(a,b):
    return a+b
def difference(a,b):
    return a-b
def product(a,b):
    return a*b
def quotient(a,b):
    return a/b

n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
print("Sum of {} and {} is {}".format(n1,n2,sum(n1,n2)))
print("Difference of {} and {} is {}".format(n1,n2,difference(n1,n2)))
print("Product of {} and {} is {}".format(n1,n2,product(n1,n2)))
print("quotient of {} and {} is {}".format(n1,n2,quotient(n1,n2)))
