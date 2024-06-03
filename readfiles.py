def lee_archivo():
    with open("test.txt", "r") as file:
        content = file.read()
        file.seek(0)
        lineas = file.readlines()
        print(content)
        print(lineas)
        file.close()


def modifica_archivo():
    with open("test.txt", "w") as file:
        file.write("Probando escritura en el archivo")
        file.close()

def agrega_texto(texto):
    with open("test.txt", "a") as file:
        file.write(texto)
        file.close()

lee_archivo()
modifica_archivo()
lee_archivo()
agrega_texto("\nDios sabra!")
lee_archivo()
