#hw27

def compute(i):
    origlist = [i]
    while(1):
        if 1 in origlist:
            break
        if i % 2 != 0: #奇數
            i = 3*i + 1
        else:          #偶數
            i = i // 2
        origlist.append(i)  
    return origlist

def compared(n, m):
    newlist = []       
    for i in range(n, m+1):
        if len(compute(i)) > len(newlist):
            newlist = compute(i)
    print(len(newlist))

def main():
    n = int(input())
    m = int(input())

    if n<1 or n>10000 or n>m or m>10000:
        print('ERROR')
        return 0
    compared(n, m)
        
main()