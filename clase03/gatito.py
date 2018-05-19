from PIL import Image

imagen = Image.open('gatito.jpg')
imagen.thumbnail((100, 100))


colores = [
    '@',
    '#',
    'H',
    'J',
    '*',
    '/',
    ',',
    '.',
    ' ',
    ' '
]

imagen_convertida = ''
ancho, alto = imagen.size
#             [(0, 0, 0), (...), ...]
for nro_pixel, pixel in enumerate(imagen.getdata()):
    r, g, b = pixel
    color = (r + g + b) / 3
    factor = color / 255
    posicion = int(factor * (len(colores) - 1))
    imagen_convertida += colores[posicion]

    if nro_pixel % ancho == 0:
        imagen_convertida += '\n'


archivo = open('gatito.txt', 'w')
archivo.write(imagen_convertida)
archivo.close()

