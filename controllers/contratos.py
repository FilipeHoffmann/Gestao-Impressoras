from flask import render_template, request, redirect, url_for, jsonify
import requests

class Contratos:
    @staticmethod
    def get_contratos():
        try:
            response = requests.get('http://localhost:3100/contratos')
            response.raise_for_status()
            data = response.json()
            return render_template('contratos.html', contratos=data)
        except requests.RequestException as e:
            print(f"Erro ao obter contratos: {e}")
            return "Erro ao obter contratos", 500
        
    @staticmethod
    def create_contrato():
        if request.method == 'POST':
            new_contrato = {
                'idContrato': request.form['idContrato'],
                'dataInicial': request.form['dataInicial'],
                'dataFinal': request.form['dataFinal'],
                'dataFinalAtual': request.form['dataFinalAtual']
            }
            try:
                response = requests.post('http://localhost:3100/contratos', json=new_contrato)
                response.raise_for_status()
                if response.status_code == 201:
                    return redirect(url_for('contratos'))
                else:
                    return "Erro ao criar contrato", response.status_code
            except requests.RequestException as e:
                print(f"Erro ao criar contrato: {e}")
                return "Erro ao criar contrato", 500
    

    @staticmethod
    def update_contrato(id):
        try:
            print(request.form)
            updated_contrato = {
                'dataInicial': request.form['dataInicial'],
                'dataFinal': request.form['dataFinal'],
                'dataFinalAtual': request.form['dataFinalAtual']
            }
            response = requests.put(f'http://localhost:3100/contratos/{id}', json=updated_contrato)
            response.raise_for_status()
            if response.status_code == 200:
                return redirect(url_for('contratos'))
            else:
                return "Erro ao atualizar contrato", response.status_code
        except requests.RequestException as e:
            print(f"Erro ao atualizar contrato: {e}")
            return "Erro ao atualizar contrato", 500


    @staticmethod
    def delete_contrato(id):
        try:
            response = requests.delete(f'http://localhost:3100/contratos/{id}')
            response.raise_for_status()
            if response.status_code == 200 or response.status_code == 204:
                return redirect(url_for('contratos'))
            else:
                return "Erro ao excluir contrato", response.status_code
        except requests.RequestException as e:
            print(f"Erro ao excluir contrato: {e}")
            return "Erro ao excluir contrato", 500
