y = 10

for i in range(1, y + 1):
    left = ''.join(str(j) for j in range(1, i + 1))
    right = ''.join(str(j) for j in range(i - 1, 0, -1))
    print(' ' * (y - i) + left + right)

# Output: 

"""
             1
            121
           12321
          1234321
         123454321
        12345654321
       1234567654321
      123456787654321
     12345678987654321
    12345678910987654321
"""