def items(n):
    a=200*(n-1)
    return a
b=int(input("enter the number:"))
if(b<=0):
    print("invalid input")
else:
    print("no of items:",b)
    print("shipping charge:",items(b)+750)
