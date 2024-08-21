#Escribe un programa que determine si un año dado es bisiesto.
# Un año es bisiesto si es divisible por 4, pero no por 100, excepto si es divisible por 400.

año = 2027

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
    
    