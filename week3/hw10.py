#輸入玩家A的三張卡牌
a1 = input()
a2 = input()
a3 = input()
#輸入玩家B的三張卡牌
b1 = input()
b2 = input()
b3 = input()

#卡片及對應點數轉換
def transferPoint(card):
    pork = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.5, 0.5, 0.5]
    index = pork.index(card)
    return points[index]

#加總點數(調整點數)
def getSum(x, y, z):
    first = transferPoint(x)
    second = transferPoint(y)
    third = transferPoint(z)
    sum = first + second + third
    if (sum > 10.5):
        sum = 0
    return sum
    
#玩家A和玩家B比大小
def compare(A, B):
    if (A > B):
        print('A Win')
    elif (B > A):
        print('B Win')
    else:
        print('Tie')
    
A_point = getSum(a1, a2, a3)
B_point = getSum(b1, b2, b3)
print(A_point)
print(B_point)
compare(A_point, B_point)