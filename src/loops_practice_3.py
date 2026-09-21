# ==========================================
# 1. Even or Odd
# ==========================================

for number in range(1, 6):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

# Output:
# 1 is odd
# 2 is even
# 3 is odd
# 4 is even
# 5 is odd


# ==========================================
# 2. Greater Than 5
# ==========================================

numbers = [2, 5, 8, 10, 3, 7]

for number in numbers:
    if number > 5:
        print(number, "is greater than 5")
    else:
        print(number, "is 5 or less")

# Output:
# 2 is 5 or less
# 5 is 5 or less
# 8 is greater than 5
# 10 is greater than 5
# 3 is 5 or less
# 7 is greater than 5


# ==========================================
# 3. If / Elif / Else
# ==========================================

scores = [95, 75, 55, 30]

for score in scores:
    if score >= 90:
        print(score, "Excellent")
    elif score >= 70:
        print(score, "Good")
    elif score >= 50:
        print(score, "Pass")
    else:
        print(score, "Fail")

# Output:
# 95 Excellent
# 75 Good
# 55 Pass
# 30 Fail


# ==========================================
# 4. Break
# ==========================================

for number in range(1, 10):
    print("Number:", number)

    if number == 5:
        break

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5


# ==========================================
# 5. Continue
# ==========================================

for number in range(1, 6):
    if number == 3:
        continue

    print("Number:", number)

# Output:
# Number: 1
# Number: 2
# Number: 4
# Number: 5


# ==========================================
# 6. Loop + If
# ==========================================

names = ["John", "Mary", "Bob", "Sarah"]

for name in names:
    if name == "Bob":
        print(name, "was found!")
    else:
        print(name)

# Output:
# John
# Mary
# Bob was found!
# Sarah