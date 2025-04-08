#wap to accept marks of 7 students and display them in a sorted manner

marks=[]
f1=int(input("enter marks here:"))
marks.append(f1)
f2=int(input("enter marks here:"))
marks.append(f2)
f3=int(input("enter marks here:"))
marks.append(f3)
f4=int(input("enter marks here:"))
marks.append(f4)
f5=int(input("enter marks here:"))
marks.append(f5)
f6=int(input("enter marks here:"))
marks.append(f6)
f7=int(input("enter marks here:"))
marks.append(f7)

marks.sort()
print(marks)