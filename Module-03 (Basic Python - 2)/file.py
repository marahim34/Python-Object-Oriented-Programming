# .csv comma separated value
# .txt text file

# with open('message.text', 'w') as file:
#     file.write('It is a complex component of Python')
with open('message.text', 'a') as file:
    file.write('It is a complex component of Python')


with open('message.text', 'r') as file:
    text = file.read()
    print(text)