raul = {
    'name': 'Raul',
    'lastname': 'Chauvin',
    'num_document': '1713068060',
    'birthdate': '05 Enero 1981',
    'cellphone': '0958863051'
}

fher = {
    'name': 'Fher',
    'lastname': 'Morales',
    'num_document': '1002333241',
    'birthdate': '18 Abril 1981',
    'cellphone': '0987229635'
}

astrid = {
    'name': 'Astrid',
    'lastname': 'Chauvin Morales',
    'num_document': '1760317238',
    'birthdate': '07 Agosto 2020',
    'cellphone': '0984309435'
}

family = [raul, fher, astrid]

print(raul)
print(type(raul))

print(fher)
print(type(fher))

print(astrid)
print(type(astrid))

print(family)
print(type(family))

print(raul['birthdate'])
print(fher['birthdate'])
print(astrid.get('birthdate'))

print(astrid.get('cumple'))

if not astrid.get('cumple'):
    print('No existe')
