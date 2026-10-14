def area_cuadrado(lado):
    return lado**2

def area_tri(base, altura):
    return base*altura

def area_circulo(radio):
    import math
    return math.pi*radio**2

def fibonacci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def palabras(*args):
    cadena = ""
    for i in args:
        cadena = cadena + " " + i
    return cadena

def añadir_eliminar(lista,comando,elemento= None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        lista.remove(elemento)
    return lista

def dic_cont(texto):
    dic = {}

    for elemento in texto.lower():
        dic[elemento] = 0

    for elemento in texto.lower():
        dic[elemento] = dic[elemento] + 1
    return dic

def lara():
    return("Lara")
