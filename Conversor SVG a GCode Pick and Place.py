from tkinter import N
from traceback import print_list


archivo_SVG = open("Circulos.svg", "r")
print(archivo_SVG.readable())
#print(archivo_SVG.read())

Contenido_SVG=[]
Contenido_SVG=archivo_SVG.readlines()
archivo_SVG.close()
#Linea_Numero=1
Lista_Puntos=[]

for Linea_Numero in range (0, len(Contenido_SVG)-1):
    if 'ellipse' in Contenido_SVG[Linea_Numero]:
        Lista_Puntos.append(Contenido_SVG[Linea_Numero+3])
        Lista_Puntos.append(Contenido_SVG[Linea_Numero+4])
        Linea_Numero = Linea_Numero+4
    Linea_Numero +=1

print (len(Lista_Puntos))
Linea_Numero=0
for Linea in Lista_Puntos:
    print (Lista_Puntos[Linea_Numero])
    Linea_Numero = Linea_Numero + 1



""""
with open("Circulos.svg") as archivo:
    for linea in archivo:
        linea_x = linea.find("ellipse")
        if linea_x > -1 :
            linea_y="Pidrita"
            print(linea_y)
"""