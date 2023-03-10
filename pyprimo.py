from time import time

def isPrimo(num):
    limit = int((num**(1/2))+2)
    if num % 2 == 0: return False
    for c in range(3, limit, 2):
        if num % c == 0: return False
    if not num < 2: return True

def find_primos(first_num, last_num):
    return [
        nowNumber for nowNumber in range(first_num, last_num+1) if isPrimo(nowNumber)
        ]

if __name__ == '__main__':
    first_num = 0 #Número inicial
    last_num = 500000 #Número final

    print('\nIniciado')
    timenow = time()

    primos = find_primos(first_num, last_num)
    
    print(primos)

    print('Finalizado,', len(primos), 'números encontrados.')
    print(f'Tempo (s): {round((time()-timenow), 4)}\n')
