#HAY MUHISIMOS PARAMETROS EN FUNCIONES def

def saludar(nombre):
    print(f"Hola {nombre}, este nombre es bonito")      #def, funcion sirve para eso para recordar luego la estructura de def
saludar("Carlos")
saludar("Manuel")


#Este es otro ejemplo parecido

def saludar(nombre="Falta nombre", edad= 0):
    print(f"Hola {nombre} y tienes {edad} años ")
saludar(nombre= "David", edad=14)

#LISTAS DE FRUTAS

def lista_fruta(*frutas):
    print(frutas)
lista_fruta("Uva","piña","fresa")

#Otro ejemplo usando nombres usando el for para aparecer uno en uno

def lista_nombres(*nombres):
    for nombre in nombres:
        print(nombre)
lista_nombres("Carlos","Paloma","Manuel")


#return

def operacioes(num_uno, num_dos):
    return num_uno + num_dos, num_uno - num_dos, num_uno * num_dos, num_uno / num_dos

sumar,restar , mul, div = operacioes(15,20  )

print(sumar)
print(restar)
print(mul)
print(div)

 