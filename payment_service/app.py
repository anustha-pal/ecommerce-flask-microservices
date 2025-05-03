from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/payment')
def payment_page():
    try:
        orders = requests.get("http://order_service:5004/orders/api").json()
    except:
        orders = []
    return render_template("payment.html", orders=orders)

@app.route('/payment/api')
def payment_api():
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
