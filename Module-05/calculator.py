class Calculator:
    brand = 'Casio M2565'
    def add(self, a, b):
        return a + b
    
    def deduction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        return a /b
    

my_sum = Calculator()
result = my_sum.add(25, 30)
result1 = my_sum.deduction(25, 30)
result2 = my_sum.multiplication(25, 30)
result3 = my_sum.division(25, 30)

print(result)
print(result1)
print(result2)
print(format(result3, ".2f"))