def factorial(n):
    if (n==1 or n==0):
        return 1
    return n*factorial(n-1)


n=int(input("enter a number"))
print(f"the factorial of this number is:{factorial(n)}")