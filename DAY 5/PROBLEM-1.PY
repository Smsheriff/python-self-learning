# LCM

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
a = 12
b = 15
result = lcm(a, b)
print( result)