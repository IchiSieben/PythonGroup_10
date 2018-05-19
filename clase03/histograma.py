from PIL import Image, ImageDraw

imagen = Image.open('gatito.jpg')

rojos = [0 for _ in range(256)]
verdes = [0 for _ in range(256)]
azules = [0 for _ in range(256)]

for r, g, b in imagen.getdata():
    rojos[r] += 1
    verdes[g] += 1
    azules[b] += 1


def generar_histograma(conteos, nombre_archivo):
    lienzo = Image.new('RGB', (256, 256))
    lapicero = ImageDraw.Draw(lienzo)

    maximo_conteo = max(conteos)
    for color, conteo in enumerate(conteos):
        factor = conteo / maximo_conteo
        lapicero.line([(color, 256), (color, 256 - (factor * 256))])

    lienzo.save(nombre_archivo)


generar_histograma(rojos, 'rojos.jpg')
generar_histograma(verdes, 'verdes.jpg')
generar_histograma(azules, 'azules  .jpg')
