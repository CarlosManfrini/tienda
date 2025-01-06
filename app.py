from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key'  # Necesario para manejar sesiones

# Simulación de una base de datos con productos
products = [
    {'id': 1, 'name': 'Producto 1', 'price': 10.00},
    {'id': 2, 'name': 'Producto 2', 'price': 15.00},
    {'id': 3, 'name': 'Producto 3', 'price': 20.00},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return 'Producto no encontrado', 404
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    cart = session['cart']
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total_price = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
