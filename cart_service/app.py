from flask import Flask, jsonify, request

app = Flask(__name__)
cart = {}

@app.route("/cart/<int:user_id>", methods=["GET"])
def get_cart(user_id):
    return jsonify(cart.get(user_id, []))

@app.route("/cart/<int:user_id>", methods=["POST"])
def add_to_cart(user_id):
    item = request.json
    cart.setdefault(user_id, []).append(item)
    return jsonify({"message": "Item added to cart", "cart": cart[user_id]}), 201

@app.route("/cart/<int:user_id>/clear", methods=["POST"])
def clear_cart(user_id):
    cart[user_id] = []
    return jsonify({"message": "Cart cleared"})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
