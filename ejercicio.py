#1 
n = int(input('Cuantos numeros quieres agregar?'))
total = 0;

print('Por el rojas por favor agrega los numeros uno por uno')

for i in range(n):
    num = float(input(f"Ingresa el numero {i+1}: "))
    total += num

print('Tu suma es: ', total)

#2
numero = input('Ingresa un numero para invertir:')
print('Tu numero invertido es: ', numero[::-1])

#3
nombre = input('Cual es tu nombre?')
edad = input('Cual es tu edad?')
profesion = input('Cual es tu profesion?')

if profesion == 'Ingenieria':
    print(f'Alabado sea el ingeniero que nunca le falte chamba ni orgullo ni el matlab crackeado, bienvenido a la familia {nombre}')
elif int(edad) > 70:
    print('Dios te cuide hermanx')
else:
    print(f'Bienvenido a la familia {nombre}, espero que tu profesion de {profesion} te llene de satisfacciones y te den ganas de ser ingeniero')


#4
x = int(input('Cuantos numeros queres agregar?'))
numeros = []

for i in range(x):
    numeros.append(input(f'Ingresa el numero {i+1}: '))

unicos = list(set(numeros))
print('Los numeros unicos son:', unicos)
