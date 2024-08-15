from flask import Flask, render_template, request
from controllers.contratos import Contratos
from controllers.secretarias import Secretarias
from controllers.produtos import Produtos
from controllers.aditivos import Aditivos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Contratos

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

#Secretarias

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

#Produtos

@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'GET':
        return Produtos.get_produtos()
    elif request.method == 'POST':
        return Produtos.create_produto()

@app.route('/produtos/<int:id>', methods=['POST'])
def update_produto(id):
    return Produtos.update_produto(id)

@app.route('/produtos/delete/<int:id>', methods=['POST'])
def delete_produto(id):
    return Produtos.delete_produto(id)

#Aditivos

@app.route('/aditivos', methods=['GET','POST'])
def aditivos():
    if request.method == 'GET':
        return Aditivos.get_aditivos()
    else:
        return Aditivos.create_aditivo()

@app.route('/aditivos/update/<int:id>', methods=['POST', 'PUT'])
def update_aditivo(id):
    return Aditivos.update_aditivo(id)

@app.route('/aditivos/delete/<int:id>', methods=['POST', 'DELETE'])
def delete_aditivo(id):
    return Aditivos.delete_aditivo(id)

if __name__ == '__main__':
    app.run(port=3200, debug=True)