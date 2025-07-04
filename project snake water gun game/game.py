'''
1 is for snake
-1 is for water
0 is for gun
'''

computer =-1
youstr = input("enter your choice:")
youDict = {"s":1, "w":-1, "g":0}
you = youDict[youstr]



if(computer == you):
  print("its a draw")

else:
    if(computer ==-1 and you ==1):
       print("you win")
    
    elif(computer ==-1 and you ==0):
     print("you lose!")

    elif(computer ==1 and you ==-1):
        print("you lose")
    
    elif(computer ==1 and you ==0):
     print("you win!")
     
    elif(computer ==0 and you ==-1):
       print("you win")
    
    elif(computer ==0 and you ==1):
     print("you lose!")
     
    
    
    else:
     
     print("something went wrong!")
     


