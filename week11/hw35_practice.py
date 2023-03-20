def findBag(num_list,letter_list, index, m, bag1,bag2):
    if index>=len(num_list):
        return False
    elif num_list[index]==m:
        bag1.append(num_list[index])
        bag2.append(letter_list[index])
        num_list.pop(index)
        letter_list.pop(index)
        return True
    elif findBag(num_list,letter_list, index+1, m-num_list[index], bag1,bag2)==True:
        bag1.append(num_list[index])
        bag2.append(letter_list[index])
        num_list.pop(index)
        letter_list.pop(index)
        return True
    elif findBag(num_list,letter_list, index+1, m, bag1,bag2)==True:
        return True
    
def compute(num_list,letter_list,value):
    m = sum(num_list)//value
    bigbag=[]
    for i in range(value): #迴圈找N次
        bag1 = []
        bag2=[]      
        if findBag(num_list,letter_list, 0, m, bag1,bag2) ==False:
            return False
        bag2.sort()
        bag2=" ".join(map(str, bag2))
        bigbag.append(bag2)
        
        #print( bag2, end=', ')#letterlist
    return bigbag 
    return True
def Duplicated(good):
    for i in good:
        a=good.count(i)
        if a>1:
            return False
            break
def load(num_list,m):
    for i in num_list:
        if i>m:
            return False
        
goods="2L 2M 4C 1S 1P"
m=5#每組重量
good=goods.split(" ")#['4Q', '3A', '2D', '3C', '5R', '2F', '1G']
#good=sorted(good , key = lambda s: s[1])#照字母小到大排序
num_list=[int(i) for i in list(goods[0::3])]#[4, 3, 2, 3, 5, 2, 1]
letter_list=[letter for letter in list(goods[1::3])]#['Q', 'A', 'D', 'C', 'R', 'F', 'G']
value=sum(num_list)//m #總共幾組
while True:
    if m<1 or m>10:#輸入的載重限制超出限制範圍
        print("Input Error")
        break
    elif Duplicated(good)==False:#貨物編號重複
        print("Duplicated ID")
        break
    elif load(num_list,m)==False: #單一貨物重量超出貨車載重限制
        print("Load limit exceeded")
        break
    elif sum(num_list)%m!=0:#貨物未滿載導致無法配送
        print("Cannot be delivered")
        break
    else:
        print(value)#幾組
        bigbag=compute(num_list, letter_list,value)
        bigbag.sort()
        bigbag.sort(key=len)
        for i in bigbag:
            print(i)    
        break