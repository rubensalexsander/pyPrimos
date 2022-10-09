from time import time

def isPrimo(num):
    bits = len(str(num))*8
    for c in range(2, int(num/bits)):
        if num % c == 0:
            return False
    if not num < 2: return True

def find_primos(first_num, last_num):
    return [
        nowNumber for nowNumber in range(first_num, last_num+1) if isPrimo(nowNumber)
        ]

if __name__ == '__main__':
    first_num = 0 #Número inicial
    last_num = 200000 #Número final

    print('\nIniciado')
    timenow = time()

    primos = find_primos(first_num, last_num)

    print('Finalizado,', len(primos), 'números encontrados.')
    print(f'Tempo (s): {round((time()-timenow), 4)}\n')
