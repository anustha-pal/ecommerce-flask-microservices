from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/orders')
def order_list():
    try:
        users = requests.get("http://user_service:5003/users/api").json()
    except:
        users = []
    return render_template("orders.html", users=users)

@app.route('/orders/api')
def order_api():
    return jsonify({
        "orders": [
            {"id": 1, "user_id": 1, "total": 999},
            {"id": 2, "user_id": 2, "total": 199}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
