A = input()
B = input()
x = input()
y = input()
C = A + B
D = C.replace(x, y)
print(len(C + D))
E = D[:3] + D[-3:]
for i in range(3):
    print(E, end='')