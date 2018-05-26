def calcular(operacion, a, b):
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    operaciones = {
        'suma': suma,
        'resta': resta
    }

    return operaciones[operacion](a, b)


print(calcular('suma', 3, 4))
print(calcular('resta', 3, 4))
# calcular('producto', 3, 4)
# calcular('cociente', 3, 4)
