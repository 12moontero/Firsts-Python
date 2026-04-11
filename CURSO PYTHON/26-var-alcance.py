#Variables locales en funciones o variables en todo el codigo

x="Hola global"
def saludar():
    x="Hola local"
    print(x)

print(x)
saludar()