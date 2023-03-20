import sys

type_picture = int(input())
n = int(input())

def myprint(n, i, mark):
    print(mark*(n-i), end='')
    
def myprint2(n, i, mark):
    print(mark*(i-1), end='')
    
def myprint3(n, i):
    if i <= 0:
        print('_'*((n//2)+i), end='')
    else:
        print('_'*((n//2)-i), end='')
    
def printpicture(n, i):
    myprint(n, i, '_')
    for j in range(1, n+1):
        if i % 2 != 0:
            print(j, end='')
        else:
            print(n-j+1, end='')
    myprint2(n, i, '_')
    print()
    
def printpicture2(n, i):
    myprint2(n, i, '_')
    for j in range(1, n+1):
        if i % 2 == 0:
            print(j, end='')
        else:
            print(n-j+1, end='')
    myprint(n, i, '_')
    print()

#朝右邊斜的平行四邊形
if type_picture == 1:
    for i in range(1, n+1):
        printpicture(n, i)
        
#朝左邊斜的平行四邊形                
elif type_picture == 2:
    for i in range(1, n+1):
        printpicture2(n, i)
        
#沙漏型    
elif type_picture == 3:
    if n % 2 == 0: #若n為偶數
        print('ERROR')
        sys.exit()
    for i in range(-(n//2), (n//2)+1):
        myprint3(n, i)
        for j in range(-abs(i), abs(i)+1):
            if j < 0:
                print(abs(j)+1, end='')
            else:
                print(j+1, end='')
        myprint3(n, i)
        print()