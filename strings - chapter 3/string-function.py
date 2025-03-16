name="radhe Krishn  "

print(len(name))
print(name.endswith("shna"))
print(name.startswith("radhe"))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.find("radhe"))
print(name.strip())
print(name.split())

s = "  Python is awesome!  "

print(s.lower())     # '  python is awesome!  '
print(s.upper())     # '  PYTHON IS AWESOME!  '
print(s.strip())     # 'Python is awesome!' (removes whitespace)
print(s.replace("Python", "Java"))  # '  Java is awesome!  '
print(s.split())     # ['Python', 'is', 'awesome!'] (splits by space)
print(s.startswith("Py"))  # True
print(s.endswith("!"))     # True
print(s.find("is"))        # 9 (index of first occurrence)
