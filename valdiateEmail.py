import re

def validEmail(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    if re.match(regex, email):
        return True
    else:
        return False
    
email = input("Ingrese un correo electronico para comprobarlo: ")    
if validEmail(email):
    user = email.split(sep="@")
    print("Su correo es correcto y su usuario es: " + user[0])
else:
    print("Su correo es invalido")