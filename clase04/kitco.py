import requests
from bs4 import BeautifulSoup

respuesta = requests.get('http://www.kitco.com/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'})

soup = BeautifulSoup(respuesta.content, 'html.parser')
precio_venta = soup.find(attrs={'id': 'AU-bid'}).text
precio_compra = soup.find(attrs={'id': 'AU-ask'}).text

print('PRECIO DEL ORO:')
print('Compra: {} | Venta: {}'.format(precio_compra, precio_venta))
