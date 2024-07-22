from Lab2 import Usuario
class Agenda:
    user = Usuario("", 0)
    def __init__(self, capacity):
        self._capacity = capacity
        self._registro = [None] * self._capacity
        self._no_reg = 0

    def agregar(self,u):
        if self._no_reg < self._capacity:
            if self.buscar(u.getId()) == -1:
                self._registro[self._no_reg] = u
                self._no_reg += 1
                return True
            else:
                print("No se puede agregar nuevamente el usuario")
                return False
        else:
            print("La agenda esá llena")

    def buscar(self, id):
        for i in range(self._capacity):
            user = self._registro[i]
            if user == None:
                return -1
            if user.getId() == id:
                return i
        return -1

    def eliminar(self, id):
        inx = self.buscar(id)

        if inx != -1:
            temp = self._registro[inx]
            for i in range(inx, self._no_reg-1):
                self._registro[i] = self._registro[i+1]
            self._registro[self._no_reg-1] = None
            self._no_reg -= 1
            return True
        else:
            return False
    def toFile(self,a):
        archivo = open(f"{a}.txt","w")
        for i in range(self._no_reg):
            archivo.write(f"{self._registro[i]}\n")
    def importar(self,a):
        archivo = open(f"{a}.txt", "r")
        for linea in archivo:
            user = linea.split("-")
            fecha = user[2].split("/")
            direc = user[-1].split(",")
            direc[-1] = direc[-1].replace("\n", "")
            u1 = Usuario(user[0], int(user[1]))
            u1.setFecha_nacimiento(int(fecha[0]), fecha[1], int(fecha[2]))
            u1.setCiudad_nacimiento(user[3])
            u1.setTel(user[4])
            u1.setEmail(user[5])
            u1.setDir(direc[0],direc[1],direc[2],direc[3],direc[4],direc[5])
            self.agregar(u1)

    def getRegistro(self):
        return self._registro
    def getNo_reg(self):
        return self._no_reg

def main1():
    agenda = Agenda(5)
    u1 = Usuario("Aleja Munoz", 1000557085)
    u1.setFecha_nacimiento(13, "Mayo", 2003)
    u1.setCiudad_nacimiento("Medellin")
    u1.setTel(3163956435)
    u1.setEmail("rusheraleja@gmail.com")
    u1.setDir("Carrera 47","1 95","El poblado","Medellin","El futuro","402")
    u2 = Usuario("Marysol Gonzalez", 43555206)
    u2.setFecha_nacimiento(30, "Marzo", 1971)
    u2.setCiudad_nacimiento("Abejorral")
    u2.setTel(3105399161)
    u2.setEmail("marysolgd@gmail.com")
    u2.setDir("Carrera 50", "3 21", "Belen", "Medellin", "Edificio Girasoles", "202")
    u3 = Usuario("Miguel Botina", 16705185)
    u3.setFecha_nacimiento(22, "Septiembre", 1964)
    u3.setCiudad_nacimiento("Cali")
    u3.setTel(3187946009)
    u3.setEmail("sietemam@gmail.com")
    u3.setDir("Calle 10", "1 82", "Laureles", "Medellin", "pieMonte", "403")
    u4 = Usuario("Laura Duque", 1000345223)
    u4.setFecha_nacimiento(17, "Junio", 1995)
    u4.setCiudad_nacimiento("Medellin")
    u4.setTel(3173745336)
    u4.setEmail("lauradanielamg@gmail.com")
    u4.setDir("Carrera 72", "16 15", "Belen", "Medellin", "Rafael Uribe Uribe", "302")
    u5 = Usuario("Juan Largo", 1000123456)
    u5.setFecha_nacimiento(16, "Julio", 2005)
    u5.setCiudad_nacimiento("Codazzi")
    u5.setTel(3136566689)
    u5.setEmail("jclargobuenahora@gmail.com")
    u5.setDir("Calle 18", "2 12", "Robledo", "Medellin", "Altos de Robledo", "105")

    agenda.agregar(u1)
    agenda.agregar(u2)
    agenda.agregar(u3)
    agenda.agregar(u4)
    agenda.agregar(u5)

    print(f"La posición donde se encuentra almacenado es: {agenda.buscar(43555206)}")
    agenda.toFile("Agenda")

def main2():
    agenda2 = Agenda(5)
    agenda2.importar("Agenda")
    for usuario in agenda2.getRegistro():
        print(usuario)
    agenda2.eliminar(1000557085)
    agenda2.toFile("Agenda2")


