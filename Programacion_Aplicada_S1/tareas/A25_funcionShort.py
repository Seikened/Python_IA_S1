import random

def MaximoMinimo(lista):
    copyLista = list(lista)
    copyLista.sort()
    maximo = copyLista[-1]
    minimo = copyLista[0]
    
    return  minimo,maximo



lista = tuple(random.randint(1,100) for _ in range(20))
#lista = (1,45,21,456,6,23,56)
minimo,maximo = MaximoMinimo(lista)
print(f"El valor mínimo es:{minimo} y el máximo es: {maximo} de la lista: {lista}")