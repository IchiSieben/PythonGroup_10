from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hola mundo!'


@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    contexto = {
        'edad': 17,
        'hobbies': ['correr', 'nadar', 'paracaidismo']
    }

    if request.method == 'POST':
        contexto['nombre'] = request.form['nombre']

    return render_template('saludo.html', **contexto)


@app.route('/saludo/<nombre>/<apellido>')
def saludo_apellido(**kwargs):
    return '{} {}, te saludo'.format(kwargs['nombre'], kwargs['apellido'])


# /calcular/suma/3/4
# /calcular/resta/3/4
# /calcular/producto/3/4
# /calcular/cociente/3/4
@app.route('/calcular/<operacion>/<int:a>/<int:b>')
def calcular(operacion, a, b):
    if operacion == 'suma':
        return str(a + b)
    elif operacion == 'resta':
        return str(a - b)
    elif operacion == 'producto':
        return str(a * b)
    elif operacion == 'cociente':
        return str(a / b)


@app.route('/portada')
def portada():
    return render_template('index.html')


lista_tareas = []


@app.route('/tareas', methods=['GET', 'POST'])
def tareas():
    if request.method == 'POST':
        lista_tareas.append(request.form['tarea'])
    return render_template('tareas.html', tareas=lista_tareas)


app.run(debug=True)
