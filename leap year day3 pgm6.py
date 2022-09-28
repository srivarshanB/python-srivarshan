try:
    year=int(input("enter the year"))
except:
    ValueError
    print("enter the proper value")
else:
    for i in range(0,5):
        if(year<=0):
            print("invalid")

        if(year%4==0 or year%400==0 and year%100!=0):
            print("it is a leap year",year)
    
        else:
            print("its not a leap year",year)
            year=year+1
            print("the next leap year s:",year)
print()
