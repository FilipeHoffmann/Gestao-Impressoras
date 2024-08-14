from flask import render_template, request, redirect, url_for
import requests

class Produtos:
    @staticmethod
    def get_produtos():
        try:
            response = requests.get('http://localhost:3100/produtos')
            response.raise_for_status()
            data = response.json()
            return render_template('produtos.html', produtos=data)
        except requests.RequestException as e:
            print(f"Erro ao obter produtos: {e}")
            return "Erro ao obter produtos", 500

    @staticmethod
    def create_produto():
        if request.method == 'POST':
            new_produto = {
                'idProduto': request.form['idProduto'],
                'descricao': request.form['descricao'],
                'franquiaPB': request.form['franquiaPB'],
                'franquiaColor': request.form['franquiaColor'],
                'tipo': request.form['tipo'],
                'copiaLocacao': request.form['copiaLocacao'],
                'color': request.form['color']
            }
            try:
                response = requests.post('http://localhost:3100/produtos', json=new_produto)
                response.raise_for_status()
                if response.status_code == 201:
                    return redirect(url_for('produtos'))
                else:
                    return "Erro ao criar produto", response.status_code
            except requests.RequestException as e:
                print(f"Erro ao criar produto: {e}")
                return "Erro ao criar produto", 500

    @staticmethod
    def update_produto(id):
        if request.method == 'POST':
            updated_produto = {
                'descricao': request.form['descricao'],
                'franquiaPB': request.form['franquiaPB'],
                'franquiaColor': request.form['franquiaColor'],
                'tipo': request.form['tipo'],
                'copiaLocacao': request.form['copiaLocacao'],
                'color': request.form['color']
            }
            try:
                response = requests.put(f'http://localhost:3100/produtos/{id}', json=updated_produto)
                response.raise_for_status()
                if response.status_code == 200:
                    return redirect(url_for('produtos'))
                else:
                    return "Erro ao atualizar produto", response.status_code
            except requests.RequestException as e:
                print(f"Erro ao atualizar produto: {e}")
                return "Erro ao atualizar produto", 500

    @staticmethod
    def delete_produto(id):
        try:
            response = requests.delete(f'http://localhost:3100/produtos/{id}')
            response.raise_for_status()
            return redirect(url_for('produtos'))
        except requests.RequestException as e:
            print(f"Erro ao excluir produto: {e}")
            return "Erro ao excluir produto", 500
