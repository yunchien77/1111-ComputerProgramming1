import math

a = int(input('第一個數(int)a:'))
b = int(input('第二個數(int)b:'))
c = int(input('第三個數(int)c:'))
x1 = ((-b) + math.sqrt(b*b-4*a*c)) / (2*a)
x2 = ((-b) - math.sqrt(b*b-4*a*c)) / (2*a)
print("%.1f" %x1)
print("%.1f" %x2)