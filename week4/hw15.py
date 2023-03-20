"""
請設計計算BMI的程式，判斷A, B 兩個人，誰的BMI比較大

BMI值計算公式: BMI = 體重(公斤) / 身高^2(公尺^2)，例如：一個52公斤的人，身高是155公分，則BMI為 : 52(公斤)/1.55^2 ( 公尺^2 )= 21.6。
正常範圍BMI 為 18.5～24 (含18.5與24)。
當BMI太大，輸出 Hi {name}, Your BMI: {xxx} too HIGH.
當BMI太小，輸出 Hi {name}, Your BMI: {xxx} too LOW.
在正常範圍，輸出 Hi {name}, Your BMI: {xxx}.

若A比B重，輸出 {A}’s BMI is larger than {B}.
若B比A重，輸出 {B}’s BMI is larger than {A}.
★ 不會有雙方BMI相同的狀況

BMI輸出，四捨五入到小數點後第二位 (可用%.2f)。

---------------------------------------------------

輸入說明 :
第一行，輸入一字串，代表A的名字
第二行，輸入浮點數 w，代表A的體重
第三行，輸入浮點數 h，代表A的身高 (單位為公尺)
第四行，輸入一字串，代表B的名字
第五行，輸入浮點數 w，代表B的體重
第六行，輸入浮點數 h，代表B的身高 (單位為公尺)

輸出說明 :
第一行，依據A的BMI，輸出A的BMI屬於過重、過輕，還是正常
第二行，依據B的BMI，輸出B的BMI屬於過重、過輕，還是正常
第三行，輸出A跟B誰的BMI比較大
輸出格式請參考題目
"""

def judge_BMI(name, BMI):
    if BMI > 24:
        print('Hi %s, Your BMI: %.2f too HIGH.' %(name, BMI))
    elif BMI < 18.5:
        print('Hi %s, Your BMI: %.2f too LOW.' %(name, BMI))
    else:
        print('Hi %s, Your BMI: %.2f.' %(name, BMI))
        
def compare(A_BMI, B_BMI, A_name, B_name):
    if A_BMI > B_BMI:
        print('{A}\'s BMI is larger than {B}.'.format(A = A_name, B = B_name))
    elif A_BMI < B_BMI:
        print('{B}\'s BMI is larger than {A}.'.format(A = A_name, B = B_name))

A_name = input()
A_weight = float(input())
A_height = float(input())
B_name = input()
B_weight = float(input())
B_height = float(input())
A_BMI = A_weight / A_height ** 2
B_BMI = B_weight / B_height ** 2
judge_BMI(A_name, A_BMI)
judge_BMI(B_name, B_BMI)
compare(A_BMI, B_BMI, A_name, B_name)
