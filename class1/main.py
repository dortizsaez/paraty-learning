from pprint import pprint

from class1.files.reservations import reservations as r

if __name__ == '__main__':
    print("Hola Mundo")

    a = 5
    b = "El valor es: %d - %.2f"
    c = False
    d = [5, "4545656567", False, ["sfgdfghdfghdfhhfdg"]]
    e = {
        "hola": 5,
        "lista": d,
        "dict": {
            "mensaje": "hola"
        }
    }


    total = b % (5.5555555555555, 5.5555555555)
    f = " es "
    total = b.split(f)
    print(total)

    l = ["hola", "mundo"]
    s = ""

    for x in l:
        s += ' ' + x

    print(s)

    s = " ".join(l)

    print(s)

    s = ""
    for x in l:
        s += x + ";"

    print(s)

    s = ";".join(l)

    print(s)

    l2 = [1,2,3,4,5,6,7,8,8,8,8,9,0,3,5,7]

    l3 = list(reversed(l2))

    print(l3)

    diccionario = {
        "clave1": 1,
        "clave2": 2
    }

    for x, y in diccionario.items():
        print("La clave es %s y el valor es %s" % (x, y))

    print(diccionario.get("clave3"))

    if diccionario.get('clave3'):
        print("to guay")

    else:
        print("mu mal")

    print(diccionario['clave3'] if diccionario.get("clave3") else "No encontrado")
    result = diccionario.get("clave3", "No encontrado")
    print(result)
    diccionario['clave3'] = None
    result = diccionario['clave4'] if diccionario.get("clave4") else "No encontrado"
    print(result)

    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 7, 0, 3, 5, 7]
    lista = []

    for x in l2:
        if x == 8:
            lista.append(x)

    print(lista)

    lista_14 = [x for x in l2 if x == 14]
    lista_2 = list(filter(lambda m: m == 2, l2))
    lista_3 = [x for x in l2 if x == 3]

    print(lista_14)
    print(lista_2)
    print(lista_3)

    lista_14 = []
    lista_2 = []
    lista_3 = []

    for x in l2:
        if x == 14:
            lista_14.append(x)

        elif x == 2:
            lista_2.append(x)

        elif x == 3:
            lista_3.append(x)

    print(lista_14)
    print(lista_2)
    print(lista_3)

    diccionario_2 = {
        "hola": 1,
        "mundo": 2,
        "prima": 3
    }

    diccionario_3 = {}

    for x, y in diccionario_2.items():
        if "o" in x and y == 2:
            diccionario_3[y] = x

    print(diccionario_3)

    diccionario_3 = {x: "El valor es %s" % y for x, y in diccionario_2.items() if "o" in x and y == 2}

    print(diccionario_3)

    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 7, 0, 3, 5, 7]

    lista_no_repetidos = []

    for x in l2:
        if not x in lista_no_repetidos:
            lista_no_repetidos.append(x)

    print(lista_no_repetidos)

    l2 = [1, 2, "hola", "adios", 5, 6, 7, 8, 8, 8, 8, 7, 0, 3, 5, 7]
    lista_no_repetidos = list(set(l2))
    print(lista_no_repetidos)
    lista_no_repetidos.remove(8)
    print(lista_no_repetidos)
    lista_no_repetidos.pop()
    print(lista_no_repetidos.pop(7))
    lista_no_repetidos.insert(0, 20)
    print(lista_no_repetidos)
    lista_no_repetidos.clear()
    print(lista_no_repetidos)

    l2 = [1, 2, 5, 6, 7, 8, 8, 8, 8, 7, 0, 3, 5, 7]
    l5 = sorted(l2, reverse=True)
    l5 = sorted(l2, key=lambda f: f == 7 or f == 5, reverse=True)
    print(l5)

    # print(diccionario_2)
    # del diccionario_2["mundo"]
    # print(diccionario_2)
    # t = diccionario_2.pop("prima")
    # print(diccionario_2)
    # print(t)
    # print(diccionario_2.pop("aaaa", 7))
    # print(diccionario_2)

    # print(lista_no_repetidos)
    # lista_no_repetidos.add("hola")
    # lista_no_repetidos.add("hola")
    # lista_no_repetidos.add("hola")
    # lista_no_repetidos.add("hola")
    # lista_no_repetidos.add("hola")
    # lista_no_repetidos.add("hola")
    # lista_no_repetidos.add("hola")
    # print(lista_no_repetidos)
    #
    total_price = 0
    for x in r:
        total_price += float(x.get("price", 0))

    print(total_price)

    price_list = []

    for x in r:
        price_list.append(float(x.get("price")))

    total_price = sum([float(x.get("price"))])
    print(total_price)

    print([x.get("startDate") for x in r])
    r2 = sorted(r, key=lambda p: p.get("startDate"))
    print([x.get("startDate") for x in r2])

    print(sum([5, 7, 6]))

    t = {
        "hola": 6,
        "adios": 111
    }

    sum(**t)
