x = 69  

def modify_x():
    x = 10  
    return f"Inside function, x is {x}"     # Output: Inside function, x is 10

print(modify_x())
print(f"Outside function, x is {x}")    # Output: Outside function, x is 69