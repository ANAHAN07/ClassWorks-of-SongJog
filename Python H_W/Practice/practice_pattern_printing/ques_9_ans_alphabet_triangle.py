x = 15

for i in range(1, x + 1):
    print(''.join(chr(65 + j) for j in range(i)))

# Output:

"""
    A
    AB
    ABC
    ABCD
    ABCDE
    ABCDEF
    ABCDEFG
    ABCDEFGH
    ABCDEFGHI
    ABCDEFGHIJ
    ABCDEFGHIJK
    ABCDEFGHIJKL
    ABCDEFGHIJKLM
    ABCDEFGHIJKLMN
    ABCDEFGHIJKLMNO
"""