num=input("enter the number:")
def reverse(num):
    number=""
    for i in num:
        number=i+number
    return number
print("the given number is:",num)
print("tne reverse number is:",reverse(num))
