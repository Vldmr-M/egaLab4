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

def toBin(len,number)->str:
    mystr=''
    for i in range(len):
        if(number):
            mystr=str(number%2)+mystr
            number=number//2
        else:
            mystr='0'+mystr
    return mystr


def MonteKarlo(S="",N=0):
    print("!!!!!!!   Метод Монте - Карло !!!!!!!!")
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

MonteKarlo('1',10)