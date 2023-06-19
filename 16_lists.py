numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
print(type(numbers))

tasks = [
    'lavar platos',
    'jugar videojuegos',
    'hacer dormir a la bebe'
]
print(tasks)
print(type(tasks))

types = [1, True, 'Hola', 3.5]
print(types)
print(types[0])

print(tasks[1])

# Mutacion
text = 'Hola'
# text[0] = 'W' # Da un error porque las cadenas de caracteres no permiten hacer modificaciones de esta forma

print(tasks[0])
tasks[0] = 'Ver los cursos de Platzi'
print(tasks[0])
tasks[0] = 'Lavar los platos'
print(tasks)

print(numbers[:3])

print(True in types)

print('Hola' in types)