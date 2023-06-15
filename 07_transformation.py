name = "Raul"
print(type(name))

name = 12
print(type(name))

name = 12.21
print(type(name))

name = False
print(type(name))

print("Raul" + " Chauvin")
print(10 + 20)
# Esto no se puede hacer
# print("Raul" + 42)

# Convertimos el tipo de dato a string para que haga la concatenacion
age = 42
print('Mi edad es ' + str(age))

# Tambien podriamos usarlo con la funcion f
print(f"Mi edad es {age}")


age = int(input("Que edad tienes?: "))
print(type(age))

print(f'Tu edad en 10 años sera {age + 10}')