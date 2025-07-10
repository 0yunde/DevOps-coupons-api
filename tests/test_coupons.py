from app.coupons import aplicate_coupon, calculate_price_final

def test_discount_discount_offer10():
    assert aplicate_coupon(100, "SALES10") == 90.0

def test_discount_discount_super20():
    assert aplicate_coupon(200, "SUPER20") == 160.0

def test_discount_discount_welcome():
    assert aplicate_coupon(100, "WELCOME") == 85.0

def test_discount_discount_fake():
    assert aplicate_coupon(990, "FAKE") == 990   

def test_discount_discount_whit_discount():
    assert calculate_price_final(100, "SALES10") == 107.1