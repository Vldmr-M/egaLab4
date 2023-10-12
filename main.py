import random
from math import sin,log,e

def mu(x):
	if int(x,2) == 0:
		return 0.0
	return round(5 * sin(int(x, 2)) + log(int(x, 2), e), 2)

def toBin(len,number)->str:
    mystr=''
    for i in range(len):
        if(number):
            mystr=str(number%2)+mystr
            number=number//2
        else:
            mystr='0'+mystr
    return mystr


def randstr(len)->str:
    mystr = ''
    for i in range(len):
        mystr = mystr+(str(random.randint(0,1000)%2))
    return mystr

def createArea(stroka):
    area=[]
    area.clear()
    for i in range(len(stroka)):
        tempstr = ''
        if(stroka[i]=='1'):
            tempstr=stroka[:i]+'0'+stroka[i+1:]
        else:
            tempstr=stroka[:i]+'1'+stroka[i+1:]
        area.append(tempstr)
    return area

def MonteKarlo(S="",N=0):
    print("!!!!!!!!! Метод Монте - Карло !!!!!!!!!!")
    MaxS=S
    MaxMu=mu(S)
    lenS=len(S)

    for i in range(N):
        print(f"////////////////////\nШаг {i+1}")
        print(f"MaxS - {MaxS}    MaxMu - {MaxMu}")
        tempS=randstr(lenS)
        tempMu=mu(tempS)
        print(f"выбранная кодировка - {tempS}   ее приспособленность - {tempMu}")

        if tempMu>MaxMu:
            print(f"Смена MaxS на {tempS} ,  смена MaxMu на {tempMu}")
            MaxS=tempS
            MaxMu=tempMu
    print(f"Итог:\nMaxS - {MaxS}   maxMu - {MaxMu}")
    return MaxS, MaxMu



def MVHG(S="",N=0):
    print("!!!!!!!!!! Метод восхождения на холм в глубину !!!!!!!!!!!")
    MaxS=S
    MaxMu=mu(MaxS)
    lenS=len(S)
    area=createArea(MaxS)
    for i in range(N):
        print(f"////////////////////\nШаг {i + 1}")
        print(f"MaxS - {MaxS}    MaxMu - {MaxMu}")
        if len(area)>0:
            print("Окрестность:")
            for j in area:
                print(j," - ",mu(j))
            tempS=random.choice(area)
            tempMu=mu(tempS)
            area.remove(tempS)
            print(f"Выбрана кодировка - {tempS}  ее приспособленностьт - {tempMu}")
        else:
            print("Кодировки исчерпаны, достигнут локальный оптимум")
            break

        if tempMu>MaxMu:
            print(f"Смена MaxS на {tempS} ,  смена MaxMu на {tempMu}")
            MaxMu=tempMu
            MaxS=tempS
            area=createArea(MaxS)
    print(f"Итог:\nMaxS - {MaxS}   maxMu - {MaxMu}")
    return MaxS, MaxMu


def MVHSH(S="",N=0):
    print("!!!!!!!!!!! Метод восхождения на холм в ширину !!!!!!!!!!!!")
    MaxS=S
    MaxMu=mu(MaxS)
    lenS=len(S)
    area=createArea(MaxS)
    for i in range(N):
        print(f"////////////////////\nШаг {i + 1}")
        print(f"MaxS - {MaxS}    MaxMu - {MaxMu}")
        tempS=""
        tempMu=0
        print("Окрестность:")
        for j in area:
            print(j, " - ", mu(j))
            if mu(j)>tempMu:
                tempS=j
                tempMu=mu(tempS)

        print(f"Выбрана кодировка - {tempS}  ее приспособленностьт - {tempMu}")

        if tempMu>MaxMu:
            print(f"Смена MaxS на {tempS} ,  смена MaxMu на {tempMu}")
            MaxMu=tempMu
            MaxS=tempS
            area=createArea(MaxS)
        else:
            print("Достигнут локальный оптимум")
            break
    print(f"Итог:\nMaxS - {MaxS}   maxMu - {MaxMu}")
    return MaxS,MaxMu

L=7
MaxS=randstr(L)
MaxMu=0
M = int(input("Введите M: "))
N = int(input("Введите N: "))

print("Ландшафт:")
for k in range(32):
    print(toBin(L,k)," - ",mu(toBin(L,k)))

for i in range(0, M):
	k = random.randint(0, 2)
	if k == 0:
		print("Выбран метод Монте-Карло")
		MaxS, MaxMu = MonteKarlo(MaxS,N)
		print()
	elif k == 1:
		print("Выбран МВХ в глубину")
		MaxS, MaxMu = MVHG(MaxS,N)
		print()
	else:
		print("Выбран МВХ в ширину")
		MaxS, MaxMu = MVHSH(MaxS,N)
		print()
print("Финальный итог: " , MaxS , " " ,MaxMu)