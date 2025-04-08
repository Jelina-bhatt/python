""" Take input from the user for 5 students' names and their scores.

Store the student names and scores as a list of tuples, where each tuple contains (name, score).

Sort the list in descending order based on score.

Print the top 3 students."""





students = []

for i in range(5):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    students.append((name, score))

# Sorting by score in descending order
students.sort(reverse=True, key=lambda x: x[1])

# Display top 3 students
print("\nTop 3 students:")
for i in range(3):
    name, score = students[i]
    print(f"{i+1}. {name} - {score}")
