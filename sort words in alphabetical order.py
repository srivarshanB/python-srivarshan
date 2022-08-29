print("enter the given string :")
str=input()
words=str.split()
words.sort()
sortedwords=" "
for word in words:
    sortedwords=sortedwords+word+" "
print(sortedwords)
    
