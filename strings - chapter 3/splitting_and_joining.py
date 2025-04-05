text = "apple,banana,cherry"
words = text.split(",")  # Converts string to list
print(words)  # ['apple', 'banana', 'cherry']

new_text = "-".join(words)  
print(new_text)  # apple-banana-cherry


strings="good,bad,abnormal"
strings_split=strings.split(",")
new_strings="-".join(strings)