class Phone:
    manufacturer = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending sms to {phone} and sms is: {sms}'
        print(text)

myPhone = Phone('Donald Trump', 'iPhone', 1500)
print(myPhone.owner, myPhone.brand, myPhone.price)

myPhone.send_sms('041204651', 'I hate you')

hiSPhone = Phone('Joe Biden', 'Samsung', 1350)
print(hiSPhone.owner, hiSPhone.brand, hiSPhone.price)
