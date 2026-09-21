
# ==========================================
# LOOPS PRACTICE
# ==========================================

# 1. Basic for loop
for i in range(5):
    print(i)


# 2. Range with start and end
for i in range(1, 6):
    print("Number:", i)


# 3. Range with step
for i in range(0, 11, 2):
    print("Even:", i)


# 4. Loop through a list
names = ["John", "Mary", "Bob"]

for name in names:
    print("Hello", name)


# 5. Loop with index
names = ["John", "Mary", "Bob"]

for i in range(len(names)):
    print(i, names[i])


# 6. enumerate()
for index, name in enumerate(names):
    print(index, name)


# 7. if inside a loop
numbers = [5, 12, 8, 20, 3]

for number in numbers:
    if number > 10:
        print("Greater than 10:", number)


# 8. break
for number in range(1, 10):
    if number == 5:
        break

    print(number)


# 9. continue
for number in range(1, 6):
    if number == 3:
        continue

    print(number)


# 10. while loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

