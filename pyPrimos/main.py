from time import time

def isPrimo(num):
    bits = int(len(str(num))) *8
    for c in range(2, int(num/bits)):
        if num % c == 0:
            return False
    if not num < 2: return True


if __name__ == '__main__':

    fistNum = 0 #Número inicial
    lastNum = 100000 #Número final
    print('\nIniciado')
    timenow = time()

    listPrimos = []
    for nowNumber in range(fistNum, lastNum+1):
        if isPrimo(nowNumber): 
            listPrimos.append(nowNumber)

    print('Finalizado,', len(listPrimos), f'números encontrados.')
    print(f'Tempo (s): {str(round((time()-timenow), 4))}\n')
