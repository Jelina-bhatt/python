l1 = [1, 2, 4, 5, 8, 89, 42]

# Sort the list in ascending order
l1.sort()
print(l1)  # [1, 2, 4, 5, 8, 42, 89]

# Reverse the sorted list
l1.reverse()
print(l1)  # [89, 42, 8, 5, 4, 2, 1]

# Add "jelina" at the end of the list
l1.append("jelina")
print(l1)  # [89, 42, 8, 5, 4, 2, 1, 'jelina']

# Insert 4 at index 3
l1.insert(3, 4)
print(l1)  # [89, 42, 8, 4, 5, 4, 2, 1, 'jelina']

# Add 8 to the end of the list
l1.append(8)
print(l1)  # [..., 'jelina', 8]

# Remove the item at index 3
print(l1.pop(3))  # Output: 4 (item at index 3)
print(l1)  # List after popping index 3

# Remove the string "jelina" from the list
l1.remove("jelina")
print(l1)

# ❌ This line has a bug:
# l1.extend("jelina", "bhatt") → ❌ Invalid, too many arguments

# ✅ FIX:
l1.extend(["jelina", "bhatt"])  # Use a list with two strings
print(l1)

l1.clear() #clears everything
print(l1)