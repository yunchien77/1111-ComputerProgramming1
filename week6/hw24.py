n = int(input())
D = int(input())

def printOriginalSquare(n):
    x = y = 0
    while x < n:
        print('%3d' %(x*n+y), end='')
        y += 1
        if y >= n:
            y = 0
            x += 1
            print()
            
#矩陣向左轉
def t1(i, n):
    x1 = i//n
    y1 = i%n
    y2 = n-x1-1
    x2 = y1
    return (x2*n+y2)

#矩陣向右轉
def t2(i, n):
    x1 = i//n
    y1 = i%n
    y2 = x1
    x2 = n-y1-1
    return (x2*n+y2)

#矩陣上下翻轉
def t3(i, n):
    x1 = i//n
    y1 = i%n
    x2 = n-x1-1
    y2 = y1
    return (x2*n+y2)

#矩陣左右翻轉
def t4(i, n):
    x1 = i//n
    y1 = i%n
    x2 = x1
    y2 = n-y1-1
    return (x2*n+y2)

def printToSquare(n, func):
    i = 0
    while i < n*n:
        print('%3d' %func(i, n), end='')
        i += 1
        if i % n == 0:
            print()
            
'''         
def printSquare1(n):
    i = 0
    while i < n*n:
        print('%3d ' %t1(i, n), end='')
        i += 1
        if i % n == 0:
            print()
            
def printSquare2(n):
    i = 0
    while i < n*n:
        print('%3d ' %t2(i, n), end='')
        i += 1
        if i % n == 0:
            print()
            
def printSquare3(n):
    i = 0
    while i < n*n:
        print('%3d ' %t3(i, n), end='')
        i += 1
        if i % n == 0:
            print()
            
def printSquare4(n):
    i = 0
    while i < n*n:
        print('%3d ' %t4(i, n), end='')
        i += 1
        if i % n == 0:
            print()
'''

if D == 0:
    printOriginalSquare(n)
elif D == 1:
    printToSquare(n, t1)
elif D == 2:
    printToSquare(n, t2)
elif D == 3:    
    printToSquare(n, t3)
elif D == 4:
    printToSquare(n, t4)