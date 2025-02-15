car = [
    {"Brand": "Toyota", "Model": "Corolla", "Price": 20000},
    {"Brand": "BMW", "Model": "X5", "Price": 50000},
    {"Brand": "Ford", "Model": "Mustang", "Price": 35000}
]

most_expensive_car = max(car, key=lambda car: car["Price"])
print("Most Expensive Car:", most_expensive_car["Brand"], most_expensive_car["Model"])   # Output: Most Expensive Car: BMW X5

car[1]["Price"] = 55000

car.append({"Brand": "Audi", "Model": "A4", "Price": 40000})  

print(car)  # Output: [{'Brand': 'Toyota', 'Model': 'Corolla', 'Price': 20000}, 
                # {'Brand': 'BMW', 'Model': 'X5', 'Price': 55000}, 
                # {'Brand': 'Ford', 'Model': 'Mustang', 'Price': 35000}, 
                # {'Brand': 'Audi', 'Model': 'A4', 'Price': 40000}]
