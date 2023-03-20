#hw34

def input_data():
    data_list = []
    while(1):
        M = input()
        if M == '-1':
            break
        data_list.append(bin_to_dec(M))
    return data_list

#二進未轉十進位    
def bin_to_dec(num):
    j, sum = 0, 0
    for i in range(len(num)-1, -1, -1):
        sum += (int(num[i]) * (2**j))
        j += 1
    return sum

#電路模擬
def c(m, process_data):
    process_data.append(m)
    #base/stop solution
    if m == 0 or m == 1:
        return process_data
    #general solution
    elif m % 2 == 0:  #偶數
        return c(m//2, process_data)
    elif m % 2 != 0:  #奇數
        return c((m+1)//2, process_data)
    
#十進位轉二進位
def dec_to_bin(num):
    bin_num = bin(num).replace('0b', '')
    z = bin_num.zfill(4)
    return z
        
    
def main():
    data_list = input_data()
    multidata = []
    for i in data_list:
        process_data = []
        process_data = c(i, process_data)
        process_data.pop(0)
        multidata.append(process_data)
    for i in range(len(multidata)):
        print(dec_to_bin(len(multidata[i])))   #*操作符可以用來解包物件。它將一個列表中的所有元素解包並列印出來，不含中括號
        if(dec_to_bin(len(multidata[i])) == '0000'):
            print('No Feedback')
        else:
            print(*multidata[i])
        
main()
