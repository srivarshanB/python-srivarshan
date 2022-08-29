import math as m
n=int(input("enter the value :"))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
if(temp==sum):
    print("the entered value is palindrome")
else:
    print("the entered value is not palindrome")
