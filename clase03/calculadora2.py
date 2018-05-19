def operar(operacion, a, b):
    return operacion(a, b)


def suma(a, b):
    return a + b


print(operar(suma, 3, 4))
