import requests
from bs4 import BeautifulSoup
from pytesseract import image_to_string
from PIL import Image

URL_BASE = 'http://www.sunat.gob.pe/cl-ti-itmrconsruc/'

sesion = requests.Session()

respuesta = sesion.get(URL_BASE + 'frameCriterioBusqueda.jsp')
soup = BeautifulSoup(respuesta.content, 'html.parser')
imagen = soup.find('img').attrs['src']
respuesta = sesion.get(URL_BASE + imagen)

archivo = open('imagen.jpg', 'wb')
archivo.write(respuesta.content)
archivo.close()

captcha = image_to_string(Image.open('imagen.jpg'))

dni = input('Ingrese DNI a consultar: ')

data = {
    'accion': 'consPorTipdoc',
    'razSoc': '',
    'nroRuc': '',
    'nrodoc': dni,
    'contexto': 'ti-it',
    'search1': '',
    'codigo': captcha,
    'tQuery': 'on',
    'tipdoc': '1',
    'search2': dni,
    'coddpto': '',
    'codprov': '',
    'coddist': '',
    'search3': '',
}
respuesta = sesion.post(URL_BASE + 'jcrS00Alias', data=data)

soup = BeautifulSoup(respuesta.content, 'html.parser')
celdas = soup.find_all(attrs={'class': 'bg', 'align': 'left'})
nombre, ciudad, estado = [elemento.text.strip() for elemento in celdas]
# textos = map(lambda elemento: elemento.text.strip(), celdas)

print('Nombre: ' + nombre)
print('Ciudad: ' + ciudad)
print('Estado: ' + estado)
