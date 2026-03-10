n = input("numero: ")

try:
    int(n)
    n2 = n[::-1]
    if n == n2:
        print("capicua")
    else:
        print("no capicua")
except ValueError:
    print("No es numero")
