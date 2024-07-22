from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    variables = request.form['variables']
    restricciones = request.form['restricciones']
    
    with open('datos.txt', 'w') as f:
        f.write(f'variable1: {variables}\n')
        f.write(f'variable2: {restricciones}\n')
    
    return 'Datos guardados con éxito'

if __name__ == '__main__':
    app.run(debug=True)
