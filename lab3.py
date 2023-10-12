import random
from math import sin,log,e

def mu(x):
	if int(x,2) == 0:
		return 0.0
	return round(5 * sin(int(x, 2)) + log(int(x, 2), e), 2)
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

MVHSH("1010010",10)