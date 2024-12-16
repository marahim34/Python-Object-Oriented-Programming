#global variable
balance = 3000

#setting local variable in function
# We can access global variable without using the global keyword
# If we want to modify the global variable we need to use the keyword global
def buy_things(item, price):
    global balance
    print('Previous balance = ', balance)
    #local scope variable
    # balance = 300
    balance = balance - price
    print(f'Balance after buying {item}', f'${balance}')

buy_things('Sunglass', 250)