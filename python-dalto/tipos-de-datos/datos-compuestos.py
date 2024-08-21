#creando una lista (se pueden modificar)
lista = ['santiago','santiago.dc',True,1.72]

#creando una tupla (no pueden modificar)
tupla = ('santiago','santiago.dc',True,1.72)

#esto es vàlido
lista[3] = "Maquinola"

#esto no
tupla[3] = "Maquinola"

print(lista[3])

#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)

conjunto = {'santiago','santiago.dc',True,1.72,'santiago.dc'}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)

diccionario = {
    'nombre' : "santiago",
    'canal' : "santiago.dc",
    'esta_emocionado' : True,
    'altura' : 1.72,
    'dato_duplicado' : "santiago.dc"
}