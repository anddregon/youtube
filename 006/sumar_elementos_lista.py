import sys

def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num #suma = suma + num
    return suma

def main():

    num_str = input("Digite lista de números separados por comas: ")

    try:

    #nueva_lista = [expresion for elemento in lista_original]
        num_list = [int(num) for num in num_str.split(',')]

    except ValueError:
        print("Error: Los elementos de la lista deben ser números entereos separados por comas: ")
        sys.exit()

    suma = suma_lista(num_list)

    print(f"La suma de los elementos de la lista de: {suma}")
        

if __name__ == '__main__':
    main()