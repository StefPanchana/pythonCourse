#Genera una funcion para validar sudokus



def verificar_sudoku(tablero):
    #Grupo valido
    def es_grupo_valido(grupo):
        numeros = [num for num in grupo if num != 0]
        return len(numeros) == len(set(numeros))

    for fila in tablero:
        if not es_grupo_valido(fila):
            return False

    for col in range(9):
        columna = [fila[col] for fila in tablero]
        if not es_grupo_valido(columna):
            return False

    for caja_fila in range(0,9,3):
        for caja_columna in range(0,9,3):
            subcuadricula = [tablero[f][c] for f in range(caja_fila,caja_fila+3) for c in range(caja_columna,caja_columna+3)]
        if not es_grupo_valido(subcuadricula):
            return False

    return True
