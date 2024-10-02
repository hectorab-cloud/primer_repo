#Título del programa
print('->Pizzería LHdP<-\n¡Bienvenido!\n')

contador_pedidos =1
def nuevo_pedido():
    global contador_pedidos 
    contador_pedidos+= 1
  
#Ingredientes
margarita=7.15
jamón=9.50
quesos=8.50

#Extra
extra_queso=1.20
champinones=0.85
albahaca=0.50

#declaración de variables del programa 
while True:
    try:
        dinero=float(input('Hola, indique con cuánto dinero dispone:\n'))
        DINERO_INICIAL=dinero
        if DINERO_INICIAL>=margarita:
            confirmar= input(f'su saldo es de {DINERO_INICIAL}.¿Es correcto? (S/N): \n').strip().upper()
            if confirmar=='S':
                print(f'opción confirmada')
                break
            elif confirmar=='N':
                print('corregir el monto')
            else:
                print('opción inválida, intente nuevamente con S/N')
        else:
            print('Cantidad no válida, por favor, inserte otro valor\n')
    except ValueError:
        print('Favor de ingresar un número')
total=0
pedido=[]


#Bucle True para pizzas
while True:
    #Menú de pizzas
    print('Elija una opción de pizza refiriendo al número')
    print(f'1- Margarita- ${margarita}')
    print(f'2- Jamón- ${jamón}')
    print(f'3- Quesos- ${quesos}')
#Almacen de la opción del usuario
    eleccion =int(input('Inserte número:\n'))
    
#Cálculo del cambio y el total a pagar, se indica la pizza a elegir
    match eleccion:
        case 1:
            print(f'Ha elegido la pizza Margarita,\nTotal a pagar ${margarita}')
            dinero -= margarita
            print(f'Restan ${round(dinero, 2)}\n')
            total += margarita
            pedido.append(f'Margarita -${margarita}') 
            break
        case 2:
            print(f'Ha elegido la pizza de Jamón,\nTotal a pagar ${jamón}')
            dinero -= jamón
            print(f'Restan ${round(dinero, 2)}\n')
            total += jamón
            pedido.append(f'Jamón -${jamón}') 
            break
        case 3:
            print(f'Ha elegido la pizza de Quesos,\nTotal a pagar ${quesos}')
            dinero -= quesos
            print(f'Restan ${round(dinero, 2)}\n')
            total += quesos
            pedido.append(f'Quesos -${quesos}')
            break
        case _:
            print('la opción elegida es incorrecta, seleccione una opción válida (1-3).')

#Bucle while para los ingredientes
while True:
    #menú de ingredientes extra
    print('¿Desea añadir ingredientes extra a la pizza?')
    print(f'Escriba 1 para Extra de queso {extra_queso}')
    print(f'Escriba 2 para Champiñones {champinones}')
    print(f'Escriba 3 para Albahaca {albahaca}')
    print(f'Escriba 4 continuar con el pago')
    eleccion=int(input('Elija entre 1-4\n'))    
    
    match eleccion:
        case 1:
            dinero -= extra_queso
            total += extra_queso
            if total<= DINERO_INICIAL:
                print(f'Ha elegido Extra de queso. \nCosto adicional ${extra_queso}')
                print(f'Total a pagar:${round(total,2)}')
                print(f'Cambio:${round(dinero,2)}')
                pedido.append(f'Extra de queso -${extra_queso}')
            else:
                print('Ha excedido su presupuesto, intente de nuevo')
        case 2:
            dinero -= champinones
            total += champinones
            if total<=DINERO_INICIAL:            
                print(f'Ha elegido Champiñones. \nCosto adicional ${champinones}')
                print(f'Total a pagar:${round(total,2)}')
                print(f'Cambio:${round(dinero,2)}')
                pedido.append(f'Champiñones -${champinones}')
            else:
                print('Ha excedido su presupuesto, intente de nuevo')
        case 3:
            dinero -= albahaca
            total += albahaca
            if  total<=DINERO_INICIAL:            
                print(f'Ha elegido Albahaca \nCosto adicional ${albahaca}')
                print(f'Total a pagar:${round(total,2)}')
                print(f'Cambio:${round(dinero,2)}')
                pedido.append(f'Albahaca -${albahaca}')
            else:
                print('Ha excedido su presupuesto, intente de nuevo')
        case 4:
            print('No se añadirá ningún extra a la orden')
            break
        case _:
            print('valor inválido, escriba un valor entre 1 a 4')
#Condicional para determinar si alcanza el presupuesto inicial 
#Si alcanza, se ejecuta el if y saca ek ticket de compra
if total <= DINERO_INICIAL:
    print(f'\n--PEDIDO No. {contador_pedidos}')
    for i in pedido:
        print(f'-Pizza {i}')
        break
    for i in pedido[1:]:
        print(f'-{i}')
    print(f'\nEl total de su pedido es:${round(total,2)}')
    print(f'Su cambio son: ${round(dinero,2)}')        
    print('\n¡¡Buen provecho\nGracias por su compra!!')
else:
    print('Saldo insuficiente, Favor de corregir la compra')
    
    
        