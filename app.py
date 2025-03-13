from flask import Flask, request, jsonify
from models import db, Product
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price
    } for product in products])

@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({
        'id': new_product.id,
        'name': new_product.name,
        'description': new_product.description,
        'price': new_product.price
    }), 201

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price
    })

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    db.session.commit()
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price
    })

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
