NOMBRE_ESCUELA = "Escuela general de la Comunidad de Madrid"
CICL0_ESCOLAR = 2026

alumnos = ["Carlos","David","Juan","Pepe"]
materias = ["Mates","Fisica","Ingles"]

def calcular_media(notas):
    return sum(notas) / len(notas)

def validar_alumnado(promedio):
    return promedio >= 5

def mostrar_materias():
    for materia in materias:
        print(" - ", materia)

def saludo(nombre):
    return f"Hola {nombre}, te damos la bienvenida a la {NOMBRE_ESCUELA}"