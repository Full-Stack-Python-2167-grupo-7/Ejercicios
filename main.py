import json
from src.utils import *
# 1 - Dado un string, escribir una funcion que cambie todos 
# los espacios por guiones.
micadena=str(input("Ingrese una cadena: "))
print(reemplazarespacios(micadena))
#2-  Cambiar Mayusculas por Minusculas. (Ejemplo: 
# "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.
micadena=str(input("Ingrese una cadena: "))
print(intercambiarMayusculasyMinusculas(micadena))
