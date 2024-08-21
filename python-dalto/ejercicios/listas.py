'''
Crea una lista vacía llamada compras.
Luego, pide al usuario que ingrese elementos para agregar a la lista.
Después de que el usuario termine de agregar elementos (puedes permitirle escribir "fin" para detenerse),
muestra la lista completa.
'''
compras = []  # Creamos una lista vacía para almacenar las compras

while True:
    elemento = input("Ingresa un artículo para agregar a la lista (escribe 'fin' para terminar): ")
    if elemento.lower() == "fin":
        break
    compras.append(elemento)

print("\nLista de compras:")
for compra in compras:
    print("- " + compra)