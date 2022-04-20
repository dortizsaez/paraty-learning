import time
from datetime import datetime

from class2.Coche import Coche, Moto, Vehiculo


def timeIt(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        print("Empieza la funcion")
        result = func(*args, **kwargs)
        print("termina la funcion")
        end_time = time.time()
        print("Ha tardado: %s" % (end_time - start_time))

        return result

    return wrap


@timeIt
def funcion2():
    return "6"


@timeIt
def print_algo(objeto, extra1=None, extra2=None, **kwargs):

    if type(objeto) == dict:
        print_dict(objeto)

    elif type(objeto) in [list, tuple, set]:
        print_lista(objeto)

    elif objeto is None:
        print("No es nada")

    elif objeto == Vehiculo:
        print("Primo que esto es una moto: %s" % objeto)

    else:
        print("Algo es, no se")
        print("El elemento es: %s" % objeto)

    print("eso es todo")

    if extra1:
        print("Que se ha acabado ya pesao")

    if extra2:
        print("Consejito del dia: ¿Sabiais que los elefantes tienen 4 rodillas?")

    if kwargs.get("hola"):
        print(kwargs['hola'])

    print(kwargs.get("despedida"))


def print_dict(d: dict):
    print("Es un diccionario")
    for x, y in d.items():
        print("El elemento es: %s - %s" % (x, y))

    d['extra'] = 8

    return "hola"


def print_lista(lista: list):
    if not type(lista) in [list, tuple]:
        print("Te has colado bro")
        return

    print("Es una %s" % ("lista" if type(lista) == list else "tupla"))
    for x in lista:
        print("El elemento es: %s" % x)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [6, 6, 7, 8]
    l3 = [5557, 25, 3, 5]
    d1 = {"hola": "mundo", "paco": "pepe"}
    t1 = (1, 2, 3, 4)
    n1 = 5.5555

    #print_algo(l1)
    #print_algo(l2)
    #print_algo(l3)
    #print_algo(d1)
    #print_algo(t1)
    #print_algo(n1)
    #print_algo(d1)
    #print_algo(n1, extra2=False, extra1=True)
    #print_algo(n1, despedida="adioooooo", extra2=False, extra1=True)
    #print(funcion2())
    # print(d1)
    # print_dict(d1)
    # print(d1)

    coche = Coche("Seat panda", 5, "Gasolina")
    coche2 = Coche("Ford fiesta", 5, "Gasolina")
    print(coche)
    print(coche2)
    print(coche2.esta_arrancado())
    print(coche2.dime_motor())
    coche2.arranca_vehiculo()
    print(coche2.esta_arrancado())
    coche2.apaga_vehiculo()
    print(coche2.esta_arrancado())

    moto1 = Moto("Kawasaki Ninja", 2, "Diesel")
    moto2 = Moto("Kawasaki Ninja", 2, "Electrico")
    moto3 = Moto("Kawasaki Ninja", 2, "Gasolina")
    print(moto1)
    moto1.arranca_vehiculo()
    print(moto1.esta_arrancado())
    print(moto1.dime_motor())

    lista_motos = [moto1, moto2, moto3]

    print(lista_motos)
    for x in lista_motos:
        print(x)

    print_algo(moto1)

    for index, x in enumerate(lista_motos):
        print(index)
        print(x)
        lista_motos[index].arranca_vehiculo()
        if index + 1 == len(lista_motos):
            print("No hay mas motos")

    for x in lista_motos:
        print(x.esta_arrancado())





