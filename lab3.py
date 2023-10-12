import random

def randstr(len)->str:
    mystr = ''
    for i in range(len):
        mystr = mystr+(str(random.randint(0,1000)%2))
    return mystr

def createArea(stroka):
    area.clear()
    for i in range(len(stroka)):
        tempstr = ''
        if(stroka[i]=='1'):
            tempstr=stroka[:i]+'0'+stroka[i+1:]
        else:
            tempstr=stroka[:i]+'1'+stroka[i+1:]
        area.append(tempstr)

def toBin(number):
    mystr=''
    for i in range(LenS):
        if(number):
            mystr=str(number%2)+mystr
            number=number//2
        else:
            mystr='0'+mystr
    return mystr

LenS=5
prostranstvo={}
for i in range(pow(2,LenS)):
    prostranstvo[toBin(i)]=random.randint(0,100)

MaxS=randstr(LenS)
MaxMu=prostranstvo[MaxS]
N=int(input("введите N"))
area=[]
createArea(MaxS)

for i in range(N):
    print("Шаг " + str(i + 1) + ":")
    print(f"maxS = {MaxS}   maxMu = {MaxMu}")
    print("area:")

    if(len(area)>0):
        tempMu = 0
        tempS=""
        for j in range(len(area)):
            if prostranstvo[area[j]] >tempMu:
                tempMu=prostranstvo[area[j]]
                tempS=area[j]

        for k in area:
            print(k, " - ", prostranstvo[k])
        print(f"выбрана кодировка - {tempS}    Mu =  {tempMu}")
    else:
        print("исчерпаны кодировки")
        break


    if tempMu > MaxMu :
        print(f"Смена maxS с {MaxS}  на {tempS}")
        print(f"Смена MaxMu c {MaxMu} на {tempMu}")
        MaxMu=tempMu
        MaxS=tempS
        createArea(MaxS)
    else:
        print("приспособленность лучшей кодировки в окрестности меньше текущей,"
              " достигнут локальный оптимум")
        break
    print("\n\n")