import random
def criterion(str)->float:
    return pow(int(str,2)-pow(2,LenOfS-1),2)

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
    area.clear()
    for i in range(len(stroka)):
        tempstr = ''
        if(stroka[i]=='1'):
            tempstr=stroka[:i]+'0'+stroka[i+1:]
        else:
            tempstr=stroka[:i]+'1'+stroka[i+1:]
        area.append(tempstr)



LenOfS=int(input('введите длину строки'))
n=int(input('введите кол-во итераций'))
area=[]
massCrit = {}
maxCrit=0
maxS=randstr(LenOfS)

createArea(maxS)

for i in range(2**LenOfS):
    massCrit[toBin(LenOfS,i)]=random.randint(0,100)

for i in range(32):
    print(toBin(LenOfS,i)," - ",massCrit[toBin(LenOfS,i)])

for i in range(n):

    print(f'/////////////////////\nSTEP {i+1}\ncurrS - {maxS}    '
          f' currMax - {massCrit[maxS]}')
    if(len(area)>0):
        index=random.randint(0,100)%len(area)
        tempS=area[index]
        area.pop(index)

    print(f'tempS - {tempS}    tempMax - {massCrit[tempS]}')

    if massCrit[tempS] > massCrit[maxS] :
        print('Maximum has changed\n')
        maxS=tempS
        maxCrit=massCrit[tempS]
        createArea(maxS)

print(maxS,maxCrit)