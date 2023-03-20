def compute(A_data, B_data, selected, N, M):
    A_store = [0 for i in range(2*N+2)]
    B_store = [0 for i in range(2*N+2)]
    for num in selected:
        checkBingo(A_data, A_store, num, N)
        checkBingo(B_data, B_store, num, N)
        # print(storeA, storeB)
        if (N in A_store) and (N in B_store):
            return 'Tie'
        elif (N in A_store):
            return 'A Win'
        elif (N in B_store):
            return 'B Win'
    return 'Tie' 

def checkBingo(data, store, num, N):
    #算出x, y 座標位置
    row = data.index(num) // N
    col = data.index(num) % N 
    
    store[row] += 1
    store[col+N] += 1
    if row == col: #符合左上右下連線
        store[N*2] += 1
    if row==(N-1-col): #符合右上左下連線
        store[N*2+1] += 1

def input_data():
    N,M = map(int, input().split())
    #九宮格輸入(使用者設定的資料)
    A_data = list(map(int, input().split()))  #A玩家的宮格
    B_data = list(map(int, input().split()))  #B玩家的宮格
    selected = list(map(int, input().split()))  #賓果數字
    return N, M, A_data, B_data, selected

def main():
    N, M, A_data, B_data, selected = input_data()
    print(compute(A_data, B_data, selected, N, M))
    
main()