Sistema_Puntos = {}
Sistema_Targetas = {}

#Sistema de Agregar 

def agregar_puntos(db,nombre,puntos):
    db[nombre] = puntos

def ranking_puntos(db):
    print("===== Sistema de Puntos =====")
    for nombre,puntos in db.items():
        print(f"Jugador: {nombre} = {puntos} puntos")

agregar_puntos(Sistema_Puntos,"David",15)
agregar_puntos(Sistema_Puntos,"Sean",20)
agregar_puntos(Sistema_Puntos,"Juan",5)


ranking_puntos(Sistema_Puntos)


def agregar_Targetas(db,nombre,targetas):
    db[nombre] = targetas

def ranking_targetas(db):
    print("===== Sistema de Targetas =====")
    for nombre, targetas in db.items():
        print(f"Jugador: {nombre} = {targetas} Trgetas A + R,")

agregar_Targetas(Sistema_Targetas,"Leon",2)
agregar_Targetas(Sistema_Targetas,"Lucas",5)
agregar_Targetas(Sistema_Targetas,"Mario",1)

ranking_targetas(Sistema_Targetas)


#Sistema de Quitar

def quitar_puntos(db,nombre,puntos):
    db[nombre] -= puntos

def quitar_targetas(db,nombre,targetas):
    db[nombre] -= targetas
 #CONCLUSIONES SI QEURIES QUITAR TIENES QUE USAR -= SI QUEIRES SUSTITUIR =
  
"""
 Lo que hecho y he aprendido es a poner todo bien organizado con funciones(def)
 y tener un codigo flexible que con cualquier base de datos (diccionario) podrias usar esas
 funciones. Basicamente un modulo o liberia externo del main.
 """