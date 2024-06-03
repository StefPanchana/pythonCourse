name, age, address = input("Por favor, a continuación Ingresa tu nombre: Ingresa tu edad: Ingresa tu dirección: ").split()

def write_file(name, age, address):
    try:
        with open("test.txt", "a+") as file:
            file.write("\nNombre: " + name + ", " + "Edad: " + age + ", " + "Dirección: " + address + "\n")
            file.close()
    except FileNotFoundError:
        print("El archivo no existe")
    except PermissionError:
        print("No tiene permiso para modificar el archivo")
    except Exception as ex:
        print(ex)
    else:
        print("correctamente procesado")
    finally:
        print("ejecucion de funcion finalizada")

write_file(name, age, address)
