'''給一個正整數 (2 <= N <= 10000)，請找出2~N之間所有質數的總和'''
#質數(Prime)是一個大於1，且無法找到除了自己本身和1之外的自然數能整除它的自然數

N = int(input())
sum = 0

def is_prime(number):
    for i in range(2, number):
        if number % i == 0: #i為number的因數，故number不是質數
            return False
    return True  #沒有i能整除number，故number為質數

for i in range(2, N+1):
    if is_prime(i):
        sum += i
    else:
        continue
    
print(sum)