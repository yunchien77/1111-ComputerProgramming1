#hw31
import math

def input_data():
    people = int(input())
    infectPeople = int(input())
    recoveryDay = int(input())
    protectedRate = float(input())
    periodWeek = int(input())
    return people, infectPeople, recoveryDay, protectedRate, periodWeek

#每周平均確診人數及新增確診人數
def total_infected(people, infectPeople, recoveryDay, protectedRate, periodWeek):
    infect = [0 for i in range(7*periodWeek)] #總確診
    addInfect = [0 for i in range(7*periodWeek)] #新增確診
    recovery = [0 for i in range(7*periodWeek)] #康復人數
    day = 0
    infect[day] = people     # infect[0] = people
    addInfect[day] = people  # addInfect[0] = people
    recovery[day] = 0        #recovery[0] = 0
    day += 1 #計日器
    while (people > 0) and (day < 7*periodWeek):
        addInfect[day] = int(infect[day-1]*(infectPeople/recoveryDay)*(1-protectedRate))
        recovery[day] = addInfect[day-recoveryDay]
        infect[day] = infect[day-1] + addInfect[day] - recovery[day]
        day += 1
    return infect, addInfect, recovery

#將每週數據取平均
def mean_result(infect, addInfect, recovery, periodWeek):
    #切割串列，以週為單位放入新的二維串列
    split_infect = [[]]
    split_addInfect = [[]]
    split_recovery = [[]]
    count = 0
    for i in range(1, periodWeek*7+1):
        split_infect[count].append(infect[i-1])
        split_addInfect[count].append(addInfect[i-1])
        split_recovery[count].append(recovery[i-1])
        if i % 7 == 0 and i != periodWeek*7:
            count += 1
            split_infect.append([])
            split_addInfect.append([])
            split_recovery.append([])
            continue
    #將各週數據取平均，並無條件進位
    mean_infect = []
    mean_addInfect = []
    mean_recovery = []
    for i in range(periodWeek):
        mean_infect.append(math.ceil(sum(split_infect[i])/7))
        mean_addInfect.append(math.ceil(sum(split_addInfect[i])/7))
        mean_recovery.append(math.ceil(sum(split_recovery[i])/7))
    return mean_infect, mean_addInfect, mean_recovery

def output_result(mean_infect, mean_addInfect, mean_recovery, periodWeek):
    for i in range(periodWeek):
        print("(Week %d, %d, %d, %d)" %(i+1, mean_infect[i], mean_addInfect[i], mean_recovery[i]))
    index = mean_addInfect.index(0) + 1
    print(index)
        
def main():
    people, infectPeople, recoveryDay, protectedRate, periodWeek = input_data()
    infect, addInfect, recovery = total_infected(people, infectPeople, recoveryDay, protectedRate, periodWeek)
    mean_infect, mean_addInfect, mean_recovery = mean_result(infect, addInfect, recovery, periodWeek)
    output_result(mean_infect, mean_addInfect, mean_recovery, periodWeek)
    
main()