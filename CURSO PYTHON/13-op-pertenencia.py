#Operadores de PERTENENCCIA
#Siempre van a dar bolenaos True o False 


#LISTAS
frutas = ["pera","Uva","Manzana"]
print("pera" in frutas)    #True
print("Uva" in frutas)     #True
print("Kiwi" in frutas)    #False                         


#CADENAS
texto = "Hola mundo"
print("H" in texto)       #True
print("z" in texto)       #False


#TUPLA
numeros = (1,2,3)
print(2 in numeros)     #True
print(4 in numeros)     #False


#SETS
flores = {"clavel","margrita", "Diente de Leon"}
print("clavel" in flores)  #True
print("amapola" in flores) #False


#DICCIONARIOS
DNI = {"nombre":"David","Edad":14}  
print("David" in DNI)      #False           Porque no es una clave es un valor
print("nombre" in DNI)     #True            Poruqe si es una clave



#EL USO DE NOT IN ES EL CONTRARIO Y YA

texto2 = "Hola mundo"
print("Hola mundo" in texto2)        #True
print("Hola mundo" not in texto2)    #False         #Porque estas poniendo el contrario not in