def generateCode(x:int, N:int):  #有2^N種排列組合
    code =''
    for i in range(N):
        if x>0:
            code = code + str(x%2)
            x = x//2
        else:
            code = code + str('0')
    return code 
'''
0000
1000
0100
1100
0010
1010
0110
1110
0001
1001
0101
1101
0011
1011
0111
1111'''

def checkValidRoom(M:int, N:int, data:list, code:str, mostUse:list):
    #data = [[3], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4], [1, 2]]
    section=[] #所有使用節數時段
    timeCount=[] #24節數時段使用會議室量
    counter = 0
    for i in range(len(code)): #i = 0~3
        if code[i]=='1':
            section = section + data[i]
            counter += 1
    timeCount=[section.count(i) for i in range(24)]
    if max(timeCount)>M: #超過教室數量
        return False, 0, mostUse
    else:
        mostUse.append(counter)
        return True, timeCount, mostUse
    
def computeMaxHours(M:int, N:int, data:list):
    maxHours = 0
    mostUse = []
    for x in range(2**N):
        code = generateCode(x, N)
        flag, timeCount, mostUse = checkValidRoom(M, N, data, code, mostUse)
        if flag==True and sum(timeCount)>maxHours:
            maxHours=sum(timeCount)
    return (maxHours), mostUse


def process():
    x =input().split()
    M, N = int(x[0]), int(x[1])
    data = []
    for i in range(N):
        x =input().split()
        data.append([int(x[1]), int(x[2])])
    # print(data) #[[3, 4], [1, 10], [1, 5], [1, 3]]
    td = [[t for t in range(d[0], d[1])] for d in data] #轉換節數時段表達
    # print(td) #[[3], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4], [1, 2]]

    maxHours, mostUse = computeMaxHours(M, N, td)
    print(maxHours)
    print(max(mostUse))
    

    
process()