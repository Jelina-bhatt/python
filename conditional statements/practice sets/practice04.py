"""wap to find whether a given username contains 10 character or not"""

username=input("enter your username:")

if(len(username)<10):
    print("your username contains less than 10 character.")

elif(len(username)==10):
    print("your username contains exactly 10 character.")      

else:
    print("your username contains more than 10 character.")    