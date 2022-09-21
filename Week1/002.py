import math

a = int(input())
b = int(input())
c = int(input())

sol1 = ((-b)+math.sqrt(b**2-4*a*c))/(2*a)
sol2 = ((-b)-math.sqrt(b**2-4*a*c))/(2*a)

print("%.1f" %sol1)
print("%.1f" %sol2)