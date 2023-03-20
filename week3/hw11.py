def appendList(hour):
    list = []
    for i in range(hour):
        time = int(input())
        list.append(time)
    return list

course_1 = int(input()) #輸入課程編號
hour_1 = int(input()) #輸入上課小時數
list_1 = appendList(hour_1)
course_2 = int(input()) #輸入課程編號
hour_2 = int(input()) #輸入上課小時數
list_2 = appendList(hour_2)
course_3 = int(input()) #輸入課程編號
hour_3 = int(input()) #輸入上課小時數
list_3 = appendList(hour_3)
a = [x for x in list_1 if x in list_2]
b = [x for x in list_2 if x in list_3]
c = [x for x in list_1 if x in list_3]
if a != []:
    print('%d and %d conflict on %d' %(course_1, course_2, a[0]))
elif b != []:
    print('%d and %d conflict on %d' %(course_2, course_3, b[0]))
elif c != []:
    print('%d and %d conflict on %d' %(course_1, course_3, c[0]))