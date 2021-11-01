#!/bin/python3
#Para fins de aprendizado esse codigo foi adaptado de PythonCafe   

def partition(lista,inicio,fim):
    pivot = lista[fim]
    i     = inicio
    for j in range(inicio,fim):
        if lista[j] < pivot:
            lista[j],lista[i] = lista[i], lista[j]
            i = i+1
    
    lista[i],lista[fim] = lista[fim],lista[i]

    return i


def quicksort(lista,inicio=0,fim=None):

    if fim is None:
        fim = len(lista)-1 

    if inicio < fim:
        p = partition(lista,inicio,fim)
        quicksort(lista,inicio,p-1)
        quicksort(lista,p+1,fim)

a= [17,99,0,8,665,4]

quicksort(a)
print(a)