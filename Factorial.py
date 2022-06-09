a=int(input("enter a number to find factorial : "))
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result=fact(a)
print(result)
