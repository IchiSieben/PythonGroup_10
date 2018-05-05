archivo = open('quijote.txt')
texto = archivo.read()
archivo.close()

# letras = {'a': 100, 'b': 200, ...}
letras = {}

for letra in texto.lower():
    if letra in letras:
        # Agrega 1 al valor existente
        # letras['a'] = 2
        letras[letra] += 1
    else:
        # Crea un par en el diccionario
        # letras['a'] = 1
        letras[letra] = 1

print(letras)

