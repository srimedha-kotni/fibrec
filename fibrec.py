n=int(input("enter a number:"))
def fib(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(n,"th term of fibonacci series is",fib(n))
