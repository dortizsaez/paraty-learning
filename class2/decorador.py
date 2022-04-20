def funcion_a(funcion_b):
    def wrapper(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')

        return result

    return wrapper