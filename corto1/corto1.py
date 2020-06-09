def par(N):
    cont=N
    modulo=N%2
    if(modulo==0):      ##Es par
        cont=cont/2
    else:
        cont=3*cont+1

    return cont

#Mi carnet es 201700722
Numero=5
Lista=[]
bandera=True
cont=0

for i in range(2,Numero):
    print(par(i))


