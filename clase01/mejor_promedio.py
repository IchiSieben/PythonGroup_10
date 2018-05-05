cantidad_notas = int(input('Cuántas notas?: '))
notas = []
for numero in range(cantidad_notas):
    nota = int(input('Nota No. {}: '.format(numero + 1)))
    notas.append(nota)

suma = sum(notas)
promedio = suma / cantidad_notas
print('Promedio: {}'.format(promedio))