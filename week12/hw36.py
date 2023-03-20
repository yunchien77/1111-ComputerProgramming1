#hw36

def input_data():
    data_list = []
    while(1):
        M = input()
        if M == '-1':
            break
        data_list.append(bin_to_dec(M))
    return data_list

#二進位轉十進位    
def bin_to_dec(num):
    j, sum = 0, 0
    for i in range(len(num)-1, -1, -1):
        sum += (int(num[i]) * (2**j))
        j += 1
    return sum

#電路模擬
def c(m, count):
    #base/stop solution
    if m == 0 or m == 1:
        return count
    #general solution
    elif m % 2 == 0:  #偶數
        return c(m//2, count+1)
    elif m % 2 != 0:  #奇數
        return c((m+1)//2, count+1)
    
#十進位轉二進位
def dec_to_bin(num):
    bin_num = bin(num).replace('0b', '')
    z = bin_num.zfill(12)
    return z
        
    
def main():
    data_list = input_data()
    for i in data_list:
        list = []
        for j in range(i+1):
            count = 0
            count = c(j, count)
            list.append(count)
        print(dec_to_bin(sum(list)))
        
main()
