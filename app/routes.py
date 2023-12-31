from app import app, db
from flask import request, jsonify, Response
from app.models import Product
import functools

# Função para autenticar a requisição com a senha
def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != 'cozi.ai' or auth.password != 'Cozi.ai.Andrey':
            return Response('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return func(*args, **kwargs)
    return wrapper

# Autenticação em todas as rotas
@app.before_request
@require_auth
def before_request():
    pass  # Nada precisa ser feito aqui, a função require_auth já faz a autenticação

# Listagem
@app.route('/v1/products', methods=['GET'])
def get_products():
    """Lista os produtos"""
    try:
        products = Product.query.all() # Adicionar filtros posteriormente
        if len(products) <= 0:
            raise ValueError("Não foram encontrados produtos com os filtros informados")
        
        products_list = []
        for product in products:
            product_dict = {
                "id": product.id,
                "name": product.name,
                "description": product.description
                # Outros campos...
            }
            products_list.append(product_dict)
        
        return jsonify(products_list)

    except ValueError as e:
        return str(e)
    
    except Exception as e:
        return f"O sistema se comportou de maneira inesperada, erro: {str(e)}"

        

# Criação
@app.route('/v1/products', methods=['POST'])
def create_product():
    """"Cria um produto"""
    try:
        data = request.json  # Assume que os dados são enviados em JSON

        if not data or "name" not in data or "description" not in data:
            raise Exception("Invalid data")
    
        new_product = Product(**data)

        db.session.add(new_product)
        db.session.commit()

        return jsonify({
            "id": new_product.id,
            "name": new_product.name,
            "description": new_product.description,
            # Outros campos...
        }), 201

    except Exception as e:
        return(f"Erro {str(e)}")

# Visualização por ID
@app.route('/v1/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Visualiza o produto"""
    try:
        product = Product.query.get(product_id)

        if not product:
            raise Exception("error, product not found")

        product_dict = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            # Outros campos...
        }
        return jsonify(product_dict)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Atualização por ID
@app.route('/v1/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Atualiza um produto"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        data = request.json
        for key, value in data.items():
            setattr(product, key, value)

        db.session.commit()

        return jsonify({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            # Outros campos...
        })

    except Exception as e:
        return f"Error found: {str(e)}"

# Exclusão por ID
@app.route('/v1/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Deleta um produto"""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    try:
        db.session.delete(product)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Product deleted"})
