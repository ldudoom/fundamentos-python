# Metodos de listas
'''
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''

# CRUD

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)
numbers.append(700)
print(numbers)
numbers.insert(0, 'Hola')
print(numbers)

numbers.insert(3, 'Change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']

new_list = numbers + tasks # Une las 3 listas
print(new_list)

new_list[new_list.index('todo 2')] = 'todo 2 changed'  # Modifica el elemento todo 2 de la ista
print(new_list)

new_list.remove('todo 1') # ELimina el elemento todo 1 de la lista
print(new_list)

new_list.pop() # elimina el ultimo elemento de la ista
print(new_list)

new_list.pop(0) # Elimina el item de la posicion 0 de la lista
print(new_list)

new_list.reverse() # Revierte los items de una lista
print(new_list)

numbers_2 = [1,4,6,9,2,7,8,5,3]
print(numbers_2)
numbers_2.sort()
print(numbers_2)

strings = ['re', 'ab', 'ed']
print(strings)
strings.sort()
print(strings)

# new_list.sort() # no funciona porque la lista tiene elementos de diferentes tipos de datos