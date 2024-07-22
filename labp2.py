#PUNTO 2
archivo = open("test_pr2.txt")
contador = 0
for linea in archivo:
    palabras = linea.split(" ")
    for j in palabras:
        if j == "en":
            contador+=1
print(f"La palabra en se repite {contador} veces")