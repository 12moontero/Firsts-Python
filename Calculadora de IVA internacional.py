#CALCULADORA INTERNACIONAL


producto = float((input("¿Precio producto: ")))
IVA = int(input("¿IVA (Ej: 21): "))

IVA_Fin = 1 + (IVA/100)
producto *= IVA_Fin

print(f"Tu producto con IVA es {producto}" )