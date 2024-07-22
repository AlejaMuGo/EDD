#PUNTO 1
n = int(input(""))
listaNum = []
suma=0
for i in range(n):
    num= int(input(""))
    listaNum.append(num)
max=listaNum[0]
min=listaNum[0]
for j in range(n):
    suma += listaNum[j]
    if listaNum[j]>max:
        max=listaNum[j]
    if listaNum[j]<min:
        min = listaNum[j]
    else:
        max=max
        min=min
promedio = suma/n
print(f"El número máximo es {max}")
print(f"El número mínimo es {min}")
print(f"La suma de los enteros ingresados es {suma}")
print(f"El promedio es {promedio}")
