def calcu_total_price( *, price, quantity):
    return price * quantity

product = "rice"
total = calcu_total_price(price=69, quantity=8)
print(f"The total price for {product} is: {total}")