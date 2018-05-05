palabra = input('Escribe una palabra: ')

if palabra == palabra[::-1]:
    print('es palíndromo')
else:
    print('no es palíndromo')
