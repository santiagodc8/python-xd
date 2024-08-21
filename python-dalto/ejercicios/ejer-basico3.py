#Escribe un programa que determine si un número dado es par o impar.

num1 = 5

op_num1 = num1 % 2

if op_num1 == 0:
    print(f"el numero {num1} es par")
else:
    print(f"el numero {num1} es impar")
    
 
#solucion chatgpt
# Dado un número
numero = 4  # Puedes cambiar este valor para probar diferentes casos

# Verifica si el número es par o impar
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
