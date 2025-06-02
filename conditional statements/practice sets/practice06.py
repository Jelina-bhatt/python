"""wap to calculate grade of a student
 from his marks from the given scheme"""

marks = int(input("enter your marks:"))

if(marks<=100 and marks>=90):
    grade ="Ex"


elif(marks<=90 and marks>=80):
    grade="A"


elif(marks<=80 and marks>=70):
    grade="B"


elif(marks<=700 and marks>=60):
    grade="F"



print(grade)