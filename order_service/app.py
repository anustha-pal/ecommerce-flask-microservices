import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
orders = []

CART_SERVICE_URL = "http://cart_service:5002"
PRODUCT_SERVICE_URL = "http://product_service:5001"
PAYMENT_SERVICE_URL = "http://payment_service:5005"

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    user_id = data["user_id"]

    # Step 1: Get items from Cart Service
    cart_resp = requests.get(f"{CART_SERVICE_URL}/cart/{user_id}")
    items = cart_resp.json()

    # Step 2: Optionally validate products (skipped here)
    # Step 3: Process payment
    total_amount = sum([item["price"] for item in items])
    payment_resp = requests.post(f"{PAYMENT_SERVICE_URL}/pay", json={"amount": total_amount})
    payment_result = payment_resp.json()

    if payment_result.get("status") != "paid":
        return jsonify({"error": "Payment failed"}), 400

    # Step 4: Save order
    order = {
        "id": len(orders) + 1,
        "user_id": user_id,
        "items": items,
        "total": total_amount,
        "payment": payment_result,
    }
    orders.append(order)

    # Step 5: Clear cart
    requests.post(f"{CART_SERVICE_URL}/cart/{user_id}/clear")

    return jsonify(order), 201

@app.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    user_orders = [o for o in orders if o["user_id"] == user_id]
    return jsonify(user_orders)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5004)
