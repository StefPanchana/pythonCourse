import time

def medir_tiempo(func):
    def funcion_decorada():
        inicio = time.time()
        resultado = func()
        fin = time.time()
        print(f"Tiempo de ejecucion de {func.__name__} : {fin - inicio:.4f} segundos")
        return resultado
    return funcion_decorada

@medir_tiempo
def ejemplo_funcion():
    print("Iniciando")
    time.sleep(2)
    print("Funcion completada")


ejemplo_funcion()