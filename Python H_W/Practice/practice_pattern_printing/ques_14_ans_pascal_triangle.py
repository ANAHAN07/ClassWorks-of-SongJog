x = 10

for i in range(x):
    print(' ' * (x - i - 1), end='')
    out_num = 1
    for j in range(i + 1):
        print(out_num, end=' ')
        out_num = out_num * (i - j) // (j + 1)
    print()


# Output:

"""
             1 
            1 1
           1 2 1
          1 3 3 1
         1 4 6 4 1
        1 5 10 10 5 1
       1 6 15 20 15 6 1
      1 7 21 35 35 21 7 1
     1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1
"""