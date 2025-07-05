 # 4!= 1*2*3*4
 
n=int(input("enter the number:"))
product =1
for i in range(1, n+1):
    product=product*i



print(f"the factorial of {n} is {product}")