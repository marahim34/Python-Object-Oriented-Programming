#define
def double_it(num):
    result = num * 2
    print(result)
    return result

double_it(12)
double_it(100)

def sum_it(num1, num2):
    result = num1 + num2
    return result

total = sum_it(10, 40)

print('Total value', total)

final = double_it(total)

print('Two function', final)