#funcion que cuenta la frecuencia de elementos en una lista

from collections import Counter

lista = ["manzana", "pera", "pera", "manzana", "uva", "melon", "uva"]

def contar_frecuencias(lista):
    return dict(Counter(lista))

frecuencias = contar_frecuencias(lista)

elementos = " ".join(list(set(lista)))

print(f"Elementos de la lista: {elementos}")

find = input("De que elemento deseas saber la frecuencia? ")

print(f"La frecuencia de {find} es {frecuencias[find]}")
