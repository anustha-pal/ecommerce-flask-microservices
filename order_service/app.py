from flask import Flask, jsonify, request

app = Flask(__name__)
orders = []

@app.route("/orders", methods=["POST"])
def create_order():
    order = request.json
    order["id"] = len(orders) + 1
    orders.append(order)
    return jsonify(order), 201

@app.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    user_orders = [o for o in orders if o["user_id"] == user_id]
    return jsonify(user_orders)

if __name__ == "__main__":
    app.run(debug=True, port=5004)
