nombre = "David"
edad = 14
mensaje = "Hola tu nombre es: "

print(mensaje + nombre + " y tu edad es " + str(edad))

print(mensaje, nombre,"y tu edad es", edad)

print(f"Hola tu nombre es : {nombre} y tu edad es: {edad}")  #LA MEJOR DE TODAS 

print("Hola mi nombre es {} y tu edad es: {}" .format(nombre,edad))   #DIFICIL

print("Hola tu nombre es %s y tu edad es : %d" % (nombre, edad))     #MUY ANTIGUA NO SE USA, SUPER DIFICIL