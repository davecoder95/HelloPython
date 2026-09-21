# ==========================================
# PYTHON DATA TYPES - PRACTICE
# ==========================================


# 1. STRING (str)
name = "John"

print("STRING")
print(name)
print("Hello " + name)
print()

# Output:
# STRING
# John
# Hello John


# 2. INTEGER (int)
age = 25

print("INTEGER")
print("Age:", age)

age = age + 1
print("Next year:", age)
print()

# Output:
# INTEGER
# Age: 25
# Next year: 26


# 3. FLOAT (float)
price = 19.99
quantity = 3

total = price * quantity

print("FLOAT")
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)
print()

# Output:
# FLOAT
# Price: 19.99
# Quantity: 3
# Total: 59.97


# 4. BOOLEAN (bool)
is_active = True

print("BOOLEAN")

if is_active:
    print("Account is active")
else:
    print("Account is inactive")

print()

# Output:
# BOOLEAN
# Account is active


# 5. NONE
result = None

print("NONE")

if result is None:
    print("There is no result yet")

print()

# Output:
# NONE
# There is no result yet


# 6. LIST
numbers = [10, 20, 30]

print("LIST")

print("First number:", numbers[0])

numbers.append(40)

print("All numbers:")

for number in numbers:
    print(number)

print()

# Output:
# LIST
# First number: 10
# All numbers:
# 10
# 20
# 30
# 40


# 7. TUPLE
coordinates = (10, 20)

print("TUPLE")

x = coordinates[0]
y = coordinates[1]

print("X:", x)
print("Y:", y)

print()

# Output:
# TUPLE
# X: 10
# Y: 20


# 8. DICTIONARY
person = {
    "name": "John",
    "age": 25,
    "city": "Vancouver"
}

print("DICTIONARY")

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Change a value
person["age"] = 26

print("New age:", person["age"])

print()

# Output:
# DICTIONARY
# Name: John
# Age: 25
# City: Vancouver
# New age: 26


# 9. SET
numbers_set = {10, 20, 20, 30}

print("SET")

print(numbers_set)

numbers_set.add(40)

print("After adding 40:")
print(numbers_set)

print()

# Output:
# SET
# {10, 20, 30}
# After adding 40:
# {10, 20, 30, 40}


# 10. CHECK TYPES
print("TYPES")

print(type(name))
print(type(age))
print(type(price))
print(type(is_active))
print(type(result))
print(type(numbers))
print(type(coordinates))
print(type(person))
print(type(numbers_set))

# Output:
# TYPES
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# <class 'set'>