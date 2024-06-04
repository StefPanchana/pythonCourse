import random
import time

inicio = time.time()
def encontrar_indices(lista, elemento):
    indices = []
    for indice, valor in enumerate(lista):
        if valor == elemento:
            indices.append(indice)
    return indices
print(encontrar_indices([1, 2, 3, 4, 3, 8, 9, 3, 10, 100, 1000, 15, 25 ,35 , 3], 3))
fin = time.time()

print(f"El tiempo de ejecucion fue {fin-inicio}")

#Creacion de una lista
lista2 = [random.randint(1,10) for i in range(100000)]
print(encontrar_indices(lista2, 2))
print(f"El tiempo de ejecucion fue {fin-inicio}")