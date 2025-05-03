from flask import Flask, jsonify, request

app = Flask(__name__)
products = [
    {"id": 1, "name": "T-Shirt", "price": 19.99},
    {"id": 2, "name": "Sneakers", "price": 89.99},
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)
