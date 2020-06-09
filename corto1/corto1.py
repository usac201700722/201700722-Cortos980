#Mi carnet es 201700722
Numero=5
Lista=[]
bandera=True
cont=0

for i in range(2,Numero):
    print(i)
    cont=i
    while cont != 1:
        modulo=cont%2
        if modulo==0:
            Lista.append(cont)
            cont=cont/2
        else:
            Lista.append(cont)
            cont =(3*cont)+1
        if cont == 1:
            Lista.append(1)
    print(Lista)


