def factorial(n):
    if(n==1):
        return n
    else:
        return (n*factorial(n-1))
n=float(input("enter the given value:"))
if(n<0):
    print("enter the positive value")
elif(n==0):
    print("the factorial of 0 is 1")
else:
    print("factorial value is:",factorial(n))
