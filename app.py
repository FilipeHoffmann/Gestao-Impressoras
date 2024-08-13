from flask import Flask, render_template, request, redirect, url_for
from controllers.contratos import Contratos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contratos', methods=['GET', 'POST'])
def contratos():
    if request.method == 'GET':
        return Contratos.get_contratos()
    elif request.method == 'POST':
        return Contratos.create_contrato()
    
@app.route('/contratos/<int:id>', methods=['POST'])
def update_contrato(id):
    return Contratos.update_contrato(id)

@app.route('/contratos/excluir/<int:id>', methods=['POST', 'DELETE'])
def delete_contrato(id):
    return Contratos.delete_contrato(id)

if __name__ == '__main__':
    app.run(port=3200, debug=True)