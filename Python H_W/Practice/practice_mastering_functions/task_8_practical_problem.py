def convert_temperature(value, mode):
    if mode == "CtoF":
        return f"{value}°C is {value * 9/5 + 32}°F"
    elif mode == "FtoC":
        return f"{value}°F is {(value - 32) * 5/9}°C"
    else:
        return "Invalid mode! Use 'CtoF' or 'FtoC'."

print(convert_temperature(41, "CtoF"))          # Output: 41°C is 105.8°F
print(convert_temperature(110, "FtoC"))         # Output: 110°F is 43.333333333333336°C