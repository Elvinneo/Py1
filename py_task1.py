
#------------------------TASK1----------------------------------
"""
list1=[]
for i in range(1,6):
    list1.append(input("{}-ci ededi daxil edin : ".format(i)))
list1.sort()    
print(list1)
"""
#---------------------TASK2----------------------------------
"""
list = input("Cümleni daxil edin : ").split()
soz=''
for i in list:
    list2=sorted(i)
    for j in list2:
        soz+=j
    soz+=" "
print (soz)
"""
#------------------------TASK3----------------------------------
"""
say=1
while True:
    eded=int(input('Eded daxil edin : '))
    if eded==20:
        print("Tebrikler {} cehdde tapdiz".format(say))
        break
    say+=1
"""
#------------------------TASK4----------------------------------
'''
sadeler = []
def sade(eded):
    for j in range(2, eded):
        if eded % j == 0:
            return False
    return True
for i in range(2, 100):
    if sade(i):
        sadeler.append(i)
print(sadeler)
'''
   
#------------------------THE END----------------------------------














