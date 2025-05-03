from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
cart = {}
PRODUCT_SERVICE_URL = "http://product_service:5001"

@app.route("/cart/<int:user_id>", methods=["GET"])
def get_cart(user_id):
    return jsonify(cart.get(user_id, []))

@app.route("/cart/<int:user_id>", methods=["POST"])
def add_to_cart(user_id):
    item = request.json
    product_id = item.get("product_id")

    # Validate product with Product Service
    resp = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    if resp.status_code != 200:
        return jsonify({"error": "Product not found"}), 404
    product = resp.json()

    cart.setdefault(user_id, []).append(product)
    return jsonify({"message": "Item added to cart", "cart": cart[user_id]}), 201

@app.route("/cart/<int:user_id>/clear", methods=["POST"])
def clear_cart(user_id):
    cart[user_id] = []
    return jsonify({"message": "Cart cleared"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)