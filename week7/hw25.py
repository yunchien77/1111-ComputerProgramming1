#hw25

def printROW(m, n, s, mark):
    for i in range(m, n, s):
        if mark.isdigit():
            print(i, end='')
        else:
            print(mark, end='')
            
def myprint(i, list):
    print('*', end='')
    if i != 1:
        for j in range(i-1):
            print(list[i-2], end='')
            print('*', end='')
            
def main():
    n = int(input())
    if n != 1 and n != 2:
        print('ERROR')
        return 0
        
    m = int(input())
    if n == 1 and (m<1 or m>29):
        print('ERROR')
        return 0
    if n == 2 and (m<2 or m>9):
        print('ERROR')
        return 0
        
    letter_list = ['A', 'B', 'C']*int((m//2.5))
    
    if n == 1:
        for i in range(1, m+1):
            printROW(m-i, 0, -1, '#')
            myprint(i, letter_list)
            printROW(m-i, 0, -1, '#')
            print()
    elif n == 2:
        for i in range(1, m+1):
            printROW(1, i+1, 1, '0')
            printROW(2*m, 2*i-2, -1, '*')
            printROW(i, 0, -1, '0')
            print()
main()
    
    