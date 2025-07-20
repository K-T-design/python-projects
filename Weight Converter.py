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
        que = print('Do you want Your Weight in Kilograms or Ounces : ')
        rep_ = input('')
        try:
            rep_
        except:
            print('Check what you entered ')
         
    if rep_.lower() == 'kilograms':
        kil_ = input(' Enter your weight in Pounds: ')
    elif rep_.lower() == 'ounces':
        oun_ = input('Enter your weight in Pounds: ')
        
    if rep_.lower() == 'kilograms':
        try:
            kilv_ = int(kil_) / 2.205
        except:
            print('Enter A Valid Value')
            continue
        print(f' Your weight in Kilograms is {kilv_} kg')
        if kilv_ >= 75:
            print('Chimmmooooo!!!🙆‍♂️🙆‍♂️🙆‍♂️ Oga go loose weight ooo🤣🤣🤣')
            
        elif kilv_ <= 74:
            print('Your Weight is Nice. Don\'t add more ooo😂😂')
        break
        
    if rep_.lower() == 'ounces':
        try:
            ounv_ = int(oun_) * 16
        except:
            print('Enter A Valid Value')
            continue
        print(f'Your weight in Ounces is {ounv_} oz')
        if ounv_ >= 2645.45:
            print('Chimmmooooo!!!🙆‍♂️🙆‍♂️🙆‍♂️ Oga go loose weight ooo🤣🤣🤣')
        elif ounv_ <= 2644.44:
            print('Your Weight is Nice. Don\'t add more ooo😂😂')       
        break
            
    elif ans.lower() == 'no':
        print('Why are you afraid to check your Weight na🤣🤣 you oversized pig. I\'ll not waste my time giving you another try🤣🤣')
        break

    



