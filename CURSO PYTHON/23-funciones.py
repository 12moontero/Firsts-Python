#Def normal una funcion normal

def saludo(nombre, edad, pais):
    print(f"Hola {nombre} tienes {edad} años y eres de {pais}")

saludo("Carlos", 20, "Argentina")
saludo("Manuel", 15, "Francia")
saludo("Isable", 80, "España")



#SUMAR Y RESTAR VALORES CON RETURN

def sumar(numero_uno, numero_dos):
    return numero_uno + numero_dos

def restar(numero_uno,numero_dos):
    return numero_uno - numero_dos

resultado_uno = sumar(10,20)
resultado_dos = restar(20,10)

operacion = resultado_uno + resultado_dos
print(f"El numero uno {resultado_uno} y el dos {resultado_dos} y la suma de los dos es {operacion}")


#COLORES

colores = ["rojo", "verde", "azul", "morado"]

def validar_color(color):
    if color in colores:
        return "True"
    else:
        return "False"

if validar_color("rojo"):
    print("Ese color esta en la lista")
else:
    print("Ese color no esta en la lista")
                                      