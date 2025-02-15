x = 69
print(x)

def myfun():
    global x
    x= 2
    return x

print(myfun())
print(x)