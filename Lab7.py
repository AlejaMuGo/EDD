import math
import random
class Heap:
    def __init__(self):
        self._A = []
        self._size = 0
    def parent(self, i):
        return math.ceil(i/2)-1
    def left(self, i):
        return (2*i)+1
    def right(self, i):
        return (2*i)+2
    def maxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self._size and self._A[l] > self._A[i]:
            largest = l
        else:
            largest = i
        if r < self._size and self._A[r] > self._A[largest]:
            largest = r
        if largest != i:
            self._A[i], self._A[largest] = self._A[largest], self._A[i]
            self.maxHeapify(largest)
    def buildMaxHeap(self, B):
        self._A = B
        self._size = len(B)
        for i in range(self._size // 2 - 1, -1, -1):
            self.maxHeapify(i)
    def heapSort(self):
        self.buildMaxHeap(self._A)
        for i in range((len(self._A)-1), -1, -1):
            temp = self._A[i]
            self._A[i] = self._A[0]
            self._A[0] = temp
            self._size -= 1
            self.maxHeapify(0)
        return self._A
class PriorityQueue(Heap):
    def maxHeapInsert(self, k):
        self._size += 1
        i = self._size-1
        self._A.append(k)
        while i > 0 and self._A[self.parent(i)] < self._A[i]:
            self._A[self.parent(i)], self._A[i] = self._A[i], self._A[self.parent(i)]
            i = self.parent(i)
    def heapExtractMax(self):
        max = self._A[0]
        self._A[0] = self._A[self._size-1]
        self._size -= 1
        self.maxHeapify(0)
        return max
    def heapMaximum(self):
        return self._A[0]

arreglo = random.sample(range(1,100),6)
print(f"Arreglo original: {arreglo}")

heap = Heap()
heap.buildMaxHeap(arreglo.copy())
print(f"Max Heap: {heap._A}")

arreglo_ordenado = heap.heapSort()
print(f"Arreglo ordenado: {arreglo_ordenado}")

priorityQueue = PriorityQueue()
for num in arreglo:
    priorityQueue.maxHeapInsert(num)
priorityQueue.maxHeapInsert(13)
priorityQueue.maxHeapInsert(100)
print(f"heap con nuevos elementos: {priorityQueue._A}")
print(f"Valor maximo eliminado: {priorityQueue.heapExtractMax()}")
print(f"nuevo heap: {priorityQueue._A}")
print(f"El nuevo maximo es: {priorityQueue.heapMaximum()}")
