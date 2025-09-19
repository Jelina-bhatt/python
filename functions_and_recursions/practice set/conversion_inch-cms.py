# this program converts inches to centimeters

def inch_to_cms(inch):
    return inch*2.54


n= int(input("enter the values in inches:"))
print(f"the corresponding value in cms is :{inch_to_cms(n)}")