'''
counter = 0
while counter <= 10:
    print(counter)
    counter += 1

counter = 0
while counter < 20:
    counter += 1
    print(counter)
    if(counter == 15):
        print('Matamos el bucle')
        break
'''

counter = 0
while counter < 20:
    counter += 1
    if(counter < 15):
        continue
    print(counter)
