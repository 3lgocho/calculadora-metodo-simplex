from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Aquí renderiza tu archivo HTML principal

@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    # Obtener modo de optimización
    modo = request.form.get('selectmodo')
    
    # Obtener la función objetivo
    variables = [key for key in request.form.keys() if key.startswith('variable')]
    funcion_objetivo = [float(request.form[key]) for key in variables]
    
    # Obtener las restricciones
    restricciones = []
    limite_keys = [key for key in request.form.keys() if key.startswith('restriccion') and 'limite' in key]
    for i in range(1, len(limite_keys) + 1):
        restriccion = []
        for key in request.form.keys():
            if f'restriccion{i}_variable' in key:
                restriccion.append(float(request.form[key]))
        restricciones.append(restriccion)
    
    # Obtener los límites y operadores de las restricciones
    limites = []
    operadores = []
    for i in range(1, len(limite_keys) + 1):
        limite_key = f'restriccion{i}_limite'
        if limite_key in request.form:
            limites.append(float(request.form[limite_key]))
        operador_key = f'restriccion{i}_operador'
        if operador_key in request.form:
            operadores.append(request.form[operador_key])
    
    # Imprimir las matrices al final por la consola
    print("Modo de optimización:", modo)
    print("Función objetivo:", funcion_objetivo)
    print("Restricciones:", restricciones)
    print("Límites:", limites)
    print("Operadores:", operadores)

    return "Datos recibidos y procesados"

if __name__ == '__main__':
    app.run(debug=True)
