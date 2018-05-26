import argparse

from PIL import Image


def convertir(nombre_imagen, texto, ancho):
    imagen = Image.open(nombre_imagen)
    ancho = ancho or 100
    imagen.thumbnail((ancho, ancho))

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

    archivo_salida = nombre_imagen.split('.')[0] + '.txt' if not texto else texto
    archivo = open(archivo_salida, 'w')
    archivo.write(imagen_convertida)
    archivo.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('archivo', nargs=1, type=str, help='Archivo de imagen de entrada')
    parser.add_argument('--output', '-o', nargs=1, type=str, required=False, help='Archivo de texto de salida')
    parser.add_argument('--size', '-s', nargs=1, type=int, required=False, help='Tamaño máximo del texto')

    argumentos = parser.parse_args()
    convertir(
        argumentos.archivo[0],
        argumentos.output[0] if argumentos.output else None,
        argumentos.size[0] if argumentos.size else None
    )
