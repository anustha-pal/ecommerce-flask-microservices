from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/users')
def user_list():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    return render_template("users.html", users=users)

@app.route('/users/api')
def user_api():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
