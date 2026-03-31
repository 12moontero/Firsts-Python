#WHILE ES LA ESTRUCTURA DE REPETICION 

#CONTADOR BASICO
contador = 0
while contador <3:
    contador += 1
    print(f"El valor del contador es {contador}")


#DIA DE LAS SEMANA
semana = ["lunes","martes","miercoles","jeuves","viernes","sabado","domingo"]
dia = 0
while dia < len(semana):
    print(f"Es dia {semana[dia]} ")
    dia += 1

#CONTADOR
contador = 0

while contador < 20:
    contador += 1
    
    if contador == 11:
        continue
    
    print(contador)


