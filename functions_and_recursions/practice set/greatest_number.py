def greatest(a,b,c):
    if(a>b and a>c):
         print(f"the greatest is {a}")
    elif(b>a and b>c):
           print(f"the greatest is {b}")
    elif(c>a and c>b):
        print(f"the greatest is {c}")

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
greatest(a,b,c)