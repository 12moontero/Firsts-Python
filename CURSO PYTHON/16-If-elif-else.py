#elif Son condiciones

#TEMPERATURAS

tempertura = 26

if tempertura <= 0:
    print("Congeglado")
elif tempertura >= 0 and tempertura <= 20:
    print("Frio")
elif tempertura >= 20 and tempertura <= 30:
    print("Templado")
elif tempertura >= 40:
    print("Caliente")
else:
    print("Eso no es normal")


#Colores

color_seleccionado = "rojo"

if color_seleccionado == "blanco" or color_seleccionado == "blanco":
    print("Tu colo es neutro")
elif color_seleccionado == "rojo" or color_seleccionado == "naranja":
    print("Tu color es calido")
elif color_seleccionado == "azul" or color_seleccionado == "verde":
    print("Tu color es frio")
else:
    print("Eso no es un color")