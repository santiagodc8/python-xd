
animales = ["gato","perro", "loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a:  {animal}")
    
#recorriendo la lista numeros y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    

for numero, animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
    
for num in range(10):
    print(num)