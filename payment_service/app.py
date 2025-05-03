from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/pay", methods=["POST"])
def make_payment():
    data = request.json
    amount = data.get("amount", 0)
    # Simulate payment success
    return jsonify({"message": "Payment successful", "status": "paid", "amount": amount}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
