# Without comprehension
list_without_comprehension = []
for x in range(10):
    if (x ** 2 % 2) == 0:
        list_without_comprehension.append(x ** 2)

print(list_without_comprehension)

# With comprehension
list_with_comprehension = [x ** 2 for x in range(10) if x ** 2 % 2 == 0]
print(list_with_comprehension)
