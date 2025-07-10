from flask import Flask, request, jsonify
from app.coupons import calculate_price_final

app = Flask(__name__)

@app.route('/price', methods=['POST'])
def calculate():
    data = request.get_json()
    price = data.get("price")
    coupon = data.get("coupon")
    tax_rate = data.get("tax_rate", 0.19)

    final = calculate_price_final(price,coupon,tax_rate)
    return jsonify({"price_final":final})

