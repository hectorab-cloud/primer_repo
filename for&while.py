#for i in range(10,60,5):
    #if i %2!=0 or i<20:
        #continue
    #print(i)

#for <variable> in <iterable>:
#    <Código>

for pollo in range(10,50,5):
    if pollo ==20:
        continue
    if pollo >=40:
        break
    print('el pollo cuesta $', pollo)
print('\n','\n')

pollo= 5

while pollo <= 20:
    print ('el precio del pollo es de $', pollo)
    pollo +=.5
