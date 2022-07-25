archivo = open("Circulos.svg", "r")
print(archivo.readable())
print(archivo.read())


with open("Circulos.svg") as archivo:
    for linea in archivo:
        linea_x = linea.find("ellipse")
        if linea_x > -1 :
            linea_y="Pidrita"
            print(linea_y)

        