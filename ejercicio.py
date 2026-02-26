'''
#Ej 1
print("Dame dos numeros a sumar")
a= int(input())
b= int(input())
suma = a+b
print("La suma es ",suma)


#Ej 2
print("Gimme your numbah'")
a= input()
areverse = a[::-1]
print("Your reversed numbah is ", areverse)

#Ej 3
print("Bom dia, quiero que me des los siguientes datos:")
print("1. Dame tu nombre")
nombre = input()
print("2. Dame tu edad")
edad = input() 
print("3. Dame tu profesion")
profesion = input()
print("Un tusco,",nombre, "de",edad, "anos", "eres", profesion)

'''
#Ej 4
print("Cuantas interaciones?")
n=int(input())
a=0
lista=[]
while(a<n):
    print("dame un numero")
    num= int(input())
    if num not in lista:
        lista.append(num)
    a=a+1
print('los valores unicos son',lista)

