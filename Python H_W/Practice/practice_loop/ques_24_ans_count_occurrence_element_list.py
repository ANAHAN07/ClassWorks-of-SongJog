num = [7, 9, 3, 7, 2, 9, 4, 7, 1, 4, 3, 2, 8, 9, 1, 8]  
count_dict = {}  

for n in num:  
    count_dict[n] = count_dict.get(n, 0) + 1  

for key, value in count_dict.items():  
    print(f"Element {key} appears {value} times")  

# Output:

"""
    Element 7 appears 3 times
    Element 9 appears 3 times
    Element 3 appears 2 times
    Element 2 appears 2 times
    Element 4 appears 2 times
    Element 1 appears 2 times
    Element 8 appears 2 times
"""