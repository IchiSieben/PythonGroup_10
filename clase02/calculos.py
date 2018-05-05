# import funciones
# from funciones import *
from matematicas.funciones import promedio as funcion_promedio
from matematicas.constantes import PI

notas = [16, 14, 11, 10]
# promedio = funciones.promedio(*notas)
promedio = funcion_promedio(*notas)

print('Mi promedio es: {}'.format(promedio))

area_circulo = PI * 7623 ** 2

print('El área de un círculo: {}'.format(area_circulo))

