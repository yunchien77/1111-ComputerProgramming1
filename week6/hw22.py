import sys

n = int(input())
if n % 2 == 0 or n < 4 or n > 30:
    print('Error')
    sys.exit()

def printOneRow(m, n, s, mark):
    for i in range(m, n, s):
        if mark.isdigit():
            print(i, end='')
        else:
            print(mark, end='')
            
for i in range(1, n//2+2):
    printOneRow(1, 2*i, 1, '*')
    printOneRow(n-i, i-1, -1, '_') 
    printOneRow(n-i, i-1, -1, '_') 
    printOneRow(1, 2*i, 1, '*')
    print()
for i in range(n-2, 0, -2):
    printOneRow(i, 0, -1, '*')
    printOneRow(1, n-i+1, 1, '_')
    printOneRow(1, n-i+1, 1, '_')
    printOneRow(i, 0, -1, '*')
    print()