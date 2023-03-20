def cal_sum(m, n, a):
    sum = 0
    count = 0
    for i in range(m, n+1, a):
        sum += (m + a * count)
        count += 1
    return sum
    
def cal_product(m, n, b):
    product = 1
    count = 0
    for i in range(m, n+1, b):
        product *= (m + b * count)
        count += 1
    return product
    
m = int(input())
n = int(input())
a = int(input())
b = int(input())
print(cal_sum(m, n, a))
print(cal_product(m, n, b))