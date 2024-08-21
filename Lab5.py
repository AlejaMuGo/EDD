from Lab2 import Usuario
from Lab4 import DoubleList
from datetime import datetime

class Mensaje:
    def __init__(self,remitente,destinatario,titulo,contenido,):
        self._titulo = titulo
        self._contenido = contenido
        self._remitente = remitente
        self._destinatario = destinatario
        self._fechaEnvio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def getFechaEnvio(self):
        return self._fechaEnvio
    def getTitulo(self):
        return self._titulo
    def getContenido(self):
        return self._contenido
    def getRemitente(self):
        return self._remitente
    def getDestinatario(self):
        return self._destinatario
    def setFechaEnvio(self,f):
        self._fechaEnvio = f
    def setTitulo(self, titulo):
        self._titulo = titulo
    def setContenido(self, contenido):
        self._contenido = contenido
    def setRemitente(self, remitente):
        self._remitente = remitente
    def setDestinatario(self, destinatario):
        self._destinatario = destinatario

class BandejaEntrada(DoubleList):
    def __init__(self,idD):
        super().__init__()
        self._idD = idD
    def getIdD(self):
        return self._idD
    def setIdD(self,idD):
        self._idD = idD

class Contrasena:
    def __init__(self, idC, contrasena, tipoUser):
        self._idC = idC
        self._contrasena = contrasena
        self.tipoUser = tipoUser
    def getIdC(self):
        return self._idC
    def getContrasena(self):
        return self._contrasena
    def getTipoUser(self):
        return self.tipoUser
    def setIdC(self, idC):
        self._idC = idC
    def setContrasena(self, contrasena):
        self._contrasena = contrasena
    def setTipoUser(self, tipoUser):
        self.tipoUser = tipoUser

class Sistema:
    _empleados = DoubleList()
    _contrasenas = DoubleList()
    _bandejas = DoubleList()
    @classmethod
    def getEmpleados(cls):
        return cls._empleados
    @classmethod
    def getContrasenas(cls):
        return cls._contrasenas
    @classmethod
    def getBandejas(cls):
        return cls._bandejas
    @classmethod
    def setEmpleados(cls, empleados):
        cls._empleados = empleados
    @classmethod
    def setContrasenas(cls, contrasenas):
        cls._contrasenas = contrasenas
    @classmethod
    def setBandejas(cls, bandeja):
        cls._bandejas = bandeja

    @classmethod
    def cargarEmpleados(cls):
        archivo = open(f"Empleados.txt", "r")
        for linea in archivo:
            user = linea.split(" ")
            nombre = user[0].replace("-", " ")
            u = Usuario(nombre, user[1])
            u.setFecha_nacimiento(user[2], user[3], user[4])
            u.setCiudad_nacimiento(user[5])
            u.setTel(user[6])
            u.setEmail(user[7])
            u.setDir(user[8], user[9], user[10], user[11], user[12], user[13])
            cls._empleados.addFirst(u)

    @classmethod
    def cargarContrasenas(cls):
        archivo = open(f"Password.txt", "r")
        for linea in archivo:
            contrasenaData = linea.split(" ")
            idC = contrasenaData[0]
            c = contrasenaData[1]
            tipoUser = contrasenaData[2]
            contrasena = Contrasena(idC, c, tipoUser)
            cls._contrasenas.addLast(contrasena)

    @classmethod
    def verificarEmpleado(cls, id, contrasInput):
        temp = cls._contrasenas.First()
        while temp is not None:
            if temp.getData().getContrasena() == contrasInput and temp.getData().getIdC() == id:
                return True
            temp = temp.getNext()
        return False

    @classmethod
    def buscarEmpleado(cls, id):
        temp = cls._empleados.First()
        while temp is not None and int(temp.getData().getId()) != int(id):
            temp = temp.getNext()
        return temp

    @classmethod
    def buscarContrasena(cls, id):
        temp = cls._contrasenas.First()
        while temp is not None and int(temp.getData().getIdC()) != int(id):
            temp = temp.getNext()
        return temp

    @classmethod
    def verificarTipoUser(cls, id):
        temp = cls._contrasenas.First()
        while temp is not None and temp.getData().getIdC() != id:
            temp = temp.getNext()
        return temp.getData().getTipoUser()

    @classmethod
    def ordenarEmpleados(cls,lista):
        if lista.size() > 1:
            for i in range(lista.size()):
                current = lista.First()
                for j in range(1, lista.size() - i):
                    next_node = current.getNext()
                    if int(current.getData().getId()) > int(next_node.getData().getId()):
                        current_data = current.getData()
                        next_data = next_node.getData()
                        current.setData(next_data)
                        next_node.setData(current_data)
                    current = next_node

    @classmethod
    def buscarBandeja(cls, id):
        temp = cls._bandejas.First()
        while temp != None and int(temp.getData().getIdD()) != int(id):
            temp = temp.getNext()
        return temp
    @classmethod
    def crearMensaje(cls,idRem,idDes,titulo,contenido):
        mensaje = Mensaje(idRem,idDes,titulo,contenido)
        bandejaE_nodo = cls.buscarBandeja(idDes)

        if bandejaE_nodo is None:
            bandejaE = BandejaEntrada(idDes)
            cls._bandejas.addFirst(bandejaE)
        else:
            bandejaE = bandejaE_nodo.getData()

        bandejaE.addFirst(mensaje)

        nombreTexto = f"{idDes}BA.txt"
        remNombre = cls.buscarEmpleado(idRem).getData().getNombre()
        with open(nombreTexto, "a") as archivo:
            archivo.write(f"{remNombre},{idRem},{mensaje.getTitulo()},{mensaje.getContenido()}\n")

    @classmethod
    def cargarBandejas(cls, id):
        textNom = f"{id}BA.txt"
        archivo = open(textNom, "r")
        bandeja = BandejaEntrada(id)
        for linea in archivo:
            men = linea.split(",")
            idRem = men[1]
            titulo = men[2]
            contenido = men[3]
            mensaje = Mensaje(idRem, id, titulo, contenido)
            bandeja.addFirst(mensaje)
            cls._bandejas.addFirst(bandeja)

    @classmethod
    def verBandeja(cls, id):
        bandeja = cls.buscarBandeja(id)

        if bandeja is None:
            print("No hay mensajes en la bandeja.")
            return

        print(f"\nTiene {bandeja.getData().size()} mensajes:")


        elemento = bandeja.getData().First()
        for i in range(1,bandeja.getData().size()+1):
            mensaje = elemento.getData()
            idRem = mensaje.getRemitente()
            nombreRem = cls.buscarEmpleado(idRem).getData().getNombre()
            print(f"Mensaje #{i} Fecha:{mensaje.getFechaEnvio()}  Título:{mensaje.getTitulo()}  De:{nombreRem}")
            elemento = elemento.getNext()
        seleccion = input("Escriba el numero del mensaje que desea leer: ")
        elemento = bandeja.getData().First()
        for i in range(1, bandeja.getData().size() + 1):
            mensaje = elemento.getData()
            idRem = mensaje.getRemitente()
            nombreRem = cls.buscarEmpleado(idRem).getData().getNombre()
            if int(i) == int(seleccion):
                print(f"\nMensaje #{i}\n"
                      f"\n{mensaje.getTitulo()}\n"
                      f"\n{mensaje.getContenido()}"
                      f"\nAtentamente, {nombreRem}")
            elemento = elemento.getNext()


