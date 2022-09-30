n=int(input("enter the string:"))
list=[]
for i in range(n):
    a=input("enter the elements of string:")
    list.append(a)
list1=sorted(list)
list2=sorted(list,reverse=True)
choice=input("enter your choice:")
if(choice=="a"):
    print("ascending",list1)
else:
    print("descending",list2)
