y = 4
length = 16

for i in range(1, y + 1):
    for j in range(1, length + 1):
        if (i + j) % y == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Output:

"""
    *   *   *   * 
       *   *   *   *  
    *   *   *   *   
       *   *   *   *
"""