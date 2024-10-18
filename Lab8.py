from Lab6 import Queue
class Node:
    def __init__(self, e):
        self.data = e
        self.left = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setData(self, data):
        self.data = data

class ArbolBinario:
    def __init__(self):
        self._root = None
        self._size = 0

    def getSize(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def isRoot(self, v):
        return v == self._root

    def hasLeft(self, v):
        return v.getLeft() != None

    def hasRight(self, v):
        return v.getRight() != None

    def isInternal(self, v):
        return self.hasLeft(v) or self.hasRight(v)

    def left(self, v):
        return v.getLeft()

    def right(self, v):
        return v.getRight()

    def parent(self, v):
        if self.isRoot(v):
            return None
        else:
            Q = Queue()
            Q.enqueue(self._root)
            temp = self._root
        while not Q.isEmpty():
            temp = Q.dequeue()
            if self.left(temp) == v or self.right(temp) == v:
                return temp
            if self.hasLeft(temp):
                Q.enqueue(self.left(temp))
            if self.hasRight(temp):
                Q.enqueue(self.right(temp))

    def depth(self, v):
        if self.isRoot(v):
            return 0
        else:
            return 1 + self.depth(self.parent(v))

    def height(self, v):
        if v is None:
            return -1
        if not self.isInternal(v):
            return 0
        else:
            h = max(self.height(self.left(v)), self.height(self.right(v)))
            return 1 + h
    def addRoot(self, e):
        self._root = Node(e)
        self._size = 1
    def insertLeft(self,v,e):
        left = Node(e)
        v.setLeft(left)
        self._size += 1
    def insertRight(self,v,e):
        right = Node(e)
        v.setRight(right)
        self._size += 1
    def remove(self,v):
        p = self.parent(v)
        if self.hasLeft(v) or self.hasRight(v):
            if self.hasLeft(v):
                child = self.left(v)
            else:
                child = self.right(v)
            if self.left(p) == v:
                p.setLeft(child)
            else:
                p.setRight(child)
            v.setLeft(None)
            v.setRight(None)
        else:
            if self.left(p) == v:
                p.setLeft(None)
            else:
                p.setRight(None)
        self._size -=1

class BSTEntry():
    def __init__(self, data, key):
        self._data = data
        self._key = key

    def getData(self):
        return self._data
    def getKey(self):
        return self._key
    def setData(self, data):
        self._data = data
    def setKey(self, key):
        self._key = key

class ABB(ArbolBinario):
    def __init__(self):
        super().__init__()
    def searchTree(self,key,v):
        if v is None:
            return None
        u = v.getData()
        if key == u.getKey():
            return v
        elif key < u.getKey():
            return self.searchTree(key, v.getLeft())
        else:
            return self.searchTree(key, v.getRight())
    def find(self,k):
        return self.searchTree(k, self._root)
    def addEntry(self,v,o):
        temp = v.getData()
        nD = Node(o)
        if o.getKey() < temp.getKey():
            if self.hasLeft(v):
                self.addEntry(self.left(v), o)
            else:
                v.setLeft(nD)
        else:
            if self.hasRight(v):
                self.addEntry(self.right(v), o)
            else:
                v.setRight(nD)
    def insert(self,e,k):
        newEntry = BSTEntry(e,k)
        if self.isEmpty():
            self.addRoot(newEntry)
        else:
            self.addEntry(self._root,newEntry)

    def remove(self, k):
        v = self.find(k)
        if v is None:
            return None
        temp = v.getData()
        if self.hasLeft(v) and self.hasRight(v):
            w = self.predecesor(v)
            v.setData(w.getData())
            super().remove(w)
        else:
            super().remove(v)
        return temp
    def predecesor(self, v):
        temp = v.getLeft()
        return self.maxNode(temp)

    def maxNode(self, temp):
        if self.hasRight(temp):
            return self.maxNode(self.right(temp))
        else:
            return temp

    def minNode(self, temp):
        if self.hasLeft(temp):
            return self.maxNode(self.left(temp))
        else:
            return temp
    listaInorder =[]
    def inorder(self,v):
        if self.hasLeft(v):
            self.inorder(self.left(v))
        #print(v.getData().getKey())
        self.listaInorder.append(v.getData().getKey())
        if self.hasRight(v):
            self.inorder(self.right(v))
    def calcularAltura(self):
        if self._root is None:
            return 0
        return self.height(self._root)
    def mostrarArbol1(self, nodo= None, hijo="Raiz-> ",nivel=1):
        niveles = self.calcularAltura() + 1
        if nodo is None:
            nodo = self._root
        if nodo is not None:
            if hijo == "Raiz-> ":
                print(" " * 8 + hijo + str(nodo.getData().getKey()))

            if self.hasLeft(nodo) and self.hasRight(nodo):
                print(" " * (nivel*4) + "I-> " + str(self.left(nodo).getData().getKey()) + " "*(nivel*4)+ "D-> "+str(self.right(nodo).getData().getKey()))
                self.mostrarArbol1(self.left(nodo), hijo="I-> ", nivel=+1)
                self.mostrarArbol1(self.right(nodo), hijo="D-> ", nivel=+1)
            if self.hasLeft(nodo) and not self.hasRight(nodo):
                print(" " * (nivel * 4) + "I-> " + str(self.left(nodo).getData().getKey()))
                self.mostrarArbol1(self.left(nodo), hijo="I-> ", nivel=+1)
            if self.hasRight(nodo) and not self.hasLeft(nodo):
                print(" " * (nivel * 4) + "D-> " + str(self.right(nodo).getData().getKey()))
                self.mostrarArbol1(self.right(nodo), hijo="D-> ", nivel=+1)
    """def mostrarArbol2(self):
        if self._root is None:
            return
        cola1 = Queue()
        cola2 = Queue()
        cola1.enqueue(self._root)
        while not cola1.isEmpty() or not cola2.isEmpty():
            while not cola1.isEmpty():
                temp = cola1.First().getData()
                cola1.dequeue()
                print(temp.getKey(), end=" ")

                if self.hasLeft(temp.getData()):
                    cola2."""


    def mostrarArbol(self):
        nNiveles = self.height(self._root)
        ancho = pow(2, nNiveles + 1)

        cola = [(self._root, 0, ancho, 'c')]
        niveles = []

        while cola:
            nodo, nivel, x, alineacion = cola.pop(0)
            if nodo:
                if len(niveles) <= nivel:
                    niveles.append([])
                niveles[nivel].append([nodo, nivel, x, alineacion])
                segmento = ancho // (pow(2, nivel + 1))
                cola.append((nodo.getLeft(), nivel + 1, x - segmento, 'l'))
                cola.append((nodo.getRight(), nivel + 1, x + segmento, 'r'))

        for i, l in enumerate(niveles):
            pre = 0
            prelinea = 0
            lineaStr = ''
            pStr = ''
            segmento = ancho // (pow(2, i + 1))
            for n in l:
                #valorStr = str(n[0].getData().getKey())
                #valorStr = str(n[0].getData().getKey()) + str(n[0].getData().getData())
                valorStr =str(n[0].getData().getKey())+"-"+str(n[0].getData().getData().nombre)
                if n[3] == 'r':
                    lineaStr += ' ' * (n[2] - prelinea - 1 - segmento - segmento // 2) + '¯' * (
                                segmento + segmento // 2) + '\\'
                    prelinea = n[2]
                if n[3] == 'l':
                    lineaStr += ' ' * (n[2] - prelinea - 1) + '/' + '¯' * (segmento + segmento // 2)
                    prelinea = n[2] + segmento + segmento // 2
                pStr += ' ' * (n[2] - pre - len(
                    valorStr)) + valorStr  # Corregir la posición de acuerdo al tamaño del número
                pre = n[2]
            print(lineaStr)
            print(pStr)
class Usuario:
    def __init__(self,nombre,id):
        self.nombre = nombre
        self.id = id
    def calcularK(self):
        return sum(int(digito) for digito in str(self.id))
    #def __str__(self):
        #return f"{self.nombre}-{self.id}"
arbol = ABB()

usuarios = [
    Usuario("Juan", 10101013),
    Usuario("Pablo", 10001011),
    Usuario("Maria", 10101015),
    Usuario("Ana", 1010000),
    Usuario("Diana", 10111105),
    Usuario("Mateo", 10110005)
]
for user in usuarios:
    key = user.calcularK()
    arbol.insert(user,key)
#arbol.mostrarArbol1()
#arbol.mostrarArbol2()
arbol.mostrarArbol()
#arbol.remove(10)
#arbol.insert(Usuario("Jose",10004006),12)
#arbol.remove(4)
#print(f"{'Encontrado'if arbol.find(1) != None else 'No encontrado' }")
#print(f"El valor maximo es: {arbol.maxNode(arbol._root).getData().getKey()}")
#print(f"El valor minimo es: {arbol.minNode(arbol._root).getData().getKey()}")
arbol.inorder(arbol._root)
print(f"Recorrido Inorder: {'-'.join(map(str, arbol.listaInorder))}")
arbol.mostrarArbol()