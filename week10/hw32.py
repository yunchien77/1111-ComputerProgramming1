#hw32
def input_str():
    n = int(input())
    list = ['' for i in range(n)]
    for i in range(n):
        string = input()
        list[i] = string
    return list

def left_push(stack, char, top):
    stack[top+1] = char
    return (top+1)   #遇到左括號則top+=1

def right_pop(top):
    return (top-1)   #遇到右括號則top-=1

def isMatch(x, y, left, right):
    if left.index(x) == right.index(y):   #假如x, y兩個字元在left list和right list的索引值相同，代表其為一對
        return True
    return False

def judge(string):
    left = ['{', '[', '(', '<', '⊂', '【']   #左括號
    right = ['}', ']', ')', '>', '⊃', '】']  #右括號
    top = -1
    stack = ['' for i in range(len(string))]  #創建一個空list來存放char
    for i in string:
        if i in left:  #若字元屬於左括號
            top = left_push(stack, i, top)  #將元素存入stack，top += 1將字元存入stack，top += 1
        elif i in right:   #若字元屬於右括號
            if top == -1:  #代表沒有出現左括號，就出現右括號(配對不成功)
                return 'Fail'
            if isMatch(stack[top], i, left, right) == False:  #此右括號與前一個出現的左括號不疋配(邏輯錯誤)
                return 'Fail'
            top = right_pop(top)
            
    if top == -1:  #所有括號都匹配成功，回到最初預設值-1
        return 'Pass'
    else:
        return 'Fail'

def count(string):
    operatorList = ['+', '-', '*', '/']
    addition, subtraction, multiplication, division = 0, 0, 0, 0
    for i in string:
        if i in operatorList:
            x = operatorList.index(i)
            if x == 0:
                addition += 1
                continue
            elif x == 1:
                subtraction += 1
            elif x == 2:
                multiplication += 1
            elif x == 3:
                division += 1
    return addition, subtraction, multiplication, division
    
def main():
    str_list = input_str()
    for i in range(len(str_list)):
        print(judge(str_list[i]))
        if judge(str_list[i]) == 'Pass':
            addition, subtraction, multiplication, division = count(str_list[i])
            print(addition, subtraction, multiplication, division)
    
main()