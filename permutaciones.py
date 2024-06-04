#Generar permutaciones: dado una lista , funcion devuelve todos los posibles reordenamientos

import itertools

def generar_permutaciones(lista):
    return list(itertools.permutations(lista))

lista = [1,5,9, 1]

permutaciones = generar_permutaciones(lista)

for i in permutaciones:
    print(i)