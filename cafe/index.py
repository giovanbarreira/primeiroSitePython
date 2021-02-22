from flask import Flask, render_template, request
import mysql.connector
import time

app = Flask(__name__)

@app.route('/home', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
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


@app.route('/mensagem', methods=['GET','POST'])
def mensagem():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    date = time.strftime('%Y-%m-%d %H:%M:%S')

    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = "",    
        database = 'dbCafe'
    )

    cursor = conn.cursor()
    #sql = """(INSERT INTO mensagens (name,surname,email,phone,message,date) VALUES (%s,%s,%s,%s,%s,%s))"""
    #data = (name, surname, email, phone, message, date)

    sql = """INSERT INTO mensagens (name,surname,email,phone,message,date) VALUES ('""" + name + """','""" + surname + """','""" + email + """','""" + phone + """','""" + message + """','""" + date + """')"""

    try:    
        cursor.execute(sql)
        conn.commit()
        pagina = '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="refresh" content="7; url='/'" />
        </head>
        <body>
            <h1>
            <br>MENSAGEM ENVIADA COM SUCESSO, VOLTANDO PARA A PÁGINA INICIAL EM 7 SEGUNDOS <br><br> 
            <a href="/">CLIQUE AQUI PARA VOLTAR AGORA</a>.</h1>
        </body>
        </html>
        '''
        conn.close()
        return pagina    
    except:
        conn.rollback()

        conn.close()
        return ':-('
    

if __name__ == '__main__':
    app.run(debug=True)