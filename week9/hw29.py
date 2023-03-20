#hw 29
def main():
    m = int(input())
    if m < 1 or m > 10:
        print('ERROR')
        return 0
    odd_list = []   #奇數，放左側
    eval_list = []  #偶數，放右側
    for i in range(m):
        n = int(input())
        if n < 1 or n > 1000:
            print('ERROR')
            return 0
        elif n % 2 != 0:
            odd_list.append(n)
        else:
            eval_list.append(n)
            
    odd_list.sort()
    eval_list.sort(reverse = True)
    list = odd_list + eval_list
    for i in range(len(list)):
        print(list[i], end = ' ')
        
main()
    