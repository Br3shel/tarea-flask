from flask import Flask, render_template

app=Flask(__name__)

@app.route('/pagina2')
def pagina2():
    data2={
        'titulo':'pagina 2',
        'mensaje':'Bienvenido al sitio Web, se encuentra en la segunda página',
        'nombre':'Claudino brishel Lopez Acosta'
    }
    return render_template('index.html', data=data2)
@app.route('/')
def index():
    data={
        'titulo':'Index',
        'mensaje':'Bienvenido al sitio Web',
        'nombre':'Claudino brishel Lopez Acosta'
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)