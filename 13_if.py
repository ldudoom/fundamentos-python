if True:
    print('Deberia ejecutarse')

if False:
    print('Nunca se ejecuta')

pet = input('Cuál es tu mascota favorita? ')

if pet == 'perro':
    print('Genial, tienes buen gusto')
elif pet == 'gato':
    print('Wow eres muy inteligente')
else:
    print('Tienes un', pet)


numero = int(input('Ingresa un numero: '))

if numero % 2 == 0:
    print('Ingresaste un numero par')
else:
    print('Ingresaste un numero impar')