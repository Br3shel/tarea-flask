from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__)

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

@app.route('/')
def inscrito():
    return redirect(url_for('login'))

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        correo=(request.form['username'])
        Password=(request.form['password'])
        return render_template('inscrito.html', correo=correo , Password=Password)
    else:    
        return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)