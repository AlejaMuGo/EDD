class Fecha:
    def __init__(self,dd,mm,aa):
        self._dd = dd
        self._mm = mm
        self._aa = aa
    def setDia(self, dd):
        self._dd = dd
    def setMes(self, mm):
        self._mm = mm
    def setA(self, aa):
        self._aa = aa
    def getDia(self):
        return self._dd
    def getMes(self):
        return self._mm
    def getA(self):
        return self._aa
    def __str__(self):
        return f"{self._dd} {self._mm} {self._aa}"

class Direccion:
    def __init__(self,c,n,b,ci,e,a):
        self._calle = c
        self._nomenclatura= n
        self._barrio = b
        self._ciudad = ci
        self._edificio = e
        self._apto = a
    def setCalle(self, c):
        self._calle = c
    def setNomenclatura(self, n):
        self._nomenclatura = n
    def setBarrio(self, b):
        self._barrio = b
    def setCiudad(self, ci):
        self._ciudad = ci
    def setEdificio(self, e):
        self._edificio = e
    def setApto(self, a):
        self._apto = a
    def getCalle(self):
        return self._calle
    def getNomenclatura(self):
        return self._nomenclatura
    def getBarrio(self, b):
        return self._barrio
    def getCiudad(self):
        return self._ciudad
    def getEdificio(self):
        return self._edificio
    def getApto(self):
        return self._apto
    def __str__(self):
        return f"{self._calle} {self._nomenclatura} {self._barrio} {self._ciudad} {self._edificio} {self._apto}"

class Usuario:
    def __init__(self, n, id):
        self._nombre = n
        self._id = id
        self._ciudad_nacimiento = None
        self._tel = None
        self._email = None
        self._fecha_nacimiento = None
        self._dir = None
    def setNombre(self, n):
        self._nombre = n
    def setId(self, id):
        self._id = id
    def setCiudad_nacimiento(self, c):
        self._ciudad_nacimiento = c
    def setTel(self, t):
        self._tel = t
    def setEmail(self, e):
        self._email = e
    def setFecha_nacimiento(self, dd, mm, aa):
        self._fecha_nacimiento = Fecha(dd,mm,aa)
    def setDir(self,c,n,b,ci,e,a):
        self._dir = Direccion(c,n,b,ci,e,a)
    def getNombre(self):
        return self._nombre
    def getId(self):
        return self._id
    def getCiudad_nacimiento(self):
        return self._ciudad_nacimiento
    def getTel(self):
        return self._tel
    def getEmail(self):
        return self._email
    def getFecha_nacimiento(self):
        return self._fecha_nacimiento
    def getDir(self):
        return self._dir
    def __str__(self):
        return f"{self._nombre}-{self._id}-{self._fecha_nacimiento}-{self._ciudad_nacimiento}-{self._tel}-{self._email}-{self._dir}"

fecha1 = Fecha(13,"Mayo",2003)
#print(fecha1)
dir1 = Direccion("Carrera 47","1-95","El poblado","Medellin","El futuro","402")
#print(dir1)
usuario1 = Usuario("Alejandra","102")
usuario1.setFecha_nacimiento(13,"Mayo",2003)
usuario1.setCiudad_nacimiento("Medellin")
usuario1.setTel(3163956435)
usuario1.setEmail("mamunozgo@unal.edu.co")
usuario1.setDir("Carrera 47","1-95","El poblado","Medellin","El futuro","402")
#print(usuario1)

def programaPrincipal():
    print("Por favor llenar los siguientes datos")
    nombre = input("Nombre: ")
    id = input("Id: ")
    cn = input("Ciudad Nacimiento: ")
    tel = input("Telefono: ")
    email = input("Email: ")
    diaN = input("Dia Nacimiento: ")
    mesN = input("Mes Nacimiento: ")
    aN = input("Año Nacimiento: ")
    print("Por favor dar la información de la dirección detallada")
    c = input("Calle: ")
    n = input("Nomenclatura: ")
    b = input("Barrio: ")
    ci = input("Ciudad: ")
    e = input("Edificio: ")
    a = input("Apto: ")

    usuario2 = Usuario(nombre,id)
    usuario2.setCiudad_nacimiento(cn)
    usuario2.setTel(tel)
    usuario2.setEmail(email)
    usuario2.setFecha_nacimiento(diaN,mesN,aN)
    usuario2.setDir(c,n,b,ci,e,a)
    print(usuario2)

