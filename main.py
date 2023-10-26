from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/telaInicial', methods=['POST'])
def telaInicial():
    return "Você está na tela inicial!"  

# Colocar o site no ar 
if __name__ == '__main__':
    app.run(debug=True) 
