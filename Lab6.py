from Lab4 import List
from Lab2 import Usuario

class Stack:
    def __init__(self):
        self._data= List()
    def size(self):
        return self._data.size()
    def isEmpty(self):
        if self._data.size() == 0:
            return True
        else:
            return False
    def push(self, e):
        self._data.addFirst(e)
    def pop(self):
        if self.isEmpty():
            return None
        temp = self._data.First()
        self._data.removeFirst()
        return temp.getData()
    def top(self):
        if not isEmpty():
            return self._data.First().getData()
        else:
            return None

class Queue:
    def __init__(self):
        self._data= List()
    def size(self):
        return self._data.size()
    def isEmpty(self):
        if self._data.size() == 0:
            return True
        else:
            return False
    def enqueue(self,e):
        self._data.addLast(e)
    def dequeue(self):
        temp = self._data.First()
        self._data.removeFirst()
        return temp.getData()
    def First(self):
        return self._data.First()

class TurnoUsuario():
    def __init__(self):
        self._registro = Queue()
        self._usuarioAtendidos = Stack()
    def registrar(self,u):
        self._registro.enqueue(u)
    def atenderSiguiente(self):
        u = self._registro.dequeue()
        self._usuarioAtendidos.push(u)
    def toFile(self):
        with open("usuariospendientes.txt","w") as archivo:
            elemento = self._registro.First()
            while elemento is not None:
                usuario = elemento.getData()
                archivo.write(f"{usuario.getNombre()} {usuario.getId()}\n")
                elemento = elemento.getNext()
        with open("usuariosatendidos.txt","w") as archivo1:
            while not self._usuarioAtendidos.isEmpty():
                user = self._usuarioAtendidos.pop()
                archivo1.write(f"{user.getNombre()} {user.getId()}\n")
def Main():
    print("Bienvenid@ al sistema de atención")
    turnos = TurnoUsuario()
    x = 0
    while True:
        x += 1
        print(f"Usuario #{x}")
        nombre = input("Ingrese su nombre: ")
        id = input("Ingrese su id: ")
        usuario = Usuario(nombre, id)
        turnos.registrar(usuario)

        if x == 5:
            turnos.toFile()
            break
    turnos.atenderSiguiente()
    turnos.atenderSiguiente()
    turnos.toFile()
Main()

def pila():
    pilaEnteros = Stack()
    pilaEnteros.push(2)
    pilaEnteros.push(4)
    pilaEnteros.push(6)
    pilaEnteros.push(8)
    pilaEnteros.push(10)
    print("Pila")
    while not pilaEnteros.isEmpty():
        print(pilaEnteros.pop())
#pila()

def cola():
    colaEnteros = Queue()
    colaEnteros.enqueue(2)
    colaEnteros.enqueue(4)
    colaEnteros.enqueue(6)
    colaEnteros.enqueue(8)
    colaEnteros.enqueue(10)
    print("\nCola")
    while not colaEnteros.isEmpty():
        print(colaEnteros.dequeue())
#cola()