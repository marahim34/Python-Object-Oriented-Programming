#list, array, collection is same (in simple terms)

# index =   0  1   2   3   4   5   6   7 [Forward Index]
numbers = [45, 60, 65, 88, 99, 77, 11, 33]
# index =  -8  -7  -6  -5  -4  -3  -2  -1 [Reverse Index]

print(numbers[3], numbers[-3])


#list (start: end) #start from the start index and end before the end index
print(numbers[2:6])
print(numbers[1:7])

#list (start: end: step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[7:2:-1 ])

print(numbers[-2: -7: -1])
print(numbers[-2: -7: -2])

print(numbers[:])
print(numbers[:5])
print(numbers[3:])
print(numbers[::-1]) #shortcut to reverse a list
print(numbers[::1]) # copy a list

