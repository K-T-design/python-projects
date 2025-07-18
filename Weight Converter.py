print('Hello There!!! I\'m WALTER, Your Weight Converter Bot 🤖')

name = input(f'Can I get to know your name please 🤗? ')

print(f'Hello {name}, Are you ready to convert your Weight')
_y = 'Yes'
_n = 'No'
print(_y)
print(_n)
ans = input('>> ')
while True:
    if ans.lower() == 'yes':
        que = print('Please input your weight in pounds: ')
        val_ = input('')
        try:
           conv_ = int(val_) / 2.205
        except:
            print('You did not enter a valid value')
        else:
            print(f'Your Weight in Kilograms is {conv_}')
            if conv_ >= 75:
               print('Chimmmooooo!!!🙆‍♂️🙆‍♂️🙆‍♂️ Oga go loose weight ooo🤣🤣🤣')
            elif conv_ <= 74:
               print('Your Weight is Nice. Don\'t add more ooo😂😂')
        break
            
    elif ans.lower() == 'no':
        print('Why are you afraid to check your Weight na🤣🤣 you oversized pig. I\'ll not waste my time giving you another try🤣🤣')
        break

    



