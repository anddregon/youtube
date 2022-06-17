def main():
    
    a = 5
    b = 2
    c = a + b

    print('Dirección en memoria de la variable a: ')
    print (id(a))

    print('Dirección en memoria de la variable b: ')
    print (id(b))

    print('Dirección en memoria de la variable c: ')
    print (id(c))

if __name__ == '__main__':
    main()