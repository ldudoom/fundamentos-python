name = "Raul"
last_name = "Chauvin"
print(name)
print(last_name)

full_name = name + last_name
full_name = name + " " + last_name

print(full_name)

quote = 'I\'m Raul'
print(quote)

# format
name = input("Cuál es nu nombre?: ")
last_name = input("Cuál es tu apellido?: ")
age = input("Qué edad tienes?: ")

# Primera forma de imprimir la cadena concatenando las variables
template = "Hola, mi nombre es " + name + ", mi apellido es " + last_name + " y tengo " + age + " años"
print('Concatenacion normal: ', template)

# Segunda forma de imprimir la cadena concatenando las variables, usamos la funcion format
template2 = "Hola, mi nombre es {}, mi apellido es {} y tengo {} años".format(name, last_name, age)
print('Concatenacion format: ', template2)

# Tercera forma de imprimir la cadena concatenando las variables, usamos una funcion format simplificada
template3 = f"Hola, mi nombre es {name}, mi apellido es {last_name} y tengo {age} años"
print('Concatenacion f: ', template3)
