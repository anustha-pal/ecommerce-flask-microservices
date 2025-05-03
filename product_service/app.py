from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/products')
def product_page():
    products = [
        {"name": "Laptop", "price": 999},
        {"name": "Headphones", "price": 199}
    ]
    return render_template("products.html", products=products)

@app.route('/products/api')
def product_api():
    return jsonify([
        {"name": "Laptop", "price": 999},
        {"name": "Headphones", "price": 199}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

