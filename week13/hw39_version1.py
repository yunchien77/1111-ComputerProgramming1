def input_data():
    data = list(map(int, input().split()))
    graph = {}
    for i in range(data[0]):
        path = list(map(int, input().split()))
        if path[0] not in graph:
            graph[path[0]] = [path[1]]
        else:
            graph[path[0]].append(path[1])
        if path[1] not in graph:
            graph[path[1]] = [path[0]]
        else:
            graph[path[1]].append(path[0])
    if len(data) > 3:
        return graph, data[1], data[2], data[3] #data, source, target, mustPassed
    return graph, data[1], data[2], 0  #data, source, target(mustPassed為零代表無規定必經之路)

def findNeighbour(data, source, target):
    passedNodes = dict() # 拜訪過的節點，{節點:level}
    stack = [[source,0]] # 待拜訪節點，[開頭點: level=0]
    while True:
        if len(stack)==0: 
            return 'NO' # 待拜訪節點，找不到
        currentNode = stack.pop(0) # 取出一個待拜訪節點，取出並從stack刪除
        currentNodeName = currentNode[0] # 取出該節點名稱
        level = currentNode[1] # 取出該節點 level
        if currentNodeName == target: # 找到最終節點(走到target)
            path = findPath(data, passedNodes, currentNodeName, level-1, target) #找路徑
            return path  #最短路徑
        passedNodes[currentNodeName] = level # 不是最終節點，存入(拜訪過節點)
        
        for node in data[currentNodeName]: # 針對每一個相鄰節點，存入(待拜訪節點)
            if node not in passedNodes.keys(): # 假如此節點尚未拜訪過
                stack.append([node, level+1]) # 只存(未拜訪過節點stack)

        
def test01():
    data, source, target, mustPassed = input_data()
    if mustPassed == 0:
        result = findNeighbour(data, source, target)
    else: #有必經路徑
        result1 = findNeighbour(data, source, mustPassed)
        result2 = findNeighbour(data, mustPassed, target)
        if type(result1) or type(result2) is str:
            result = 'NO'
        else:
            result2.pop(0)
            result = result1 + result2
            
    if type(result) is list:  #印出路徑
        print(len(result)-1)
        for i in range(len(result)):
            print(result[i], end=' ')
    else:  #找不到
        print(result)

def findPrevNode(data, passedNodes: dict, targetNodeName, level):#找上一層
    nodeCandidate = []
    for nodeName, nodeLevel in passedNodes.items(): #走過的節點
        if nodeLevel==level: 
            nodeCandidate.append(nodeName) # 所有上一層節點
    for nodeName in nodeCandidate:
        if targetNodeName in data[nodeName]: 
            return nodeName # K 相鄰節點是 F，回傳K

def findPath(data, passedNodes, currentNodeName, level, target): #尋找走過的路徑
    path = []
    while level >= 0: #找到level=0 停止
        nodeName = findPrevNode(data, passedNodes, currentNodeName, level)
        path.append(nodeName) #找 F 上一個節點 K
        level = level-1 #level-1 往上一節點找
        currentNodeName = nodeName # 找到上一節點K，繼續往上找B
    path.insert(0, target)
    path.reverse()
    return path

test01()