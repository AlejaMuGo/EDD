from Lab2 import Usuario
from Lab3 import Agenda


class Node:
    def __init__(self, e):
        self._data = e
        self._next = None

    def setData(self, e):
        self._data = e

    def setNext(self, n):
        self._next = n

    def getData(self):
        return self._data

    def getNext(self):
        return self._next


class List:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def setSize(self, s):
        self._size = s

    def First(self):
        return self._head

    def Last(self):
        return self._tail

    def addFirst(self, e):
        n = Node(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            n.setNext(self._head)
            self._head = n
        self._size += 1

    def addLast(self, e):
        n = Node(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            self._tail.setNext(n)
            self._tail = n
        self._size += 1

    def removeFirst(self):
        if not self.isEmpty():
            temp = self._head
            self._head = temp.getNext()
            temp.setNext(None)
            self._size -= 1
            return temp.getData()
        else:
            return None

    def removeLast(self):
        if self._size == 1:
            return self.removeFirst()
        else:
            temp = self._tail
            anterior = self._head
            while anterior.getNext() != self._tail:
                anterior = anterior.getNext()
            anterior.setNext(None)
            self._tail = anterior
            self._size -= 1
            return temp.getData()


class DoubleNode:
    def __init__(self, d):
        self._data = d
        self._prev = None
        self._next = None

    def setData(self, d):
        self._data = d

    def setNext(self, n):
        self._next = n

    def setPrev(self, p):
        self._prev = p

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def getPrev(self):
        return self._prev


class DoubleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def setSize(self, s):
        self._size = s

    def First(self):
        return self._head

    def Last(self):
        return self._tail

    def addFirst(self, e):
        n = DoubleNode(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            n.setNext(self._head)
            self._head.setPrev(n)
            self._head = n
        self._size += 1

    def addLast(self, e):
        n = DoubleNode(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            self._tail.setNext(n)
            n.setPrev(self._tail)
            self._tail = n
        self._size += 1

    def removeFirst(self):
        if self.isEmpty() == False:
            temp = self._head
            self._head = temp.getNext()
            temp.setNext(None)
            self._head.setPrev(None)
            self._size -= 1
            return temp.getData()
        else:
            return None

    def removeLast(self):
        if self._size == 1:
            return self.removeFirst()
        else:
            temp = self._tail
            self._tail = temp.getPrev()
            self._tail.setNext(None)
            temp.setPrev(None)
            self._size -= 1
            return temp.getData()

    def remove(self, nodo):
        if nodo == self._head:
            return self.removeFirst()
        elif nodo == self._tail:
            return self.removeLast()
        else:
            prevNodo = nodo.getPrev()
            nextNodo = nodo.getNext()
            prevNodo.setNext(nextNodo)
            nextNodo.setPrev(prevNodo)
            nodo.setNext(None)
            nodo.setPrev(None)
            self._size -= 1
            return nodo.getData()

    def addAfter(self, nodo, valor):
        if nodo == self._tail:
            self.addLast(valor)
        else:
            nuevoNodo = DoubleNode(valor)
            nextNodo = nodo.getNext()
            nodo.setNext(nuevoNodo)
            nuevoNodo.setNext(nextNodo)
            nextNodo.setPrev(nuevoNodo)
            nuevoNodo.setPrev(nodo)
            self._size += 1

    def addBefore(self, nodo, valor):
        if nodo == self._head:
            self.addFirst(valor)
        else:
            nuevoNodo = DoubleNode(valor)
            prevNodo = nodo.getPrev()
            nodo.setPrev(nuevoNodo)
            nuevoNodo.setPrev(prevNodo)
            prevNodo.setNext(nuevoNodo)
            nuevoNodo.setNext(nodo)
            self._size += 1


def listaSimplePares(inicio, fin):
    simplePares = List()
    for i in range(inicio, fin + 1):
        if i % 2 == 0:
            simplePares.addLast(i)
    elemento = simplePares.First()
    print("Lista simple números pares:")
    for j in range(simplePares.size()):
        print(elemento.getData())
        elemento = elemento.getNext()
    print("Nueva lista:")
    simplePares.removeFirst()
    simplePares.removeLast()

    def buscarnodo(numero):
        n = simplePares.First()
        for i in range(simplePares.size()):
            if n.getData() == numero:
                return n
            n = n.getNext()

    def eliminarNodo(numero):
        elemento = simplePares.First()
        anterior = elemento
        s = simplePares.size()
        x = 0
        y = 1
        while x < s:
            if x+1 == y and x != 0 and x!= 1:
                anterior = anterior.getNext()
            if numero == simplePares.First().getData():
                simplePares.removeFirst()
                break
            elif numero == simplePares.Last().getData():
                simplePares.removeLast()
                break
            elif elemento.getData() == numero:
                anterior.setNext(elemento.getNext())
                s -= 1
                simplePares.setSize(s)
                break
            x += 1
            y += 1
            elemento = elemento.getNext()

    eliminarNodo(10)
    elemento = simplePares.First()
    for j in range(simplePares.size()):
        print(elemento.getData())
        elemento = elemento.getNext()


def listaDoblePares(inicio, fin):
    doblePares = DoubleList()
    for i in range(inicio, fin + 1):
        if i % 2 == 0:
            doblePares.addLast(i)
    elemento = doblePares.First()
    print("\nLista doble números pares:")
    for j in range(doblePares.size()):
        print(elemento.getData())
        elemento = elemento.getNext()
    print("Nueva lista:")
    doblePares.removeFirst()
    doblePares.removeLast()

    def buscarnodo(numero):
        n = doblePares.First()
        for i in range(doblePares.size()):
            if n.getData() == numero:
                return n
            n = n.getNext()

    doblePares.remove(buscarnodo(10))
    elemento = doblePares.First()
    for h in range(doblePares.size()):
        print(elemento.getData())
        elemento = elemento.getNext()


#listaSimplePares(1, 20)
#listaDoblePares(1, 20)

u1 = Usuario("Aleja Munoz", 1000557085)
u2 = Usuario("Marysol Gonzalez", 43555206)
u3 = Usuario("Miguel Botina", 16705185)
u4 = Usuario("Laura Muñoz", 1000345223)
u5 = Usuario("Juan Largo", 1000123456)


def coleccionsimple():
    simpleUsuarios = List()
    simpleUsuarios.addLast(u1)
    simpleUsuarios.addLast(u2)
    simpleUsuarios.addLast(u3)
    simpleUsuarios.addLast(u4)
    simpleUsuarios.addLast(u5)
    elemento = simpleUsuarios.First()
    print("Coleccion simple de usuarios:")
    for i in range(simpleUsuarios.size()):
        print(elemento.getData())
        elemento = elemento.getNext()
    print("\nEscriba los datos para el nuevo usuario que se insertará al principio de la lista")
    nombre1 = input("nombre primer usuario: ")
    id1 = input("id primer usuario: ")
    print("\nEscriba los datos para el nuevo usuario que se insertará al final de la lista")
    nombre2 = input("nombre último usuario: ")
    id2 = input("id último usuario: ")
    nuevo1 = Usuario(nombre1, id1)
    nuevo2 = Usuario(nombre2, id2)
    simpleUsuarios.addFirst(nuevo1)
    simpleUsuarios.addLast(nuevo2)
    elemento = simpleUsuarios.First()
    print("\nNueva coleccion simple de usuarios:")
    for i in range(simpleUsuarios.size()):
        print(elemento.getData())
        elemento = elemento.getNext()


def coleccionDoble():
    dobleUsuarios = DoubleList()
    dobleUsuarios.addLast(u1)
    dobleUsuarios.addLast(u2)
    dobleUsuarios.addLast(u3)
    dobleUsuarios.addLast(u4)
    dobleUsuarios.addLast(u5)
    elemento = dobleUsuarios.First()
    print("\nColección doble de usuarios:")
    for i in range(dobleUsuarios.size()):
        print(elemento.getData())
        elemento = elemento.getNext()
    print("\nEscriba los datos para el nuevo usuario que se insertará al principio de la lista")
    nombre1 = input("nombre primer usuario: ")
    id1 = input("id primer usuario: ")
    print("\nEscriba los datos para el nuevo usuario que se insertará al final de la lista")
    nombre2 = input("nombre último usuario: ")
    id2 = input("id último usuario: ")
    print("\nEscriba los datos para el nuevo usuario que se insertará en el cuarto lugar de la lista")
    nombre4 = input("nombre: ")
    id4 = input("id: ")
    nuevo1 = Usuario(nombre1, id1)
    nuevo2 = Usuario(nombre2, id2)
    nuevo4 = Usuario(nombre4, id4)
    dobleUsuarios.addFirst(nuevo1)
    dobleUsuarios.addLast(nuevo2)

    def buscarNodo(usuario):
        n = dobleUsuarios.First()
        for i in range(dobleUsuarios.size()):
            if n.getData() == usuario:
                return n
            n = n.getNext()

    dobleUsuarios.addAfter(buscarNodo(u2), nuevo4)
    elemento = dobleUsuarios.First()
    print("\nNueva coleccion doble de usuarios:")
    for i in range(dobleUsuarios.size()):
        print(elemento.getData())
        elemento = elemento.getNext()
#coleccionsimple()
#coleccionDoble()