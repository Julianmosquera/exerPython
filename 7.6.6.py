__author__='Julián Mosquera'

def listas(lista,k):
    maiores=[]
    menores=[]
    iguais=[]

    for n in lista:
        if n>k:
            maiores.append(n)
        elif n<k:
            menores.append(n)
        else:
            iguais.append(n)

    return [maiores,menores,iguais]

lista=[1,2,3,4,5,6,7,8,9,10]
resultado=listas(lista,7)
print(resultado)