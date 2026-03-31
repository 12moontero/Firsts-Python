#ESTRUCTURA MATCH Y CLASE
#SE USA CUANDO TIENES MUCHAS CONDICIONES Y NO USAR ELIF O IF TODo EL RATO

promedio = 6
match promedio:
    case 10:
        print("Nota perfecta")
    case 9:
        print("Nota muy beuna")
    case 8:
        print("Nota buena")
    case 7:
        print("Nota buena pero mejorable")
    case 6:
        print("Nota bien pero muy mejorable")
    case 5:
        print("Nota neutra y demasiado mejorable")
    case _:
        print("Nota suspensa, hay que esforzarse mucho")


#DATOS
dato_a_validar =  ("Hola mundo")

match dato_a_validar:
    case list():
        print("Es un dato de tipo: lista")
    case str():
        print("Es un dato de tipo: string")
    case int():
        print("Es un dato de tipo: entero")
    case dict():
        print("Es un dato de tipo: diccionario")
    case _:
        print("Dato desconocido")


#EDADES
edad = 55
match edad:
    case edad if edad >= 0 and edad <= 13:
        print("Eres un niño")
    case edad if edad >13 and edad <18:
        print("Eres un adolescente")
    case edad if edad >= 18 and edad <=60:
        print("Eres adulto")
    case edad if edad >60 and edad <=100:
        print("Eres un viejo")
    case edad if edad >100 and edad <=110:
        print("Estas en las últimas")
    case _:
        print("Estas muerto")