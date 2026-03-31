#Votar en las votaciones

edad = 20
if edad >18:
    print("Puedes votar")




#Reglas de ocnducir

edad = 20
licencia_conducir = True

if edad >=18 and licencia_conducir:
    print("Puedes conducir")


#MAQUINA DE FRUTAS

frutas = ["uva","manzana","pera"]
fruta_selecionada = "manzana"

if fruta_selecionada in frutas:
    print("Aqui tines tu fruta seleccioonada")



lista_negra = ["192.168.1.50", "10.0.0.13"]
ip_visitante = "10.0.0.13"

if ip_visitante in lista_negra:
    print("No puedes acceder BLOQUEADO")