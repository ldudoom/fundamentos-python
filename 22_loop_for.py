'''
for element in range(1, 21):
    print('iteracion', element)
'''

my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print(element)

my_tuple = ('Raul', 'Alejandro', 'Chauvin', 'Ojeda')
for element in my_tuple:
    print(element)

product = {
    'name': 'Cellphone',
    'price': 100.50,
    'stock': 85
}

for element in product:
    print(element)
    print(product[element])


for key in product:
    print(key, '=>', product[key])

for key, value in product.items():
    print(key, ':', value)


family = [
    {
        'name': 'Raul',
        'lastname': 'Chauvin',
        'num_document': '1713068060',
        'birthdate': '05 Enero 1981',
        'cellphone': '0958863051'
    },
    {
        'name': 'Fher',
        'lastname': 'Morales',
        'num_document': '1002333241',
        'birthdate': '18 Abril 1981',
        'cellphone': '0987229635'
    },
    {
        'name': 'Astrid',
        'lastname': 'Chauvin Morales',
        'num_document': '1760317238',
        'birthdate': '07 Agosto 2020',
        'cellphone': '0984309435'
    }
]

for person in family:
    print('Hola', person['name'], person['lastname'])