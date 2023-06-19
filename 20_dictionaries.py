'''
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''

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

