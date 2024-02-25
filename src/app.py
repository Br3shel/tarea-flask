from flask import Flask, render_template

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
@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)