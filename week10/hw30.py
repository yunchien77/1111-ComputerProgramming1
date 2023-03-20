#hw30
def input_passward():
    passward_list = []
    while(1):
        passward = input()
        if passward == '-1':
\            break
        passward_list.append(passward)
        if len(passward_list) >= 5:
            break
    return passward_list

def count_score(list):
    point_score = []
    symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '_', '+', '=']
    for i in range(len(list)):
        N, X, Y, M = 0, 0, 0, 0
        point = 0
        count = 0  #計算不相鄰數字出現次數
        for j in list[i]:
            if j.islower():
                N += 1
            elif j.isupper():
                X += 1
            elif j.isdigit():
                Y += 1
            elif j in symbol:
                M += 1
        point = N + X*3 + Y*2 + M*5
        
        for n, k in enumerate(list[i]):
            if k.isdigit():
                if n == len(list[i]) - 1: #最後一個元素為數字
                    count += 1
                elif not (list[i])[n+1].isdigit():  #數字的下一個元素不是數字
                    count += 1
        if count >= 5:
            point += 15
        point_score.append(point)
    return point_score
                
def main():
    list = input_passward()
    point = count_score(list)
    print(list[point.index(max(point))], max(point))
    print(list[point.index(min(point))], min(point))
    
main()