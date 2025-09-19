# sum of natural numbers

def natural_sum(n):
  if (n==1):
    return 1
  return n + natural_sum(n-1)

n= int(input("enter a number"))
print(f"the natural sum is {natural_sum(n)}")