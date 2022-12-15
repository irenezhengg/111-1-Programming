from math import ceil

def dailyNewInfect(_people: int) -> int:
    return int((_people * infectPeople/recoveryDay) * (1-protectedRate))

people =        int(input())
infectPeople =  int(input())
recoveryDay =   int(input())
protectedRate = float(input())
periodWeek =    int(input())

zero_COVID_flag = False
zero_COVID = 0
infect = [people]
newInfect = [people]

for week in range(periodWeek):
    days = 6 if week == 0 else 7
    
    for day in range(days):
        todayRecovery = newInfect[-recoveryDay] if len(newInfect) >= recoveryDay else 0

        dni = dailyNewInfect(infect[-1])
        newInfect.append(dni)
        infect.append(infect[-1] + dni - todayRecovery)

    avgInfect: int    = ceil(sum(infect[-7:]) / 7)
    avgNewInfect: int = ceil(sum(newInfect[-7:]) / 7)
    avgRecovery: int  = ceil(sum(newInfect[-(7+recoveryDay):-recoveryDay]) / 7) if len(newInfect) >= recoveryDay else 0

    print(f'(Week {week+1}, {avgInfect}, {avgNewInfect}, {avgRecovery})')
    
    if not (zero_COVID_flag or avgNewInfect):
        zero_COVID_flag = True
        zero_COVID = week + 1

print(zero_COVID)