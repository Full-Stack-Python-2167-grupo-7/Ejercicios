# Ejercicio 1
def reemplazarespacios(cadena):
    return cadena.replace(" ", "_")
#Ejercicio 2
def intercambiarMayusculasyMinusculas(cadena):
    if len(cadena) > 100:
        return "La cadena es demasiado larga"
    return cadena.swapcase()
# Extra a
def imprimeTriangulo(valor):
    
    for i in range(1,valor+1):
        caracter = str(i)
        print(caracter *i)
# Extra b
def caracteresMasRepetidos(cadena):
    diccionario = {}
    for i in cadena:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    diccionarioOrdenado = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
    return diccionarioOrdenado[:3]