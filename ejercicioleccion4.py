# Ejercicio de Juego Tic Tac Toe
marcajugadorA = "X"
marcajugadorB = "O"

# Primera Función
def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print("|" + "|".join(fila) + "|")

def verificar_ganador(tablero, jugador):
    #Verificar filas, columnas y diagonales
    for i in range(3):
        #Chequeo de columnas
        if all([tablero[i][j] == jugador for j in range(3)]):
            return True
        #Chequeo de filas
        if all([tablero[j][i] == jugador for j in range(3)]):
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

def tablero_lleno(tablero):
    return all([tablero[i][j] != " " for i in range(3) for j in range(3)])

def cambiar_jugador(actual):
    return "O" if actual == "X" else "X"

def hacer_movimiento(tablero, jugador):
    while True:
        fila = int(input(f"{jugador}, elija fila 1, 2 o 3: ")) -1
        columna = int(input(f"{jugador}, elija columna 1, 2 o 3: ")) - 1

        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("Movimiento inválido, intente nuevamente")


def jugar_tateti():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        mostrar_tablero(tablero)
        hacer_movimiento(tablero, jugador_actual)

        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print(f"{jugador_actual} ha ganado")
            break
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("Empate")
            break

        jugador_actual = cambiar_jugador(jugador_actual)

jugar_tateti()