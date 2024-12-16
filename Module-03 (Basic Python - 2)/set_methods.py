# set: unique items collection, no duplicate. But it does not maintain the orders. Therefore we cannot set any number in a specific position
# list: we use []
# tuple: we use ()
# set: we use {}
numbers = [12, 25, 37, 50, 62, 75, 87, 100 ]
print(numbers)

numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(55)
print(numbers_set)

for item in numbers_set:
    print(item)

if 12 in numbers_set:
    print("Exists")

A = {1,3,5,7}
B = {2,3,4,5,6}

print(A & B) 
print(A | B) 