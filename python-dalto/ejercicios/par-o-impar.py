'''
Ejercicio 1: Número par o impar
Escribe un programa que pida al usuario un número y determine si es par o impar.
Utiliza if y else para mostrar el resultado.
'''
numero = int(input("Escribe un numero entero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")