from flask import Flask, render_template

# Configurando o Flask para servir arquivos estáticos e templates das pastas corretas
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/conteudos')
def conteudos():
    return render_template('conteudos.html')

@app.route('/novidades')
def novidades():
    return render_template('novidades.html')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/planos')
def planos():
    return render_template('planos.html')


if __name__ == '__main__':
    app.run(debug=True)