class Administrador(Usuario):
    def registrar_usuario(self, nombre, id,fechaNaci,cn,tel,email,calle,nomen,barrio,ciudad,edificio,apto,contrasena):
        nuevoUser = Usuario(nombre, id)
        f = fechaNaci.split("/")
        dia = f[0]
        mes = f[1]
        a = f[2]
        nuevoUser.setFecha_nacimiento(dia,mes,a)
        nuevoUser.setCiudad_nacimiento(cn)
        nuevoUser.setTel(tel)
        nuevoUser.setEmail(email)
        nuevoUser.setDir(calle,nomen,barrio.replace(' ','-'),ciudad,edificio.replace(' ','-'),apto)
        Sistema.getEmpleados().addLast(nuevoUser)
        Sistema.ordenarEmpleados(Sistema.getEmpleados())
        with open("Empleados.txt","a") as archivo:
            archivo.write(f"{nuevoUser.getNombre().replace(' ', '-')} {nuevoUser.getId()} {nuevoUser.getFecha_nacimiento()} {nuevoUser.getCiudad_nacimiento()} {nuevoUser.getTel()} {nuevoUser.getEmail()} {nuevoUser.getDir()}\n")
        contras = Contrasena(nuevoUser.getId(),contrasena,"empleado")
        Sistema.getContrasenas().addLast(contras)
        with open("Password.txt", "a") as archivo:
            archivo.write(f"{contras.getIdC()} {contras.getContrasena()} {contras.getTipoUser()}")

    def eliminar_usuario(self, id):
        empleado = Sistema.buscarEmpleado(id)
        Sistema.getEmpleados().remove(empleado)
        with open("Empleados.txt", "w") as archivo:
            e = Sistema.getEmpleados().First()
            for j in range(Sistema.getEmpleados().size()):
                archivo.write(f"{e.getData().getNombre().replace(' ', '-')} {e.getData().getId()} {e.getData().getFecha_nacimiento()} {e.getData().getCiudad_nacimiento()} {e.getData().getTel()} {e.getData().getEmail()} {e.getData().getDir()}")
                e = e.getNext()
        contrasena = Sistema.buscarContrasena(id)
        Sistema.getContrasenas().remove(contrasena)
        with open("Password.txt", "w") as archivo:
            c = Sistema.getContrasenas().First()
            for j in range(Sistema.getContrasenas().size()):
                archivo.write(f"{c.getData().getIdC()} {c.getData().getContrasena()} {c.getData().getTipoUser()}")
                c = c.getNext()

    def cambiar_contrasena(self, id, nueva_contrasena):
        contrasenaCambiar = Sistema.buscarContrasena(id)
        contrasenaCambiar.getData().setContrasena(nueva_contrasena)
        with open("Password.txt", "w") as archivo:
            c = Sistema.getContrasenas().First()
            for j in range(Sistema.getContrasenas().size()):
                archivo.write(f"{c.getData().getIdC()} {c.getData().getContrasena()} {c.getData().getTipoUser()}")
                c = c.getNext()

