import operator

#1. Dado un string, escribir una funcion que cambie todos los espacios por guiones.
def replace_spaces(p_str):
    '''Dado un string, escribir una funcion que cambie todos los espacios por guiones.'''
    return p_str.replace(" ", "_")

# 2-  Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.
def cambia_mayus(p_str):
    '''Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.'''
    if len(p_str) > 100:
        return "El Parametro Excede los 100 caracteres"
    else:
        return p_str.swapcase()

#3- Los strings son inmutables, escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y que devuelve el string modificado.
def subst_str(p_str, p_index, p_new_char):
    '''Los strings son inmutables, escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y que devuelve el string modificado.'''
    return p_str[0:p_index-1] + p_new_char + p_str[p_index:]

#4- Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre y apellido pero con capitalizacion(primera letra mayuscula).
def cap_nom_ape(p_str):
    return p_str.title()

#5- 5- Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, y esta devuelve la puntuacion del subcampeon. 
# (ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)
def puntos_subcampeon(* args):
    if not isinstance(args[0], list) :
        l_ret = list(set(args))
    else:
        l_ret = list(set(args[0]))        
    l_ret.sort()
    return l_ret[-2]

#Extra  a- Escribir una funcion que recibe un numero entero y imprima por salida estandar(usando print) un triangulo de numeros de altura igual al numero ingresado.
def triangulo(altura):
    for i in range(1,altura + 1):
        print(str(i)* i)

#Extra b - Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) y devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente. 
def mas_usados(p_str):
    cadena = p_str.lower().replace(" ", "")
    letras = set(cadena)
    dic = {}
    for l in letras:
        dic[l] = cadena.count(l)
    sorted_d =  sorted(dic.items(), key=operator.itemgetter(1),reverse=True)

    for a,b in sorted_d[:3]:
        print(str(a) + " " + str(b))
    

#print(triangulo(5))
#mas_usados("Codo a Codo")

#print(subst_str("Cadena a Remplazar", 8, 'x'))

#print(cap_nom_ape("alejandro meDici"))

#print(puntos_subcampeon(2,6,10,10,7,5,6))

#print(puntos_subcampeon([2,6,10,10,7,5,6]))