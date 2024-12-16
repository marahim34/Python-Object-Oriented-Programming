numbers = [10, 30, 20, 50, 60]

numbers.append(99)
print(numbers)

numbers.insert(1, 5)
print(numbers)

numbers.insert(2, 55)
print(numbers)

numbers.pop()
print(numbers)

if 55 in numbers:
    numbers.remove(55)

if 8 in numbers:
    numbers.remove(8)

print(numbers)

last = numbers.pop()
print(last, numbers)

index = numbers.index(30)
print(index)

# index = numbers.index(77)
print(index)

if 77 in numbers:
    print(index)
else: print("Not Found")

sorted = numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)