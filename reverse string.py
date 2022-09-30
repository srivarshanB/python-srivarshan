str=input("enter the string:")
def reverse(str):
    string="   "
    for i in str:
        string=i+string
    return string
print("the given string is:",str)
print("the reverse string is:",reverse(str))


