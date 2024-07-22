datos={"Juan123":"J12an*.","Maria2345":"M23a*.","Pablo1459":"P14o*.","Ana3456 ":"A34a*."}

for i in range(4):
    if i == 3:
        print("Lo siento, su acceso no es permitido")
        break
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario in datos and contrasena == datos[usuario]:
        print("Acceso permitido")
        break
    else:
        print("\ndatos incorrectos ingreselos de nuevo")
