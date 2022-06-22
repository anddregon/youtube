#* Teorema de Wilson
#* Si p es primo:
#* (p-1)! = p° - 1 

def factorial(n):
    fact = 1
    if n < 0:
        return 0
    elif n == 0: 
        return 1
    while (n > 1):
        fact *= n #* fact = fact * n
        n -= 1 #* n = n - 1
    return fact

def main():
    
    numero = int(input('Digite un número: '))
    wilson = factorial(numero - 1) + 1
    if wilson % numero == 0:
        print('El número es primo')
    else: 
        print('El número no es primo')

if __name__ == '__main__':
    main()