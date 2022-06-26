import random

def main():

    lista = []

    for indice in range (1,21):
        lista.append(random.randint(1,10))
    
    #Lista desordenada
    print(lista)
    
    #Ordenarmos la lista
    lista.sort()

    #Recorremos la lista ordenada
    print(lista)

if __name__ == '__main__':
    main()
