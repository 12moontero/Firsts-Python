intentos = 3
clave_real = "admin123"

while intentos > 0:
    intentos -= 1
    acceso = input("Introduce la clave: ")
    
    print(f"Te quedan, {intentos} intentos")

if acceso == clave_real:
        print("Acceso concedido")
else:
    print("Sistema bloqueado")