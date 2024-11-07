from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import os

app = Flask(__name__)

# Definindo as variáveis de ambiente
API_BASE_URL = "http://backend:8000"

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir o formulário de cadastro
@app.route('/cadastro', methods=['GET'])
def inserir_esportivo_form():
    return render_template('cadastro.html')

# Rota para enviar os dados do formulário de cadastro para a API
@app.route('/inserir', methods=['POST'])
def inserir_esportivo():
    modelo = request.form.get['modelo']
    empresa = request.form['empresa']
    quantidade = request.form['quantidade']
    preco = request.form['preco']

    payload = {
        'modelo': modelo,
        'empresa': empresa,
        'quantidade' : quantidade,
        'preco' : preco
    }

    response = requests.post(f'{API_BASE_URL}/api/v1/esportivos/', json=payload)
    
    if response.status_code == 201:
        return redirect(url_for('listar_esportivos'))
    else:
        return "Erro ao inserir esportivo", 500

# Rota para listar todos os esportivos
@app.route('/estoque', methods=['GET'])
def listar_esportivos():
    response = requests.get(f'{API_BASE_URL}/api/v1/esportivos/')
    try:
        esportivos = response.json()
    except:
        esportivos = []
    return render_template('estoque.html', esportivos=esportivos)

# Rota para exibir o formulário de edição de esportivo
@app.route('/atualizar/<int:esportivo_id>', methods=['GET'])
def atualizar_esportivo_form(esportivo_id):
    response = requests.get(f"{API_BASE_URL}/api/v1/esportivos/")
    #filtrando apenas o esportivo correspondente ao ID
    esportivos = [esportivo for esportivo in response.json() if esportivo['id'] == esportivo_id]
    if len(esportivos) == 0:
        return "esportivo não encontrado", 404
    esportivo = esportivos[0]
    return render_template('atualizar.html', esportivo=esportivo)

# Rota para enviar os dados do formulário de edição do esportivo para a API
@app.route('/atualizar/<int:esportivo_id>', methods=['POST'])
def atualizar_esportivo(esportivo_id):
    modelo = request.form['modelo']
    empresa = request.form['empresa']
    quantidade = request.form['quantidade']
    preco = request.form['preco']

    payload = {
        'id': esportivo_id,
        'modelo': modelo,
        'empresa': empresa,
        'quantidade' : quantidade,
        'preco' : preco
    }

    print("Payload: ", payload)
    response = requests.patch(f"{API_BASE_URL}/api/v1/esportivos/{esportivo_id}", json=payload)
    
    if response.status_code == 200:
        return redirect(url_for('listar_esportivos'))
    else:
        return "Erro ao atualizar esportivo", 500

# Rota para exibir o formulário de edição de esportivo
@app.route('/vender/<int:esportivo_id>', methods=['GET'])
def vender_esportivo_form(esportivo_id):
    response = requests.get(f"{API_BASE_URL}/api/v1/esportivos/")
    #filtrando apenas o esportivo correspondente ao ID
    esportivos = [esportivo for esportivo in response.json() if esportivo['id'] == esportivo_id]
    if len(esportivos) == 0:
        return "esportivo não encontrado", 404
    esportivo = esportivos[0]
    return render_template('vender.html', esportivo=esportivo)

# Rota para vender um esportivo
@app.route('/vender/<int:esportivo_id>', methods=['POST'])
def vender_esportivo(esportivo_id):
    quantidade = request.form['quantidade']

    payload = {
        'quantidade': quantidade
    }

    response = requests.put(f"{API_BASE_URL}/api/v1/esportivos/{esportivo_id}/vender/", json=payload)
    
    if response.status_code == 200:
        return redirect(url_for('listar_esportivos'))
    else:
        return "Erro ao vender esportivo", 500

# Rota para listar todas as vendas
@app.route('/vendas', methods=['GET'])
def listar_vendas():
    response = requests.get(f"{API_BASE_URL}/api/v1/vendas/")
    try:
        vendas = response.json()
    except:
        vendas = []
    # salvando nomes dos esportivos vendidos
    total_vendas = 0
    for venda in vendas:
        total_vendas += float(venda['valor_venda'])
    return render_template('vendas.html', vendas=vendas, total_vendas=total_vendas)

# Rota para excluir um esportivo
@app.route('/excluir/<int:esportivo_id>', methods=['POST'])
def excluir_esportivo(esportivo_id):
    response = requests.delete(f"{API_BASE_URL}/api/v1/esportivos/{esportivo_id}")
    
    if response.status_code == 200  :
        return redirect(url_for('listar_esportivos'))
    else:
        return "Erro ao excluir esportivo", 500

#Rota para resetar o database
@app.route('/reset-database', methods=['GET'])
def resetar_database():
    response = requests.delete(f"{API_BASE_URL}/api/v1/esportivos/")
    
    if response.status_code == 200  :
        return render_template('confirmacao.html')
    else:
        return "Erro ao resetar o database", 500


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')