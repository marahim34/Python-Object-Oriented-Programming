# in, not, not in, is, is not
# comparison >=, <=, ==, !==

a = 1
if a>5:
    print('It is greater than 5')
elif a > 3:
    print("A bit larger")
elif a == 2:
    print("Almost same")
else:
    print('It is one')


boss = False

if boss is not True:
    print("Call someone")
else:
    print("Boss, someone is looking for you")