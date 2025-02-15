countries = {"Russia": "Mosscow", "Pakistan": "Islamabad", "Japan": "Tokyo"}

for country, capital in countries.items():
    print(f"{country}: {capital}")   # Output: Russia: Mosscow
                                            # Pakistan: Islamabad
                                            # Japan: Tokyo

print("Pakistan" in countries)       # Output: True

print(list(countries.values()))      # Output: ['Mosscow', 'Islamabad', 'Tokyo']
 