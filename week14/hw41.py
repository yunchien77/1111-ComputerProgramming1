#hw41
def get_data():
    university = {}
    n = int(input())
    for i in range(n):
        item = input().split()
        university[item[0]] = set(item[1:])
    return university  #university={'大學名稱':[屬性1, 屬性2,...]}

def match(condition, feature):
    if '+' in condition:
        condition = condition.split(' + ')
    else:
        condition = [condition]
    counter = 0
    for i in range(len(condition)):
        if feature.issuperset(set(condition[i].split())): #issuperset()判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False
            counter += 1
    return counter

def compute(condition, university, b):
    data = {}
    result = []
    for name, feature in university.items():
        data[name] = match(condition, feature)
    if b == 0:
        for key in data:
            if data[key] > 0:
                result.append(key)
    elif b == 1:
        maxNum = max(data.values())
        for key, value in data.items():
            if value == maxNum:
                result.append(key)
    return result
    
def main():
    university = get_data()
    allCondition = []
    m = int(input())
    for i in range(m):
        allCondition.append(input())
    b = int(input())  #b=0，輸出能符合條件的房屋當;b=1，輸出符合最多條件的房屋
    for condition in allCondition:
        ans = compute(condition, university, b)
        ans.sort()
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
  
main()
