## Calculate the sum of the digits of a random three-digit number.

from random import random

n = random()*900+100
n = int(n)
print(n)

s = str(n)

a = int(s[0])
b = int(s[1])
c = int(s[2])

print(a+b+c)