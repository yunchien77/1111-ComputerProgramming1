#hw40

#(參數說明: 遊戲玩家所填數字, 賓果數字, 賓果宮格行/列數)
# 1:賓果數字; 0:未賓果數字
def mapData(data, selected, N):
    mData = [[0 for i in range(N)] for j in range(N)] #初始化陣列
    for x in selected: #針對挑選數字
        index=data.index(x) #找出九宮格相對位置
        mData[index//N][index%N] = 1 # 轉出設定對應0/1檢測矩陣
    # print(mData)
    return mData #回傳0/1檢測矩陣

def checkBingo(mdata, N): #0/1矩陣
    count = 0
    for i in range(N): #對角線1
        if mdata[i][i] == 1:
            count = count + 1
    if count==N: return True
    
    for i in range(N): #對角線2
        if mdata[i][N-i-1] == 1:
            count = count + 1
    if count==N: return True
    
    for i in range(N): #3條水平線
        count = 0
        for j in range(N):
            if mdata[i][j] == 1:
                count = count + 1
        if count==N: return True
    
    for i in range(N): #3條垂直線
        count = 0
        for j in range(N):
            if mdata[j][i] == 1:
                count = count + 1
        if count==N: return True
    return False

def input_data():
    N,M = map(int, input().split())
    #九宮格輸入(使用者設定的資料)
    A_data = list(map(int, input().split()))
    B_data = list(map(int, input().split()))
    selected = list(map(int, input().split()))
    return N, A_data, B_data, selected

def test01():
    N, A_data, B_data, selected = input_data()
    #轉成 【0/1檢測矩陣】
    A_mData = mapData(A_data, selected, N) 
    B_mData = mapData(B_data, selected, N)
    #【判斷0/1檢測矩陣連線】
    A_result = checkBingo(A_mData, N) 
    B_result = checkBingo(B_mData, N)
    if A_result & B_result:  #若A和B皆為True
        print('Tie')
    elif A_result:
        print('A Win')
    elif B_result:
        print('B Win')
        
test01()