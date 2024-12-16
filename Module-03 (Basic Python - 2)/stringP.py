#sting is sequence of characters

# Single Line String
name1 = 'Steward SingleQuote'
name2 = "James DoubleQuote"

# Multiline string
name3 = """
    Mogumba TripleQuote
    Goody Type
"""

name4 = 'Donald\'s Trump' #escape sign

print(name1)
print(name2)
print(name3)
print(name4)

print(name2[2])
print(name2[2:5])
print(name2[-2])
print(name2[::-1])

if 'James' in name2:
    print('Exist')

print(name2.upper())