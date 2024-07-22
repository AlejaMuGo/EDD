from Lab2 import Usuario
from Lab3 import Agenda
class Node:
    def __init__(self, e):
        self._data = e
        self._next = None
    def setData(self,e):
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
    def setSize(self,s):
        self._size = s
    def First(self):
        return self._head
    def Last(self):
        return self._tail
    def addFirst(self,e):
        n = Node(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            n.setNext(self._head)
            self._head = n
        self._size += 1
    def addLast(self,e):
        n = Node(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            self._tail.setNext(n)
            self._tail = n
        self._size += 1
    def removeFirst(self):
        if self.isEmpty() == False:
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
    def setSize(self,s):
        self._size = s
    def First(self):
        return self._head
    def Last(self):
        return self._tail
    def addFirst(self,e):
        n = DoubleNode(e)
        if self.isEmpty():
            self._head = n
            self._tail = n
        else:
            n.setNext(self._head)
            self._head.setPrev(n)
            self._head = n
        self._size += 1
    def addLast(self,e):
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
        if nodo == self._head:
            nuevoNodo = DoubleNode(valor)
            nuevoNodo.setNext(nodo.getNext())
def listaSimplePares(inicio,fin):
    simplePares = List()
    for i in range(inicio, fin+1):
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
    elemento = simplePares.First()
    for j in range(simplePares.size()):
        if elemento.getData() == 10:
            elemento.setNext(None)
        print(elemento.getData())
        elemento = elemento.getNext()

def listaDoblePares(inicio,fin):
    doblePares = List()
    for i in range(inicio, fin+1):
        if i % 2 == 0:
            doblePares.addLast(i)
    elemento = doblePares.First()
    print("\nLista doble números pares:")
    for j in range(doblePares.size()):
        print(elemento.getData())
        elemento = elemento.getNext()
listaSimplePares(1,20)
listaDoblePares(1,20)
