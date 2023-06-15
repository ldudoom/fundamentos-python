'''
(+)  Suma
(-)  Resta
(*)  Multiplicacion
(/)  Division
(%)  Modulo o Residuo
(//) Division con resultado valor entero
(**) Potenciacion

Operadores Basicos en Python con ejemplos:
https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/

'''

print(10 + 10)
print(10 - 5)
print(10 * 2)
print(10 / 2)
print(10 % 2)
print(10 / 3)
print(10 % 3)
print(10 // 3)
print(2**3)

'''
Orden de ejecucion de operadores
P -> parentesis
E -> exponenciales
M -> multiplicaciones
D -> divisiones
A -> adiciones
S -> substracciones
'''
print(2**3 + 3 - 7 / 1 // 4)
'''
El resultado de esta operacion (2**3 + 3 - 7 / 1 // 4) es 10.0, debido a que se resuelve de la siguiente manera:
1. 2**3 = 8
2. 7 / 1 // 4 = 1
3. 8 + 3 - 1 = 10  -> ((2**3) + 3 - (7 / 1 // 4))
'''

# concatenacion
print("Hola" + " Mundo")

# la cadena se replica 3 veces
print('Muchas gracias ' * 3)



