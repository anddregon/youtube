def main():
    
    #* range(start<Optional>, stop<Required>, step<Optional>)


    print('Números del 0 al 100 divisibles entre 6: ')
    for i in range (101):
        if i % 6 == 0:
            print(i)

    print('Números del 1 al 100 con incremento de 2: ')
    for i in range (1,101,2):
        print(i)



if __name__ == '__main__':
    main()