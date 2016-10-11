

def exercicio769(lista):
    empaquetado=[]
    elemento=lista[0]
    i=0
    for n in lista:
        if elemento== n:
            i=i+1
        else:
            empaquetado.append((elemento,i))
            elemento=n
            i=1
    empaquetado.append((elemento,i))
    return empaquetado




l=[1,2,3,4,5,6,7,8,9,10]
print(exercicio769(l))