from flask import render_template, request, redirect, url_for, jsonify
import requests

class Aditivos:
    @staticmethod
    def get_aditivos():
        try:
            # Fazendo requisições para a API para obter aditivos e contratos
            aditivos_response = requests.get('http://localhost:3100/aditivos')
            contratos_response = requests.get('http://localhost:3100/contratos')
            
            aditivos_response.raise_for_status()
            contratos_response.raise_for_status()

            # Convertendo as respostas em JSON
            aditivos = aditivos_response.json()
            contratos = contratos_response.json()

            # Renderizando a página com a lista de aditivos e contratos
            return render_template('aditivos.html', aditivos=aditivos, contratos=contratos)
        except requests.RequestException as e:
            print(f"Erro ao obter aditivos ou contratos: {e}")
            return "Erro ao obter aditivos ou contratos", 500

    @staticmethod
    def create_aditivo():
        if request.method == 'POST':
            new_aditivo = {
                'idAditivo': request.form['idAditivo'],
                'descricao': request.form['descricao'],
                'dataInicial': request.form['dataInicial'],
                'dataFinal': request.form['dataFinal'],
                'situacao': request.form['situacao'],
                'idContrato': request.form['idContrato']  # ID do contrato selecionado
            }
            try:
                response = requests.post('http://localhost:3100/aditivos', json=new_aditivo)
                response.raise_for_status()
                if response.status_code == 201:
                    return redirect(url_for('aditivos'))
                else:
                    return "Erro ao criar aditivo", response.status_code
            except requests.RequestException as e:
                print(f"Erro ao criar aditivo: {e}")
                return "Erro ao criar aditivo", 500

    @staticmethod
    def update_aditivo(id):
        try:
            updated_aditivo = {
                'descricao': request.form['descricao'],
                'dataInicial': request.form['dataInicial'],
                'dataFinal': request.form['dataFinal'],
                'situacao': request.form['situacao'],
                'idContrato': request.form['idContrato']  # ID do contrato atualizado
            }
            response = requests.put(f'http://localhost:3100/aditivos/{id}', json=updated_aditivo)
            response.raise_for_status()
            if response.status_code == 200:
                return redirect(url_for('aditivos'))
            else:
                return "Erro ao atualizar aditivo", response.status_code
        except requests.RequestException as e:
            print(f"Erro ao atualizar aditivo: {e}")
            return "Erro ao atualizar aditivo", 500

    @staticmethod
    def delete_aditivo(id):
        try:
            response = requests.delete(f'http://localhost:3100/aditivos/{id}')
            response.raise_for_status()
            if response.status_code == 200 or response.status_code == 204:
                return redirect(url_for('aditivos'))
            else:
                return "Erro ao excluir aditivo", response.status_code
        except requests.RequestException as e:
            print(f"Erro ao excluir aditivo: {e}")
            return "Erro ao excluir aditivo", 500
