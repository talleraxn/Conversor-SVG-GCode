"""             Convierte Archivos .SVG a .GCode
Buscando circulos ( ellipse) y mueve el cabezal al centro del mismo para depositar una pieza convirtiendo a instrucciones de GCode        
        
        EN PROCESO        
"""
from tkinter import N, Place
from traceback import print_list

Nombre_Archivo_SVG="Circulos.svg"
Nombre_Archivo_Gcode=Nombre_Archivo_SVG[:-3]+"gcode"

gcode=[]

archivo_inicio_gcode = open("Inicio.gcode", "r")
gcode=archivo_inicio_gcode.readlines()
archivo_inicio_gcode.close()

archivo_fin_gcode = open("Fin.gcode", "r")
fin_gcode=[]
fin_gcode=archivo_fin_gcode.readlines()
archivo_fin_gcode.close()

toma=[]
archivo_toma_gcode = open("Pick.gcode", "r")
toma=archivo_toma_gcode.readlines()
archivo_toma_gcode.close()

coloca=[]
archivo_coloca_gcode = open("Place.gcode", "r")
coloca=archivo_coloca_gcode.readlines()
archivo_coloca_gcode.close()

def tomar_pieza():
    instruccion_numero=0
    for instruccion_numero in range (0, len(toma)):
        gcode.append(toma[instruccion_numero])
        instruccion_numero = instruccion_numero + 1
    gcode.append("\n")
def colocar_pieza():
    instruccion_numero=0
    for instruccion_numero in range (0, len(coloca)):
        gcode.append(coloca[instruccion_numero])
        instruccion_numero = instruccion_numero + 1
    gcode.append("\n\n")

archivo_SVG = open(Nombre_Archivo_SVG, "r")
Contenido_SVG=[]
Contenido_SVG=archivo_SVG.readlines()
archivo_SVG.close()

Linea_Numero=0
for Linea_Numero in range (0, len(Contenido_SVG)-1):
    
    if 'ellipse' in Contenido_SVG[Linea_Numero]:

        Posicion_X=Contenido_SVG[Linea_Numero+3]
        Posicion_Y=Contenido_SVG[Linea_Numero+4]
        gcode.append("; ----------------------------------------------------------------- \n")
        tomar_pieza()
        gcode.append("\n"+"G0 F1000 X"+ Posicion_X[11:-2] +" Y"+ Posicion_Y[11:-2] +"\n\n")
        colocar_pieza()

        Linea_Numero = Linea_Numero+4
    Linea_Numero +=1

instruccion_numero=0
for instruccion_numero in range (0, len(fin_gcode)):
        gcode.append(fin_gcode[instruccion_numero])
        instruccion_numero = instruccion_numero + 1


with open(Nombre_Archivo_Gcode,"w") as Archivo_Gcode:
    
    Linea_Numero=0
    for Linea_Numero in range (0, len(gcode)-1):
        Archivo_Gcode.write(gcode[Linea_Numero])
        Linea_Numero = Linea_Numero + 1

