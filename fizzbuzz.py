#Fizzbuzz: imprima numero del 1 al 100,
# pero en los multiplos de 4 que imprima "Fizz" en lugar del numero,
# en los multiplos de 5 que imprima "Buzz"
# y cuando es multiplo de ambos que imprima "Fizzbuzz"

numeros = list(range(1, 101))

def fizzbuzz(list):

    numeros_procesados = []

    for i in list:
        if (i % 3 == 0 and i % 5 == 0):
            numeros_procesados.append("FizzBuzz")
        elif (i % 3 == 0 and i % 5 > 0):
            numeros_procesados.append("Fizz")
        elif (i % 3 > 0 and i % 5 == 0):
            numeros_procesados.append("Buzz")
        else:
            numeros_procesados.append(i)

    return numeros_procesados

print(fizzbuzz(numeros))
