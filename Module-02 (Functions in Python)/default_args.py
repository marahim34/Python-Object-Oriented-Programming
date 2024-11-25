def sum(num1, num2):
    result = num1 + num2
    return result

total = sum(100, 300)

print('Total: ', total)


def sum(num1, num2):
    result = num1 + num2
    return result

# total = sum(100, 300, 400)

print('Total: ', total)


def sum(num1, num2, num3 = 0):
    result = num1 + num2 + num3
    return result

total = sum(100, 800)
total = sum(100, 800, 700)

print('Total: ', total)

# args
def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        # num = num + 1
        sum = sum + num
    return sum

total = all_sum(500, 100, 200, 150, 400, 600)

print('All sum ', total)
