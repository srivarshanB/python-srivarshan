def fib(n):
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)
s=int(input("Enter n value:"))
print("output:",fib(s+1))
