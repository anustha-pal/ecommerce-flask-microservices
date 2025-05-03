from flask import Flask, jsonify, request

app = Flask(__name__)
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = next((u for u in users if u["id"] == id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    user = request.json
    user["id"] = len(users) + 1
    users.append(user)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
