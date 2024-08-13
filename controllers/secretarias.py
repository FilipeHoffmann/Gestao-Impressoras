from flask import render_template, request, redirect, url_for
import requests

class Secretarias:
    @staticmethod
    def get_secretarias():
        try:
            response = requests.get('http://localhost:3100/secretarias')
            response.raise_for_status()
            data = response.json()
            return render_template('secretarias.html', secretarias=data)
        except requests.RequestException as e:
            print(f"Erro ao obter secretarias: {e}")
            return "Erro ao obter secretarias", 500

    @staticmethod
    def create_secretaria():
        if request.method == 'POST':
            new_secretaria = {
                'idSecretaria': request.form['idSecretaria'],
                'secretaria': request.form['secretaria']
            }
            try:
                response = requests.post('http://localhost:3100/secretarias', json=new_secretaria)
                response.raise_for_status()
                if response.status_code == 201:
                    return redirect(url_for('secretarias'))
                else:
                    return "Erro ao criar secretaria", response.status_code
            except requests.RequestException as e:
                print(f"Erro ao criar secretaria: {e}")
                return "Erro ao criar secretaria", 500

    @staticmethod
    def update_secretaria():
        if request.method == 'POST':
            id = request.form['idSecretaria']
            updated_secretaria = {
                'secretaria': request.form['secretaria']
            }
            try:
                response = requests.put(f'http://localhost:3100/secretarias/{id}', json=updated_secretaria)
                response.raise_for_status()
                if response.status_code == 200:
                    return redirect(url_for('secretarias'))
                else:
                    return "Erro ao atualizar secretaria", response.status_code
            except requests.RequestException as e:
                print(f"Erro ao atualizar secretaria: {e}")
                return "Erro ao atualizar secretaria", 500

    @staticmethod
    def delete_secretaria(id):
        try:
            response = requests.delete(f'http://localhost:3100/secretarias/{id}')
            response.raise_for_status()
            return redirect(url_for('secretarias'))
        except requests.RequestException as e:
            print(f"Erro ao excluir secretaria: {e}")
            return "Erro ao excluir secretaria", 500
