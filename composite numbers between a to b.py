a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
if(a>b or a==0 or b==0):
    print("invalid input")
elif(a>0 or b<0):
     print("Composite number from",a,"to",b)
for i in range(a+2,b):
    for j in range(2,a):
        if(i%j==0):
            print(i)
            break
else:
    print(i)
