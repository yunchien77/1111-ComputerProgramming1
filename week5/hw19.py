import sys

n = int(input())

if n % 2 == 0:
    print('ERROR')
    sys.exit()

j = 1
k = 2*n - 1

def myprint(a, mark):
    print(mark * a, end='')
    
for i in range(-abs(n//2), (n//2)+1):
    myprint(2*abs(i), ' ')
    if i < 0:
        myprint(j, '*')
        j += 4
    else:
        myprint(k, '*')
        k -= 4
    myprint(abs(i)*4, ' ')
    myprint((n-2)-2*abs(i), '+')
    print()


# k = n // 2
# for i in range(-(n-k)+1, n-k):
#     print(" " * abs(i) + "*" *(k-abs(i)+1) + " " * abs(i)*2 + "+" *(k-abs(i)))
#     print()