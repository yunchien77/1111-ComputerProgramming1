#hw37
import math

def input_data():
    n = int(input())
    m = int(input())
    wooden_pallet = []
    for i in range(m):
        wooden_pallet.append([])
    return n, wooden_pallet

#檢查是否為平方數
def check(num):
    x = int(math.sqrt(num))
    if x == math.sqrt(num):
        return 1  #完全平方數
    return 0  #非完全平方數

#重新排列二維列表
def sorted_list(list):
    for i in range(len(list)):
        list[i].sort()
    list.sort()
    sort_list = sorted(list, key=lambda x:len(x), reverse=False)
    return sort_list

#刪除空列表
def remove_nested_list(listt):
    for index, value in enumerate(reversed(listt)):
        if isinstance(value, list) and value != []:
            remove_nested_list(value)
        elif isinstance(value, list) and len(value) == 0:
            listt.remove(value)

def exist(list, num):
    for i in list:
        if num in i:
            return 1 #存在
    return 0 #不存在

def main():
    n, wooden_pallet = input_data()
    wooden_pallet[0].append(1)
    for i in range(2, n+1):
        for j in range(len(wooden_pallet)):
            if wooden_pallet[j] != []:
                if check(wooden_pallet[j][-1] + i) == 1:
                    wooden_pallet[j].append(i)
                    break
            else:  #空木棧板
                wooden_pallet[j].append(i)
                break
            
    #倉庫已達貨物上限，還有貨物尚未放置倉庫中
    for i in range(1, n+1):
        if exist(wooden_pallet, i) == 0:
            print('False')
            return 0
 
    #所有貨物皆放置於倉庫中且未達置物上限
    print('True')        
    remove_nested_list(wooden_pallet)
    new_pallet = sorted_list(wooden_pallet)
    for i in range(len(new_pallet)):
        print(' '.join(map(str, new_pallet[i])))  #使用join要先將元素轉成string
        
main()