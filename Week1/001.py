import math

a = int(input())
b = int(input())
c = int(input())

x1 = ((-b)+math.sqrt(b**2-4*a*c))/(2*a)
x2 = ((-b)-math.sqrt(b**2-4*a*c))/(2*a)

print("%.1f" %x1)
print("%.1f" %x2)
