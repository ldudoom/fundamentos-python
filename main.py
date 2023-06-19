# Juego de piedra papel o tijera
import random

user_option = input('piedra, papel o tijera? => ').lower().strip()
options = ('piedra', 'papel', 'tijera')
rand_option = random.randint(0,2)
'''
if rand_option == 0:
    computer_option = 'piedra'
elif rand_option == 1:
    computer_option = 'papel'
else:
    computer_option = 'tijera' 
'''
computer_option = options[rand_option]
print('Computer option: ', computer_option)
print('*' * 100)

if computer_option == 'piedra':
    if user_option == 'piedra':
        print('Empate')
    elif user_option == 'papel':
        print('Ganaste !!')
    elif user_option == 'tijera':
        print(':( Perdiste')
elif computer_option == 'papel':
    if user_option == 'piedra':
        print(':( Perdiste')
    elif user_option == 'papel':
        print(':: Empate ::')
    elif user_option == 'tijera':
        print('Ganaste !!')
else:
    if user_option == 'piedra':
        print('Ganaste !!')
    elif user_option == 'papel':
        print(':( Perdiste')
    elif user_option == 'tijera':
        print('Empate')