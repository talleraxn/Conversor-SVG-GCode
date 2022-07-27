"""             Convierte Archivos .SVG a .GCode
Buscando circulos ( ellipse) y mueve el cabezal al centro del mismo para depositar una pieza convirtiendo a instrucciones de GCode        
        
        EN PROCESO        
"""
from tkinter import N, Place
from traceback import print_list

Nombre_Archivo_SVG="Circulos.svg"
Nombre_Archivo_Gcode=Nombre_Archivo_SVG[:-3]+"gcode"

archivo_SVG = open(Nombre_Archivo_SVG, "r")
Contenido_SVG=[]
Contenido_SVG=archivo_SVG.readlines()
archivo_SVG.close()

archivo_inicio_gcode = open("Inicio.gcode", "r")
inicio_gcode=[]
inicio_gcode=archivo_inicio_gcode.readlines()
archivo_inicio_gcode.close()


archivo_fin_gcode = open("Fin.gcode", "r")
fin_gcode=[]
fin_gcode=archivo_fin_gcode.readlines()
archivo_fin_gcode.close()

Lista_Puntos=[]
Linea_Numero=0


for Linea_Numero in range (0, len(Contenido_SVG)-1):
    
    if 'ellipse' in Contenido_SVG[Linea_Numero]:

        Lista_Puntos.append(Contenido_SVG[Linea_Numero+3])
        Lista_Puntos.append(Contenido_SVG[Linea_Numero+4])

        Linea_Numero = Linea_Numero+4
    Linea_Numero +=1


print (len(Lista_Puntos))

with open(Nombre_Archivo_Gcode,"w") as Archivo_Gcode:
    
    Linea_Numero=0
    for Linea in range (0, len(inicio_gcode)-1):
        Archivo_Gcode.write(inicio_gcode[Linea_Numero])
        Linea_Numero = Linea_Numero + 1
    
    Linea_Numero=0
    for Linea_Numero in range (0, len(Lista_Puntos)-1):
        Posicion_X=Lista_Puntos[Linea_Numero]
        Posicion_Y=Lista_Puntos[Linea_Numero + 1]
        Lista_Puntos[Linea_Numero]="G0 F1000 X"+ Posicion_X[11:-2] +" Y"+ Posicion_Y[11:-2] +"\n"
        print (Lista_Puntos[Linea_Numero])
        Archivo_Gcode.write(Lista_Puntos[Linea_Numero])
        Linea_Numero = Linea_Numero + 2

    Archivo_Gcode.write("\n")
    Linea_Numero=0
    for Linea_Numero in range (0, len(fin_gcode)-1):
        Archivo_Gcode.write(fin_gcode[Linea_Numero])
        Linea_Numero = Linea_Numero + 1
