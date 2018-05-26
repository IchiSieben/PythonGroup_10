import requests

print('Películas:')
respuesta_films = requests.get('https://swapi.co/api/films/')
films = respuesta_films.json()['results']

# {'https://swapi.co/api/people/1/': 'Luke Skywalker'}
personajes = {}

for film in films:
    nombre = film['title']
    print('* {}'.format(nombre))

    personajes_pelicula = film['characters']
    for personaje in personajes_pelicula:
        if personaje not in personajes:
            personajes[personaje] = requests.get(personaje).json()['name']

        print('- {}'.format(personajes[personaje]))

    print()