class Main:
    Sistema.cargarEmpleados()
    Sistema.cargarContrasenas()
    Sistema.ordenarEmpleados(Sistema.getEmpleados())

    @staticmethod
    def main_loop():
        while True:
            idUserInput = input("Escriba su ID: ")
            contrasenaInput = input("Por favor ingrese su contraseña: ")

            if Sistema.verificarEmpleado(idUserInput, contrasenaInput):
                nombre = Sistema.buscarEmpleado(idUserInput).getData().getNombre()
                print(f"\nBienvenid@ {nombre}")

                Sistema.cargarBandejas(idUserInput)

                tipoUser = Sistema.verificarTipoUser(idUserInput)
                if tipoUser.strip() == "administrador":
                    print("Hola administrador")
                    admin = Administrador(nombre, idUserInput)
                    while True:
                        print("\nMenu:"
                              "\n1.Registrar nuevo usuario"
                              "\n2.Cambiar contraseñas"
                              "\n3.Eliminar usuario"
                              "\n4.Ver bandeja de entrada"
                              "\n5.Enviar mensaje"
                              "\n6.Salir")
                        opcion = input("Escriba el número: ")
                        if opcion == "1":
                            print("\nEligió registrar nuevo usuario")
                            nom = input("Nombre: ")
                            id1 = input("Id: ")
                            fechaNaci = input("Fecha Nacimiento formato DD/MM/AA: ")
                            cn = input("Ciudad Nacimiento: ")
                            tel = input("Telefono: ")
                            email = input("Email: ")

                            print("Por favor dar la información de la dirección detallada")
                            calle = input("Calle: ")
                            nomen = input("Nomenclatura: ")
                            barrio = input("Barrio: ")
                            ciudad = input("Ciudad: ")
                            edificio = input("Edificio: ")
                            apto = input("Apto: ")
                            contrasena = input("Establezca la contraseña: ")
                            admin.registrar_usuario(nom, id1, fechaNaci, cn, tel, email, calle, nomen, barrio, ciudad,
                                                    edificio, apto,contrasena)

                        elif opcion == "2":
                            print("\nEligió cambiar contraseñas")
                            id2 = input("Escriba el id del Usuario: ")
                            nueva_contrasena = input("Escriba la nueva contrasena: ")
                            admin.cambiar_contrasena(id2,nueva_contrasena)

                        elif opcion == "3":
                            print("\nEligió eliminar usuario")
                            id3 = input("Escriba el id: ")
                            admin.eliminar_usuario(id3)

                        elif opcion == "4":
                            print("Esta es su bandeja de entrada")
                            Sistema.verBandeja(idUserInput)

                        elif opcion == "5":
                            print("\nRedactar nuevo mensaje")
                            idDestino = input("Cedula destinatario: ")
                            titulo = input("Titulo: ")
                            contenido = input("Contenido: ")
                            Sistema.crearMensaje(idUserInput, idDestino, titulo, contenido)

                        elif opcion == "6":
                            print("Gracias por usar nuestro sistema")
                            break

                elif tipoUser.strip() == "empleado":
                    print("Hola empleado")
                    while True:
                        print("\nMenu:"
                              "\n1.Ver bandeja de entrada"
                              "\n2.Enviar mensaje"
                              "\n3.Salir")
                        opcion = input("Escriba el número: ")
                        if opcion == "1":
                            print("Esta es su bandeja de entrada")
                            Sistema.verBandeja(idUserInput)
                        if opcion == "2":
                            print("\nRedactar nuevo mensaje")
                            idDestino = input("Cedula destinatario: ")
                            titulo = input("Titulo: ")
                            contenido = input("Contenido: ")
                            Sistema.crearMensaje(idUserInput,idDestino,titulo,contenido)
                        if opcion == "3":
                            print("Gracias por usar nuestro sistema")
                            break
                break
            else:
                print("\nInformación incorrecta, vuelva a intentarlo")
if __name__ == "__main__":
    Main.main_loop()




































"""def ordenaInsercionId(lista):
    elemento = lista.First().getNext()
    for i in range(lista.size()-1):
        temp = elemento.getData()
        j = elemento
        while j != lista.First() and j.getPrev().getData().getId() > temp.getId():
            j.setData(j.getPrev().getData())
            j = j.getPrev()
        j.setData(temp)
        elemento = elemento.getNext()
#ordenaInsercionId(coleccionEmpleados)"""
