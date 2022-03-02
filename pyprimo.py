from time import time

class Pyprimo:
    def __init__(self):
        pass

    def isPrimo(self, num):
        bits = int(len(str(num))) *8
        for c in range(2, int(num/bits)):
            if num % c == 0:
                return False
        if not num < 2: return True
    
    def find_primos(self, first_num, last_num):
        listPrimos = []
        for nowNumber in range(first_num, last_num+1):
            if self.isPrimo(nowNumber): 
                listPrimos.append(nowNumber)
        return listPrimos

if __name__ == '__main__':
    py_primos = Pyprimo()

    first_num = 0 #Número inicial
    last_num = 100000 #Número final

    print('\nIniciado')
    timenow = time()

    primos = py_primos.find_primos(first_num, last_num)

    print('Finalizado,', len(primos), f'números encontrados.')
    print(f'Tempo (s): {str(round((time()-timenow), 4))}\n')
