__author__='Julián Mosquera'

lista=[1,2,3,4,5,6,7,8,9,10]
def exercicio767(lista):
    cadea=[]
    for persoa in lista:
        cadea.append(persoa[2]+","+persoa[1]+","+persoa[0])

    return cadea

l=[("perez","gonzalez","F"),("manu","eva","R"),("ana","ruiz","v")]
resultado=exercicio767(l)
print(resultado)