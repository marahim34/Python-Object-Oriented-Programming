numbers = [10, 14, 22, 25, 37, 64, 77, 44]

person1 = ['Donald Trump', 'USA', 65, 'Business Man']

# It is know in different names in different programming languages
# Key Value pair
# Dictionary
# Object
# Hash table
# Overlap with set
# {key: value}

person = {'name': 'Joe Biden', 'address': 'USA', 'age': 68, 'profession': 'Hacker'}
print(person)
print(person['profession'])
print(person['age'])
print(person.keys())
print(person.values())
person['language'] = 'Somali'

print(person['language'])
print(person)

# If we run the following function then we will only get the item names
for item in person:
    print(item)

# Therefore we need to run the for loop in the following ways
for key, value in person.items():
    print(key, value)



