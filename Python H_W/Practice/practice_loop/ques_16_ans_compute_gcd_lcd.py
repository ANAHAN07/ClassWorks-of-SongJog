import math

x, y = map(int, input("Enter two numbers: ").split())   # Output: Enter two numbers: 534 567
gcd = math.gcd(x, y)
lcm = (x * y) // gcd

print("GCD:", gcd)      # Output: GCD: 3
print("LCM:", lcm)      # Output: LCM: 100926
