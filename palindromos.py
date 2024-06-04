#Verifica palindromos: chequear string y verificar si es palindromo

#Definir funcion
#Limpiar: espacios, puntuacion y pasar a minusculas
#Ver si se lee igual de atras para adelante y de adelante para atras
#Devolver true si es palindromo, caso contrario false

def es_palindromo(s):
    string_limpio = "".join(caracter.lower() for caracter in s if caracter.isalnum())

    return string_limpio == string_limpio[::-1]


print(es_palindromo("Dabale arroz a la zorra el abad"))
print(es_palindromo("No 'x' in Nixon"))
print(es_palindromo("Aguante Boca"))