def encontrar_maximo_minimo(lista):
    
    maximo = lista[0]
    minimo = lista[0]

    for i in range(len(lista)):

        if lista[i] > maximo:
            maximo = lista[i]
        
        elif lista[i] < minimo:
            minimo = lista[i]

    return maximo, minimo


def main():

    lista = [1,4,5,6,7,4,5,6,7,3,2,10]

    maximo, minimo = encontrar_maximo_minimo(lista)

    print(f'El valor máximo de la lista es: {maximo}')
    print(f'El valor minimo de la lista es: {minimo}')
if __name__ == '__main__':
    main()

    