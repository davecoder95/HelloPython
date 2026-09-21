
# ==========================================
# LISTS PRACTICE
# ==========================================

# 1. Create a list
numbers = [10, 20, 30, 40, 50]

print(numbers)


# 2. Access items
print(numbers[0])
print(numbers[2])
print(numbers[-1])


# 3. Change an item
numbers[0] = 100

print(numbers)


# 4. Add an item
numbers.append(60)

print(numbers)


# 5. Insert an item
numbers.insert(1, 15)

print(numbers)


# 6. Remove an item
numbers.remove(30)

print(numbers)


# 7. Remove by position
numbers.pop(0)

print(numbers)


# 8. List length
print("Length:", len(numbers))


# 9. Loop through list
for number in numbers:
    print(number)


# 10. Find items
for number in numbers:
    if number > 30:
        print("Greater than 30:", number)


# 11. Sum
total = sum(numbers)

print("Total:", total)


# 12. Minimum and maximum
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))


# 13. Sort
numbers.sort()

print("Sorted:", numbers)


# 14. Reverse
numbers.reverse()

print("Reversed:", numbers)


# 15. Check if item exists
if 50 in numbers:
    print("50 exists")


# 16. List of strings
names = ["John", "Mary", "Bob"]

for name in names:
    print(name)


# 17. List comprehension
squares = [number * number for number in range(1, 6)]

print("Squares:", squares)
