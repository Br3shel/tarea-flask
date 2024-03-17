from flask import Flask, render_template,request,redirect,url_for,flash,session
from flask_mysqldb import MySQL
import config

app=Flask(__name__)

app.config["MYSQL_USER"]= config.MYSQL_USER
app.config["MYSQL_DB"]= config.MYSQL_DB
app.config["MYSQL_PASSWORD"]= config.MYSQL_PASSWORD
app.config['SECRET_KEY'] = config.HEX_SEC_KEY
db = MySQL(app)

@app.route('/')
def index():
    data={
        'titulo':'Index',
        'mensaje':'Bienvenido al sitio Web',
        'nombre':'Claudino brishel Lopez Acosta'
    }
    return render_template('index.html', data=data)

@app.route('/pagina2/')
def pagina2():
    data={
        'titulo':'Index',
        'mensaje':'Bienvenido al sitio Web',
        'nombre':'Claudino brishel Lopez Acosta',
    }
    return render_template('pagina2.html', data=data)

@app.route('/imagen/')
def imagen():
    return render_template('imagen.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, password))
            user = cur.fetchone()
            cur.close()
            if user is not None:
                session['email'] = email
                session['name'] = user[1]
                session['surnames'] = user[2]
                return redirect(url_for('inscrito'))
            
        return render_template('login.html', message="Email o contraseña incorrectos")
    
    return render_template('login.html')
   
@app.route('/inscrito')
def inscrito():
    return render_template('inscrito.html')   


@app.route('/logout', methods=['POST'])
def logout():
    session.clear() 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)