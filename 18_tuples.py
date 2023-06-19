numbers = (1, 2, 3, 5)
print(numbers)
print(type(numbers))
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])

names = ('raul', 'fher', 'astrid', 'raul')
print(names)
print(type(names))

# Las tuplas, a diferencia de las listas, son inmutables, 
# es decir no las podemos modificar, no se pueden agregar 
# elementos ni actualizarlos ni eliminarlos

print('En que indice esta el nombre fher:', names.index('fher'))

print('Cuantas veces esta el nombre raul presente en esta tupla:', names.count('raul'))


my_list = list(names)
print(my_list)
print(type(my_list))

my_list[3] = 'isaac'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))