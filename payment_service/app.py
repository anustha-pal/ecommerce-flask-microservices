from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/pay", methods=["POST"])
def make_payment():
    data = request.json
    # Simulate payment processing
    return jsonify({"message": "Payment successful", "status": "paid", "amount": data.get("amount", 0)}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5005)
