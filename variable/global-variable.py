#Variables that are created outside of a function are known as global variables

#Global variables can be used by everyone, both inside of functions and outside.
     
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
