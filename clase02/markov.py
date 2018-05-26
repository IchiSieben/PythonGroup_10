import random

archivo = open('quijote.txt')
contenido = archivo.read()
archivo.close()

# contenido = ['el', 'ingenioso', 'hidalgo', ...]
contenido = contenido.lower().replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').split(' ')

# palabras = {'el': ['ingenioso', 'rey', ...], ...}
palabras = {}

#                      [(0, 'a'), (1, 'b'), ....]
for posicion, palabra in enumerate(contenido[:-1]):
    # Si la palabra no está el diccionario de palabras
    if palabra not in palabras:
        # Crear la palabra con una lista vacía
        palabras[palabra] = []

    # Agregar a la lista la palabra siguiente
    palabras[palabra].append(contenido[posicion + 1])


palabra_inicial = input('Escribe una palabra: ')

oracion = [palabra_inicial]
for _ in range(15):
    ultima_palabra = oracion[-1]
    siguiente_palabra = random.choice(palabras[ultima_palabra])
    oracion.append(siguiente_palabra)

print(' '.join(oracion))
