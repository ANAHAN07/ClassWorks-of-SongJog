def order_summary(item, quantity, price):
    total = quantity * price
    return f"Order Placed: {quantity} {item}(s) for a total of {total:.2f}৳"

print(order_summary("Dragon Fruit", 10, 6.9))                   # Output: Order Placed: 10 Dragon Fruit(s) for a total of 69.00৳ 
print(order_summary(price=3.9, quantity=25, item="grapes"))     # Output: Order Placed: 25 grapes(s) for a total of 97.50৳
