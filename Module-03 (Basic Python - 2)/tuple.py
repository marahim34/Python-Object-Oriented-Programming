def multiple():
    return 3, 4
print(multiple())
print(type(multiple))

things = 'pen'
print(things)
print(type(things))

allThings = 'pen', 'pencil', 'water bottle'
print(allThings)
print(type(allThings))
print(allThings[0])
print(allThings[-3])
print(allThings[1:2])

if 'pencil' in allThings:
    print('Exists')

for item in allThings:
    print(item)


# allThings[0] = 'Eraser'

print(allThings.count(2))

# Creating tuples 
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2) 
Tuple2 = ('python', 'geek', 'python', 
		'for', 'java', 'python') 

# count the appearance of 3 
res = Tuple1.count(3) 
print('Count of 3 in Tuple1 is:', res) 

# count the appearance of python 
res = Tuple2.count('python') 
print('Count of Python in Tuple2 is:', res)
