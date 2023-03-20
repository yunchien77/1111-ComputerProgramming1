import sys

n = int(input())
if n<1 or n>=10:
    print('ERROR')
    sys.exit()

def printOneRow(m, n, s, mark):
    for i in range(m, n, s):
        if mark.isdigit():
            print(i, end='')
        else:
            print(mark, end='')
            
for i in range(1, n+1):
    printOneRow(n, i, -1, '#')
    printOneRow(1, i+1, 1, '*')
    print(' ', end='')
    printOneRow(1, i+1, 1, '0')
    print()
for i in range(1, n+1):
    printOneRow(0, i-1, 1, '#')
    printOneRow(n, i-1, -1, '0')
    print(' ', end='')
    printOneRow(n, i-1, -1, '*')
    print()
    
    
    