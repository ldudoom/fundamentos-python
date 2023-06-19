person = {
    'name': 'Raul',
    'lastname': 'Chauvin',
    'langs': ['python', 'javascript', 'php', 'go', 'java'],
    'age': 42
}

print(person)

person['name'] = 'Alejandro' # Cambiamos un valor
person['age'] -= 2 # Cambiamos un valor numerico
person['birthday'] = '05 Enero 1981' # Agrego otro indice al diccionario
person['langs'].append('ruby') # Modifico la lista del atributo lagns de mi diccionario

print(person)

del person['birthday']  # Elimino el atributo seleccionado

person.pop('age') # Otra manera de eliminar un atributo

print(person)

# Ver los items de un diccionario
print(person.items())

# Ver los keys de un diccionario
print(person.keys())

# Ver los values de un diccionario
print(person.values())

