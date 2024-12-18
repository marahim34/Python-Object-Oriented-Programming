def call():
    print('calling ....')
    print('calling done')

class Phone:
    price = 36000
    color = 'metalic blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(4125545, 'I forgot to remind you')
print(result)
