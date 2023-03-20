#hw35

#輸入data
def input_data():
    id = input()
    weight = int(input())
    num_list = list(map(int, [i for i in id[::3]]))
    letter_list = [i for i in id[1::3]]
    if duplicated(id) == 1:
        print('Duplicated ID')
        return 0, 0, 0
    return num_list, letter_list, weight
    

#judge whether duplicated elements in the id(ex:3W, 3W)
def duplicated(id):
    set_list = set(id.split(' '))
    if len(set_list)  == len(id.split(' ')):
        return 0 #無重複元素
    return 1  #有重複元素

#取出配對成功的元素後，清除原本資烙中的相同元素
def remove(data_list, bag, letter_list):
    if bag in data_list:
       letter_list.remove(letter_list[data_list.index(bag)])
       data_list.remove(bag)


def findBag(data_list, index, weight, bag):
    if index >= len(data_list):  #超出資料列表長度則停止
        return False
    elif data_list[index] == weight:  #單一元素剛好等於所要之值
        bag.append(data_list[index])
        return True
    elif findBag(data_list, index+1, weight - data_list[index], bag) == True:  #要減
        bag.append(data_list[index])
        return True
    elif findBag(data_list, index+1, weight, bag) == True:  #不要減
        return True
 
def compute(data_list, weight, letter_list):
    resultofLetter = []
    if weight < 1 or weight > 10:  #限重1~10
        print('Input Error')
        return 0
    for k in data_list:   
        if k > weight:  #單一貨物重不可大於限重
            print('Load limit exceeded')
            return 0
    for i in range(sum(data_list) // weight):
        bag = []
        let = []
        if findBag(data_list, 0, weight, bag) == False:
            # print('Cannot be delivered')
            return 0
        # print('bag=', bag, end=',')
        for j in range(len(bag)):
            a = data_list.index(bag[j])
            let.append(letter_list[a])
            remove(data_list, bag[j], letter_list)  #移除已配對(bag中有的)的元素
        resultofLetter.append(let)
        # print(resultofLetter)
    if data_list != []:
        print('Cannot be delivered')
        return 0
    return output(length_arrangement(resultofLetter))

#重新排列印出的結果(sort())
def findindex_letter(resultofLetter):
    #ex: [['r'], ['d', 'a'], ['f', 'c'], ['g', 'q']]
    #先排1d array  --> [['r'], ['a', 'd'], ['c', 'f'], ['g', 'q']]
    for i in range(len(resultofLetter)):
        resultofLetter[i].sort()
    #後排2d array  --> [['a', 'd'], ['c', 'f'], ['g', 'q'], ['r']]
    resultofLetter.sort()
    return resultofLetter

#將2d list依據各元素長度進行排序(短->長)
def length_arrangement(list):
    list = findindex_letter(list)
    new_list = sorted(list, key=lambda x:len(x), reverse = False)
    return new_list
        
    
#輸出結果
def output(list):
    print(len(list))
    for i in range(len(list)):
        print(' '.join(list[i]))
      
def main():
    num, letter, weight = input_data()
    if num != 0:   #id中無重複編號才會繼續執行
        compute(num, weight, letter)
    
main()