#hw26

def calculate_sum(k):
    sum = 0
    for i in range(1, k+1):
        sum += (i**i)
    return sum

n = int(input())
list = []

for i in range(n):
    k = int(input())
    list.append(k)

for i in range(n):
    if 1<=list[i]<=15:
        result = calculate_sum(list[i])
        print(result)
        new_list = [x for x in reversed(str(result))]
        print(','.join(new_list))
    else:
        print('ERROR')