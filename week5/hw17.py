#輸入三角形樣式
type_picture = int(input()) 
#輸入三角形行數
n = int(input()) 

#正三角形印底線
def equilateral_triangle(n, i, mark):
    print(mark*(n-i), end='')
    
    
def myprint(i):
    for j in range(1, 2*i):
        if i >= j:
            print(j, end='')
        else:
            print(2*i-j, end='')
    
#直角三角形
if type_picture == 1: 
    for i in range(1, n+1):
        myprint(i)
        print()
        
#正三角形
elif type_picture == 2: 
    for i in range(1, n+1):
        equilateral_triangle(n, i, '_')
        myprint(i)
        equilateral_triangle(n, i, '_')
        print()
    
#倒三角形
elif type_picture == 3: 
    for i in range(n, 0, -1):
        equilateral_triangle(n, i, '_')
        myprint(i)
        equilateral_triangle(n, i, '_')
        print()