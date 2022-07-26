from tkinter import N
from traceback import print_list

Nombre_Archivo_SVG="Circulos.svg"
Nombre_Archivo_Gcode=Nombre_Archivo_SVG[:-3]+"gcode"

print (Nombre_Archivo_SVG,Nombre_Archivo_Gcode)

archivo_SVG = open(Nombre_Archivo_SVG, "r")
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

with open(Nombre_Archivo_Gcode,"w") as Archivo_Gcode:
    for Linea in Lista_Puntos:
        print (Lista_Puntos[Linea_Numero])
        Archivo_Gcode.write(Lista_Puntos[Linea_Numero])
        Linea_Numero = Linea_Numero + 1
    