import sys

def myPrint(n, mark):
    for i in range(n):
        print(mark, end='')

def triangle_1(n):
    for i in range(n):
        if i <= (n//2):
            # print('*' * (i+1), end='')
            myPrint(i+1, '*')
        else:
            # print('*' * (n-i), end='')
            myPrint(n-i, '*')
        print('\n')
    
def triangle_2(n):
    for i in range(n):
        if i <= (n//2):
            myPrint(n//2-i, '.')
            myPrint(i+1, '*')
        else:
            myPrint(i-(n//2), '.')
            myPrint(n-i, '*')
        print('\n')
                 
def triangle_3(n):
    count = 1
    for i in range(n):
        if i <= (n//2):
            myPrint(n//2-i, '.')
            myPrint(2*i+1, '*')
            myPrint(n//2-i, '.')
        else:
            myPrint(i-n//2, '.')
            myPrint(n-2*count, '*')
            count += 1
            myPrint(i-n//2, '.')
        print('\n')
    

type = int(input())
n = int(input())
if n % 2 == 0:
    print('ERROR')
    sys.exit()

if type == 1:
    triangle_1(n)
elif type == 2:
    triangle_2(n)
elif type == 3:
    triangle_3(n)
    
    