from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_moeda', methods=['POST'])
def converter_moeda():

    resultado = ''

    if request.method == 'POST':
        valor = float(request.form['valor'])
        resultado = valor * 5

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)