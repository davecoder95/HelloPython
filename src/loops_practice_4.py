
# ==========================================
# 7. Nested For Loops
# ==========================================

for row in range(1, 4):
    for column in range(1, 4):
        print("Row:", row, "Column:", column)

# Output:
# Row: 1 Column: 1
# Row: 1 Column: 2
# Row: 1 Column: 3
# Row: 2 Column: 1
# Row: 2 Column: 2
# Row: 2 Column: 3
# Row: 3 Column: 1
# Row: 3 Column: 2
# Row: 3 Column: 3


# ==========================================
# 8. Nested If
# ==========================================

age = 25
has_id = True

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("You need ID")
else:
    print("You are too young")

# Output:
# You can enter


# ==========================================
# 9. Find Numbers That Match
# ==========================================

numbers = [10, 15, 20, 25, 30, 35]

for number in numbers:
    if number >= 20 and number <= 30:
        print(number)

# Output:
# 20
# 25
# 30


# ==========================================
# 10. Multiple Conditions
# ==========================================

for number in range(1, 11):
    if number % 2 == 0 and number > 5:
        print(number, "is even and greater than 5")

# Output:
# 6 is even and greater than 5
# 8 is even and greater than 5
# 10 is even and greater than 5


# ==========================================
# 11. Loop Through Names
# ==========================================

names = ["John", "Mary", "Bob", "Sarah", "Mike"]

for name in names:
    if name.startswith("M"):
        print(name, "starts with M")
    else:
        print(name, "does not start with M")

# Output:
# John does not start with M
# Mary starts with M
# Bob does not start with M
# Sarah does not start with M
# Mike starts with M


# ==========================================
# 12. Count Matching Numbers
# ==========================================

numbers = [5, 10, 15, 20, 25, 30]

count = 0

for number in numbers:
    if number >= 20:
        count = count + 1

print("Numbers 20 or higher:", count)

# Output:
# Numbers 20 or higher: 3


# ==========================================
# 13. Find the Largest Number
# ==========================================

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)

# Output:
# Largest: 89


# ==========================================
# 14. Find the Smallest Number
# ==========================================

numbers = [12, 45, 7, 89, 23]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)

# Output:
# Smallest: 7