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

odd_numbers = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_numbers)

players = ['Sakib', 'Mushfiq', 'Rafiq', 'Nannu']
ages = [42, 36, 55, 65]

age_com = []
for player in players:
    print('player: ', player)
    for age in ages:
        print(player, age)
        age_com.append([player, age])

print(age_com)

age_comb2 = [(player, age) for player in players for age in ages ]
print(age_comb2)