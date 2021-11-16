# Ejercicio 1
def reemplazarespacios(cadena):
    return cadena.replace(" ", "_")
#Ejercicio 2
def intercambiarMayusculasyMinusculas(cadena):
    return cadena.swapcase()
# Extra a
def imprimeTriangulo(valor):
    
    for i in range(1,valor+1):
        caracter = str(i)
        print(caracter *i)