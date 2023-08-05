from app import app, db
from flask import request, jsonify
from app.models import Product

# Listagem

@app.route('/produtos', methods=['GET'])
def obter_produtos():
    produtos = Product.query.all()
    lista_de_produtos = []

    for produto in produtos:
        produto_dict = {
            "id": produto.id,
            "nome": produto.nome,
            "descricao": produto.descricao,
            # Outros campos...
        }
        lista_de_produtos.append(produto_dict)

    return jsonify(lista_de_produtos)

# Criação

@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.json  # Assume que os dados são enviados em JSON
    novo_produto = Product(**dados)

    db.session.add(novo_produto)
    db.session.commit()

    return jsonify({
        "id": novo_produto.id,
        "nome": novo_produto.nome,
        "descricao": novo_produto.descricao,
        # Outros campos...
    }), 201

# Visualização por ID

@app.route('/produtos/<int:id_produto>', methods=['GET'])
def obter_produto(id_produto):
    produto = Product.query.get(id_produto)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    produto_dict = {
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        # Outros campos...
    }
    return jsonify(produto_dict)

# Atualização por ID

@app.route('/produtos/<int:id_produto>', methods=['PUT'])
def atualizar_produto(id_produto):
    produto = Product.query.get(id_produto)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    dados = request.json
    for chave, valor in dados.items():
        setattr(produto, chave, valor)

    db.session.commit()

    return jsonify({
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        # Outros campos...
    })

# Exclusão por ID

@app.route('/produtos/<int:id_produto>', methods=['DELETE'])
def excluir_produto(id_produto):
    produto = Product.query.get(id_produto)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    db.session.delete(produto)
    db.session.commit()

    return jsonify({"mensagem": "Produto excluído"})
