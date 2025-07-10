def aplicate_coupon(price, coupon):
    discounts = {
        "OFFER10": 0.10,
        "SUPER20": 0.20,
        "WELCOME": 0.15
    }
    if coupon in discounts:
        return round(price * (1- discounts[coupon]),2)
    return price

def calculate_price_final(price_base, coupon, tax_rate=0.19):
    price_desc = aplicate_coupon(price_base,coupon)
    return round(price_desc * (1 + tax_rate), 2)
