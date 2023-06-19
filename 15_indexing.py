'''
Los textos tienen indices a los cuales podemos acceder, algo como esto:

 |-----------------------------------------------------------------------|
 | 0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |  11
 |-----------------------------------------------------------------------|
 |    |     |     |     |     |     |     |     |     |     |      |     |
 | H  |  o  |  l  |  a  |  ,  |     |  m  |  u  |  n  |  d  |   o  |  !  |
 |    |     |     |     |     |     |     |     |     |     |      |     |
 |-----------------------------------------------------------------------|
 |-12 | -11 | -10 | -9  | -8  | -7  | -6  | -5  | -4  | -3  |  -2  |  -1 |
 |-----------------------------------------------------------------------|
'''

text = 'El sabe PHP'
print(text.index('PHP'))
print(text[8])
# print(text[16]) # En este caso Python devuelve un error

print(text[-1])
print(text[len(text) - 1])
print(text[0:2])
print(text[8:11])

print(text[:2]) # es lo mismo que poner  print(text[0:2]), imprime desde el inicio de la cadena hasta el valor del indice que hayamos ingresado

print(text[6:-1]) # Vamos a imrpimir desde in indice hasta el final de la cadena, el problema de esto es que no se incluye el ultimo caracter
# para eso vamos a hacer lo siguiente:
print(text[6:]) # Con esta sintaxis si vamos a imprimir la cadena desde el indice que le indicamos hasta el final de la cadena

print(text[:]) # Por lo tanto esta linea imprime desde el inicio hasta el final de la cadena

print(text[6:11:1]) # Se imprimime la cadena desde la posicion 6 hasta la posicion 11 dando 1 salto por vez
print(text[6:11:2]) # Se imprimime la cadena desde la posicion 6 hasta la posicion 11 dando 2 saltos por vez