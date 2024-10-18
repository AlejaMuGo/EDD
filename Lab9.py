import math
import random
from Lab4 import DoubleList
from Lab4 import DoubleNode
from Lab2 import Usuario
class Entry:
    def __init__(self, key, dato):
        self.key = key
        self.dato = dato
class Chained_Hash:
    def __init__(self, m, funcion):
        self._m = m
        self._funcion = funcion
        self._tabla = [DoubleList() for _ in range(m)]
        self._A = (math.sqrt(5)-1) / 2

    def hash(self, k):
        if self._funcion == "division":
            return k % self._m
        elif self._funcion == "multiplicacion":
            return int(self._m * ((k * self._A) % 1))

    def insertar(self, key, dato):
        i = self.hash(key)
        entry = Entry(key, dato)
        nodo = DoubleNode(entry)
        self._tabla[i].addLast(nodo)

    def buscar(self, key):
        i = self.hash(key)
        nodo = self._tabla[i].First()
        while nodo is not None:
            entry = nodo.getData()
            if entry.getData().key == key:
                return entry.getData().dato
            nodo = nodo.getNext()
        return None

    def eliminar(self, key):
        i = self.hash(key)
        nodo = self._tabla[i].First()
        while nodo is not None:
            entry = nodo.getData()
            if entry.getData().key == key:
                self._tabla[i].remove(nodo)
                return True
            nodo = nodo.getNext()
        return False

    def contarUsuarios(self):
        numUsers = [0] * self._m
        for i in range(self._m):
            numUsers[i] = self._tabla[i].size()
        return numUsers

def prueba1():
    numerosAl = [43, 16, 27, 67, 40, 49, 61, 58, 15, 63, 21, 54, 88, 52, 25, 18, 79, 31, 24, 66]
    print(numerosAl)
    print("\nUsando funcion division")
    tablaHashDiv = Chained_Hash(10,"division")
    for num in numerosAl:
        tablaHashDiv.insertar(num,num)
    number = 21
    numBuscado= tablaHashDiv.buscar(number)
    print(f"Buscando {number}: {'Encontrado' if numBuscado is not None else 'No encontrado'}")
    numEliminado = tablaHashDiv.eliminar(number)
    print(f"Eliminando {number}: {'Eliminado' if numEliminado else 'No encontrado'}")
    numBuscado = tablaHashDiv.buscar(number)
    print(f"Buscando {number}: {'Encontrado' if numBuscado is not None else 'No encontrado'}")

    print("\nUsando funcion multiplicacion")
    tablaHashMulti = Chained_Hash(10, "multiplicacion")
    for num in numerosAl:
        tablaHashMulti.insertar(num,num)
    number1 = 43
    numBuscado = tablaHashMulti.buscar(number1)
    print(f"Buscando {number1}: {'Encontrado' if numBuscado is not None else 'No encontrado'}")
    numEliminado = tablaHashMulti.eliminar(number1)
    print(f"Eliminando {number1}: {'Eliminado' if numEliminado else 'No encontrado'}")
    numBuscado = tablaHashMulti.buscar(number1)
    print(f"Buscando {number1}: {'Encontrado' if numBuscado is not None else 'No encontrado'}")
prueba1()


def prueba2():
    usuarios = [
        Usuario("Aleja",1),
        Usuario("Juan",2),
        Usuario("Jose",3),
        Usuario("Aura",4),
        Usuario("Paula",5),
        Usuario("Sofia",6)
    ]

    print("\nUsuarios insertados usando la función de división...")
    tablaHashDiv = Chained_Hash(5, "division")
    for usuario in usuarios:
        tablaHashDiv.insertar(usuario._id, usuario)

    listaDiv = tablaHashDiv.contarUsuarios()
    for i in range(len(listaDiv)):
        print(f"{i}: {listaDiv[i]} usuarios")

    print("\nUsuarios insertados usando la función de multiplicación...")
    tablaHashMulti = Chained_Hash(5, "multiplicacion")
    for usuario in usuarios:
        tablaHashMulti.insertar(usuario._id, usuario)

    listaMul = tablaHashDiv.contarUsuarios()
    for i in range(len(listaMul)):
        print(f"{i}: {listaMul[i]} usuarios")
prueba2()