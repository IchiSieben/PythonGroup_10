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


print(palabras)
