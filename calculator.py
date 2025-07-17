import math

print('MY SIMPLE CALCULATOR PROJECT')

name = input(f'Can I get to know your name please 🤗? ')

print(f'Hello there {name}! Let\'s get your values down?')
while True:
    try:
        _nu1 = int(input(f'First Value: '))
        _nu2 = int(input(f'Second Value: '))
    except :
        print('The Value You Entered is Not A Number') 
    else:
        break
    
    
while True:
        
    print('What operation would you like to perform? Addition, Subtraction, Multiplication, Division, Modulus')

    op_ = input(f'>> ')
    if (op_.lower()) == 'addition':
        print(int(_nu1) + int(_nu2))
    elif (op_.lower()) == 'subtraction':
        print(int(_nu1) - int(_nu2))
    elif (op_.lower()) == 'multiplication':
        print(int(_nu1) * int(_nu2))
    elif (op_.lower() == 'division'):
        print(int(_nu1) // int(_nu2))
    elif (op_.lower() == 'modulus'):
        print(int(_nu1) % int(_nu2))
    else:
        print('I\'m Very Sorry This Function Has Not Been Added To My Functionality By My Developer')
        break
    
    
    
          
