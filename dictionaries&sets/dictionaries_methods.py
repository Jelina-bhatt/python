# Dictionary to begin with
student = {
    "name": "Jelina",
    "age": 20,
    "major": "Computer Engineering"
}

# get()
print("get():", student.get("name"))            # Jelina
print("get() with default:", student.get("grade", "N/A"))  # N/A

# keys()
print("keys():", student.keys())                # dict_keys(['name', 'age', 'major'])

# values()
print("values():", student.values())            # dict_values(['Jelina', 20, 'Computer Engineering'])

# items()
print("items():", student.items())              # dict_items([('name', 'Jelina'), ('age', 20), ('major', 'Computer Engineering')])

# update()
student.update({"grade": "A"})
print("After update():", student)               # {'name': ..., 'age': ..., 'major': ..., 'grade': 'A'}

# pop()
student.pop("age")
print("After pop('age'):", student)             # 'age' removed

# popitem()
student.popitem()
print("After popitem():", student)              # removes the last inserted item

# setdefault()
student.setdefault("university", "FWU")
print("After setdefault():", student)           # Adds university key if not present

# copy()
student_copy = student.copy()
print("Copy of dictionary:", student_copy)

# clear()
student.clear()
print("After clear():", student)                # {}
