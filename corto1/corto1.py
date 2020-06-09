import time #Para generar pausa
import datetime #Para generar fecha/hora actual
#Mi carnet es 201700722
Numero=722
Lista=[]
bandera=True
cont=0
archivo = open('collatz.txt', 'a')          #Creo el archivo con el nombre collatz.txt en modo append
for i in range(2,Numero):                   #For de 2 hasta 722
    print(i)
    cont=i
    while cont != 1:                        #Se ejecuta mientras el contador sea diferente de 0
        modulo=cont%2                       #Determina el modulo para saber si es par
        if modulo==0:                       #Si es par cont = cont/2
            Lista.append(cont)              #Escribe al final del archivo
            cont=cont/2
        else:                               #Si es impar cont = (3*cont)+1
            Lista.append(cont)
            cont =(3*cont)+1                #Escribe al final del archivo
        if cont == 1:
            Lista.append(1)
        #archivo.write(Lista)                    #Escribe la lista en en el archivo
        print(Lista)
    archivo.write(str(Lista))
archivo.close()


