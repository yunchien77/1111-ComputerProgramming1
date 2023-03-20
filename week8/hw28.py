#hw28
n = int(input())
list = []
for i in range(n):
    m = input().split()
    if m[0] == 'ADD':
        list.append(m[1])
        continue
        
    elif m[0] == 'INSERT':
        if m[1] in list:
            list.insert(list.index(m[1]), m[2])
        continue
        
    elif m[0] == 'REMOVE':
        if m[1] in list:
            list.remove(m[1])
        continue
        
if list == []:
    print('list is null')
else:
    for i in range(len(list)):
        print(list[i], end=' ')