import math
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
d=(b**2)-(4*a*c)
ans1=(-b-math.sqrt(d))/(2*a)
ans2=(-b+math.sqrt(d))/(2*a)
print('answers are',ans1,'and',ans2)
