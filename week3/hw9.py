def getDiscount(quantity, discounts):
    dis = 0
    if quantity >= 21:      #21顆(含)以上
        dis = discounts[0]
    elif quantity >= 16:    #16~20顆
        dis = discounts[1]
    elif quantity >= 11:    #11~15顆
        dis = discounts[2]
    elif quantity >= 1:     #1~10顆
        dis = discounts[3]
    else:                   #不到一顆
        dis = discounts[4]
    return dis

#輸入購買數量
x = int(input())
y = int(input())
z = int(input())
#建立各種類的折價方案list
x_discounts = [0.8, 0.9, 0.95, 1, 0]
y_discounts = [0.75, 0.85, 0.9, 1, 0]
z_discounts = [0.8, 0.8, 0.85, 1, 0]
price = [30, 70, 40]
#呼叫function，回傳對應的折價方案
x_dis = getDiscount(x, x_discounts)  
y_dis = getDiscount(y, y_discounts)
z_dis = getDiscount(z, z_discounts)
#輸出總金額
cost = (x * price[0] * x_dis) + (y * price[1] * y_dis) + (z * price[2] * z_dis)
if (x + y + z) >= 30:
    cost = cost * 0.87
print(int(cost))