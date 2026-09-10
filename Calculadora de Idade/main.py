from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():

    idade = ''

    if request.method == 'POST':
        ano = int(request.form['ano'])
        idade = 2026 - ano
    if ano <= 0:
        idade = 'Idade Invalida'

    return render_template('index.html', idade=idade)

if __name__ == '__main__':
    app.run(debug=True)

