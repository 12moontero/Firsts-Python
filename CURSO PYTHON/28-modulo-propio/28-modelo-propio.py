import escolar

print(escolar.saludo("David"))
print(escolar.alumnos)

print(escolar.calcular_media([10,10,3]))

validar_estudainte =  escolar.validar_alumnado(5.0)

if validar_estudainte:
    print("El estudiante pasa")
else:
    print("El estudiante repite")

escolar.mostrar_materias()

print(escolar.saludo("Carlos"))