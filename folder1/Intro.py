person = {
    "name": "Jelina",
    "age": 30,
    "city": "Kanchanpur"
}

print(person)

# Accessing elements
print(person["name"])
print(person.get("age"))

# Adding an element
person["email"] = "jelina@example.com"
print(person)

# Removing an element
del person["city"]
print(person)
