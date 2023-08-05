from app import app, db
from flask import request, jsonify
from app.models import Product

# Listagem

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.__dict__ for product in products])

# Criação

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json  # Assume que os dados são enviados em JSON
    new_product = Product(**data)
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify(new_product.__dict__), 201

# Visualização por ID

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.__dict__)


# Atualização por ID

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    data = request.json
    for key, value in data.items():
        setattr(product, key, value)
    
    db.session.commit()
    
    return jsonify(product.__dict__)

# Esclusão por ID

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({"message": "Product deleted"})

