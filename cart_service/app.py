from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/cart')
def view_cart():
    try:
        res = requests.get("http://product_service:5001/products/api")
        products = res.json()
    except:
        products = []
    return render_template("cart.html", products=products)

@app.route('/cart/api')
def cart_api():
    return jsonify({"user": "123", "items": ["Laptop", "Headphones"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
