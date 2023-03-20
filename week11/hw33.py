#hw33
from fractions import Fraction

def input_data():
    num1_list, num2_list, oper_list = [], [], []
    while(1):
        num1 = input()
        num2 = input()
        operator = input()
        judge = input()
        num1 = split_str(num1)
        num2 = split_str(num2)
        num1_list.append(num1)
        num2_list.append(num2)
        oper_list.append(operator)
        if judge == 'n':
            break
    return num1_list, num2_list, oper_list

def split_str(num):
    #帶分數 Ex: 2(3/4) --> ['2', ['3', '4']] --> [11, 4]
    if '(' in num: 
        num = num.split('(')
        num[1] = num[1].split('/')
        a = num[1][1].split(')')
        num[1][1] = a[0]
        if int(num[0]) < 0:
            num[0] = -(abs(int(num[0])) * int(num[1][1]) + int(num[1][0]))
        else:
            num[0] = int(num[0]) * int(num[1][1]) + int(num[1][0])
        num[1] = int(num[1][1])
    #假分數  Ex: 1/2 --> ['1', '2'] --> [1, 2]
    else:
        num = num.split('/')
        num = list(map(int, num))
    return num  #回傳為list， list[0]為分子，list[1]為分母

def calculate(num1, num2, operator):
    if operator == '+':
        result = Fraction(num1[0], num1[1]) + Fraction(num2[0], num2[1])
    elif operator == '-':
        result = Fraction(num1[0], num1[1]) - Fraction(num2[0], num2[1])
    elif operator == '*':
        result = Fraction(num1[0], num1[1]) * Fraction(num2[0], num2[1])
    elif operator == '/':
        result = Fraction(num1[0], num1[1]) / Fraction(num2[0], num2[1])
    return str(result)

def main():
    num1, num2, operator = input_data()
    for i in range(len(operator)):
        if num1[i][1] != 0 and num2[i][1] != 0:
            result = calculate(num1[i], num2[i], operator[i])
            if '/' not in result:
                print(result)
            else:
                x = result.split('/')
                x = list(map(int, x))
                if abs(x[0]) > x[1]:
                    fr = int(x[0] / x[1])  #最前面帶分數的部分
                    mo = abs(x[0]) % abs(x[1])  #分子，x[1]是分母
                    print("%d(%d/%d)" %(fr, mo, x[1]))
                else:
                    print(result)
        else:   #分母為零不可運算
            print('ERROR')
    
main()