from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_temperatura', methods=['POST'])
def converter_temperatura():

    resultado = ''

    if request.method == 'POST':
        temperatura = float(request.form['temperatura'])

        resultado = (temperatura * 9/5) + 32

    if temperatura <= 0:
        temperatura = 'Digite uma temperatura válida'

    return render_template('converter_temperatura', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
