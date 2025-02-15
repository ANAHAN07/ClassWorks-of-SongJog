products = {"Laptop": 1000, "Phone": 800, "Tablet": 500}
coupon = "laptop7807"
web = ("https://laptopache.com/")

for product, price in products.items():
    print(f"{product}: ${price}")      # Output: Laptop: $1000
                                               # Phone: $800
                                               # Tablet: $500

most_expensive_product = max(products, key=products.get)
print("Most Expensive Product:", most_expensive_product)  # Output: Most Expensive Product: Laptop

print("Phone" in products)                                  # Output: True
print(f"For discount use this coupon code {coupon}")        # Output: For discount use this coupon code laptop7807
print(f"Buy the products from {web}\nThanks")               # Output: Buy the products from https://laptopache.com/
                                                                    # Thanks