# 1.
def add_numeros():
    n = int(input("Cuantos numeros quieres"))
    t = 0

    for i in range(n):
        num = int(input("insertar"))
        t = t + num
    print("los numeros son", t)

# 2. 
def invertir_numero():
    numero = input("Ingrese un número para invertir")
    invertido = numero[::-1]
    print("Número invertido:", invertido)


# 3. 
def informacion_usuario():
    nombre = input("Ingrese su nombre ")
    edad = input("Ingrese su edad ")
    profesion = input("Ingrese su profesión")

    print("Hola", nombre + ", tienes", edad, "años y tu profesión es", profesion)


# 4. 
def valores_unicos():
    cantidad = int(input("Cuántos números desea ingresar "))
    lista = []

    for i in range(cantidad):
        numero = input("Ingrese un número: ")
        lista.append(numero)

    unicos = list(set(lista))
    print("Valores únicos:", unicos)

add_numeros()
invertir_numero()
informacion_usuario()
valores_unicos()
