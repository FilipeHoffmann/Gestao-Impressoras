from flask import Flask, render_template, request, redirect, url_for
from controllers.contratos import Contratos
from controllers.secretarias import Secretarias

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

@app.route('/secretarias', methods=['GET', 'POST'])
def secretarias():
    if request.method == 'GET':
        return Secretarias.get_secretarias()
    elif request.method == 'POST':
        return Secretarias.create_secretaria()

@app.route('/secretarias/update', methods=['POST'])
def update_secretaria():
    return Secretarias.update_secretaria()

@app.route('/secretarias/delete/<int:id>', methods=['POST'])
def delete_secretaria(id):
    return Secretarias.delete_secretaria(id)

if __name__ == '__main__':
    app.run(port=3200, debug=True)