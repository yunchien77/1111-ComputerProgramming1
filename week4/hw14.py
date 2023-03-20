# -*- coding: utf-8 -*-
"""
輸入N個字串，請執行以下操作
1. 印出這N個字串中所有的小寫字母
(注意:若沒有字串中沒有小寫字母則輸出'No lowercase letters')
2. 輸出這N個字串中所有大寫字元的數量
3. 輸出這N個字串共有多少個字元 (含標點符號與空格)
4. 以空格分割這N個字串，將其中長度最長的單字輸出

---------------------------------------------------

輸入說明 :
第一行，輸入整數 N，代表接下來有N行輸入
第二 ~ N+1 行，輸入的字串，根據這N行執行操作1~4

輸出說明 :
第一行，輸出N個字串中所有的小寫字母
第二行，輸出N個字串中所有大寫字元的數量
第三行，輸出N個字串中所有字元的數量 (含標點符號、特殊字元與空格)
第四行，輸出以空格分割這N個字串後，其中長度最長的字串；若有多個長度最長的字串，輸出最早出現的字串

---------------------------------------------------

範例輸入 1說明:
2 (接下來輸入2行)
I have a pen I have an apple
Pen pineapple apple pen

範例輸出 1說明:
haveapenhaveanappleenpineappleapplepen (輸入的2個字串所有小寫字元)
3 (輸入的2個字串總共有2個大寫字元 (2個I))
51 (輸入的2個字串共有51個字元)
pineapple (以空格切分輸入的2個字串後，得到的所有字串為['I', 'have', 'a', 'pen', 'I', 'have', 'an', 'apple', 'Pen', 'pineapple', 'apple', 'pen']，其中最長的字串為'pineapple')
"""
def upper(list):
    upper = []
    for i in list:
        if i.isupper():
            upper += i
    print(len(upper))
            
def lower(list):
    lower = []
    for i in list:
        if i.islower():
            print(i, end='')
            lower += i
    print('\n')
    if lower == []:
        print('No lowercase letters')
            
            
N = int(input())
list = []
for i in range(N):
    list += ' ' + input()
lower(list)
upper(list)
print(len(list) - N)
newlist = ''.join(list)
afterSplit = newlist.split(' ')
longestString = max(afterSplit, key=len, default='')
print(longestString)