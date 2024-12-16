numbers = [10, 60, 55, 99, 77, 33, 66]
odds = []
even = []
uncategorized = []

for num in numbers:
    if num % 2 == 1 and num % 5 ==0:
        odds.append(num)
    elif num % 2 == 0:
        even.append(num)
    else: 
        uncategorized.append(num)

print(odds, even, uncategorized)

odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)