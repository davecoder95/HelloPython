
# ==========================================
# 1. Create a String
# ==========================================

"""
len()          → length
.upper()       → uppercase
.lower()       → lowercase
.strip()       → remove spaces
.replace()     → replace text
.find()        → find text
.split()       → string → list
.join()        → list → string
.startswith()  → check beginning
.endswith()    → check ending
"""

name = "John Smith"

print(name)

# Output:
# John Smith


# ==========================================
# 2. String Length
# ==========================================

name = "John Smith"

print(len(name))

# Output:
# 10


# ==========================================
# 3. Convert Uppercase / Lowercase
# ==========================================

text = "Hello World"

print(text.upper())
print(text.lower())

# Output:
# HELLO WORLD
# hello world


# ==========================================
# 4. Capitalize
# ==========================================

text = "hello world"

print(text.capitalize())
print(text.title())

# Output:
# Hello world
# Hello World


# ==========================================
# 5. Remove Spaces
# ==========================================

text = "   Hello World   "

print(text.strip())

# Output:
# Hello World


# ==========================================
# 6. Replace Text
# ==========================================

text = "I like Java"

text = text.replace("Java", "Python")

print(text)

# Output:
# I like Python


# ==========================================
# 7. Check if Text Exists
# ==========================================

text = "I am learning Python"

print("Python" in text)
print("Java" in text)

# Output:
# True
# False


# ==========================================
# 8. Find Text
# ==========================================

text = "Hello Python"

print(text.find("Python"))
print(text.find("Java"))

# Output:
# 6
# -1


# ==========================================
# 9. String Index
# ==========================================

text = "Python"

print(text[0])
print(text[1])
print(text[5])

# Output:
# P
# y
# n


# ==========================================
# 10. Negative Index
# ==========================================

text = "Python"

print(text[-1])
print(text[-2])

# Output:
# n
# o


# ==========================================
# 11. String Slicing
# ==========================================

text = "Python"

print(text[0:3])
print(text[2:6])

# Output:
# Pyt
# thon


# ==========================================
# 12. Reverse a String
# ==========================================

text = "Python"

print(text[::-1])

# Output:
# nohtyP


# ==========================================
# 13. Split a String
# ==========================================

text = "John,Mary,Bob"

names = text.split(",")

print(names)

# Output:
# ['John', 'Mary', 'Bob']


# ==========================================
# 14. Join Strings
# ==========================================

names = ["John", "Mary", "Bob"]

result = ", ".join(names)

print(result)

# Output:
# John, Mary, Bob


# ==========================================
# 15. Check Start / End
# ==========================================

text = "Hello Python"

print(text.startswith("Hello"))
print(text.endswith("Python"))

# Output:
# True
# True


# ==========================================
# 16. Count Characters
# ==========================================

text = "banana"

print(text.count("a"))
print(text.count("n"))

# Output:
# 3
# 2


# ==========================================
# 17. String Formatting
# ==========================================

name = "John"
age = 30

print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is John and I am 30 years old.


# ==========================================
# 18. Loop Through a String
# ==========================================

text = "Python"

for letter in text:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n


# ==========================================
# 19. Count Vowels
# ==========================================

text = "Hello World"

count = 0

for letter in text.lower():
    if letter in "aeiou":
        count = count + 1

print("Vowels:", count)

# Output:
# Vowels: 3