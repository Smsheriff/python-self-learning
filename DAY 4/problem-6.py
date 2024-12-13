def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
a=60
b=48
result=gcd(a,b)
print(result)
