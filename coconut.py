__author__ = 'Theo'


#Write a program that will find the initial number
#of coconuts.

def f(n):
    return (n-1) / 5 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n

def is_int(n):
    return abs(n-int(n)) < 0.0000001

# Enter code here.
found = False
n = 0
while not found :
    n += 1
    result = f6(float(n))
    found = is_int(result)

print n