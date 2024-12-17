# lambda

def double(x):
    return x * 2

result = double(16)
print(f'Result is {result}')


doubled = lambda num : num * 2

result1 = doubled(22)
print(result1)

squared = lambda num : num * num
result2 = squared(8)
print(result2)

squared2 = lambda num : num **2
result3 = squared2(8)
print(result3)


sum = lambda a, b: a + b

output = sum(2, 3)
print(output)

numbers = [10, 14, 22, 25, 37, 64, 77, 44]
doubled_nums = map(doubled, numbers)
doubled_numbers = map(lambda x: x *2, numbers)
print(list(doubled_nums))
print(list(doubled_numbers))

actors = [
    {'name': 'Rafi', 'age': 36},
    {'name': 'Shofi', 'age': 65},
    {'name': 'Mofi', 'age': 35},
    {'name': 'Riti', 'age': 39}
]

juniors = filter(lambda actor: actor['age'] < 40, actors)
print(list(juniors))