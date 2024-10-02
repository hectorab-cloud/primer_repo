lista_de_num= [10,45,365,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_de_num=list(set(lista_de_num))
lista_de_num.sort()

for num in lista_de_num:
    if num==10:
        continue
    elif num==366:
        break
    else:
        print(f'El valor del elemento es: {num}.')

n_l=len(lista_de_num)
print(n_l-1)
