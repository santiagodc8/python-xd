#Escribe un programa que determine cuál de tres números dados es el mayor.

num1 = 3
num2 = 7
num3 = 5

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
    
print("el numero mayor es: ",mayor)