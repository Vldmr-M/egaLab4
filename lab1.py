import random
def criterion(str)->float:
    return pow(int(str,2)-pow(2,lenOFs-1),2)

def randstr(len)->str:
    mystr = ''
    for i in range(len):
        mystr = mystr+(str(random.randint(0,1000)%2))
    return mystr



iterOFsearch=10
lenOFs=15
s=""
max=0
maxS=""
iterOFsearch = int(input('введите кол-во итераций:\n'))
lenOFs = int(input('введите длину строки:\n'))

#вывод ландшафта
#///////////////////////////////////////////////////
def toBin(len,number)->str:
    mystr=''
    for i in range(len):
        if(number):
            mystr=str(number%2)+mystr
            number=number//2
        else:
            mystr='0'+mystr
    return mystr

print('ВЫВОД ЛАНДШАФТА')
for i in range(32):
    print(toBin(10,i),'    критерий -  ' ,criterion(toBin(10,i)))
#////////////////////////////////////////////////////

for i in range(iterOFsearch):
    s=randstr(lenOFs)
    print("============\nШАГ" + str(i+1))
    print('s = ' + s + "   или  " + str(int(s,2)),end=';  ' )
    print('критерий - ' + str(criterion(s)))

    if(criterion(s)>max):
        max = criterion(s)
        maxS = s
        print(f'maximum has changed - {max}')



    print(f'current max = {max}    current maxS = {maxS}')

print('=============\nИТОГ',end='')
print(f"\nmax={max}\nmaxS={maxS}")

