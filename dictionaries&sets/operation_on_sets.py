s = {1, 2, 3, 4}

print(len(s))    # ➤ 4 (total elements)

s.remove(4)      # ➤ Removes element 4
print(s)         # ➤ {1, 2, 3}

s.pop()          # ➤ Removes a random element (since sets are unordered)
print(s)         # ➤ One element removed

s.clear()        # ➤ Empties the set
print(s)         # ➤ set()
