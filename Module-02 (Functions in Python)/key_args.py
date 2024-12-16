def full_name(first, last):
    name = f'{first} {last}'
    return name

# Take parameters in order
name = full_name('Monti', 'James')
print(name)

name = full_name(last= 'kodu', first= 'loku')
print(name)

def famous_name(first, last, **addition):
    print(addition)
    name = f' {first} {last}'
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first = 'James', last= 'Augustin', title='Dr', addition='Phd')
print(name)


#return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    multi = num1 * num2
    div = round(num1 / num2)

    # return [sum, multi, div]
    return sum, multi, div

everything = a_lot(20, 10)
print(f'Everything, {everything}')
