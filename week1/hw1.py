name = input('輸入學生名字:')
stu_id = int(input('輸入學生學號:'))
ch_score = int(input('輸入學生國文成績:'))
cs_score = int(input('輸入學生計算機概論成績:'))
pd_score = int(input('輸入學生計算機程式設計成績:'))
total = ch_score + cs_score + pd_score
print("Name:%s" %name)
print("\nID:%s" %stu_id)
print("\nAverage:%d" %(int(total / 3)))
print("\nTotal:%d" %total)