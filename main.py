from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/botao', methods=['POST'])
def botao():
    return "Você clicou no botao!"

if __name__ == '__main__':
    app.run(debug=True) 
