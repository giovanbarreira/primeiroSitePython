from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    return render_template("paginas/index.html")

@app.route('/plantio')
def plantio():
    return render_template("paginas/plantio.html")

@app.route('/bebida')
def bebida():
    return render_template("paginas/bebida.html")

@app.route('/graos')
def graos():
    return render_template("paginas/graos.html")    

@app.route('/contato')
def contato():
    return render_template("paginas/contato.html")

if __name__ == '__main__':
    app.run(debug=True)