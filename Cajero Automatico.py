saldo = 5000
opcion = 0

while opcion != 4:
    menu_visual = """
==============================
      CAJERO AUTOMÁTICO
==============================
1. Ver saldo
2. Ingresar dinero
3. Sacar dinero
4. Salir
==============================
Elija una opción: """

    opcion = int(input(menu_visual))
    match opcion:
        case 1:
            print(f"Este es tu saldo actual {saldo}")
        case 2:
            ingreso = float(input("Ingrese la cantidad de dinero: "))
            saldo += ingreso
            print(f"Su saldo actual es de {saldo}")
        case 3:
            retiro = float(input("¿Cuanto dinero desea retirar: "))
            if saldo < retiro:
                print("No tiene ese dinero")
            else:
                print(f"Su saldo actual es de {saldo}")
                saldo -= retiro 
        case 4:
            print("Gracias por tu tiempo")
        case _:
            print("Eso no es un numero")