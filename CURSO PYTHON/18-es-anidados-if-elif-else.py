#TIENDA WEB

cliente = "Premium"
Rregalos = True

if cliente == "Premium":
    print("Gracias por ser premium")
    if Rregalos == True:
        print("Tienes un 20% en tu pproxima compra")
    else:
        print("No hay bonificaciones este mes")
elif cliente == "Esential":
    print("Gracias por ser cliente Esential, esperemos que sea premium")
else:
    print("Gacias por tu compra")