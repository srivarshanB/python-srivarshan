print("enter -1 to exit:")
b=[]
(c,d,e,f)=(0,0,0,0)
for i in range(0,100):
    a=int(input("enter the element:"))
    if(a==-1):
        break
    else:
        b.append(a)
for i in b:
    if(i<=0):
        c+=i
        d+=i
    elif(i>0):
        e+=i
        f+=i
print("average of negative:",c/d)
print("average of positive:",e/f)
