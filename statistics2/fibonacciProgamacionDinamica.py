import sys

def fibonacciRecursivo(n):

    if n == 0 or n == 1:
        return 1
    else:
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

def fibonacciDinamico(n , memo={}):
    if n == 0 or n == 1:
        print(f'(if) el fibonacci de {n} es: 1')
        return 1
    
    try:
        print(f'(try) el fibonacci de {n} es: {memo[n]}')
        return memo[n]
    except:
        resultado = fibonacciDinamico(n-1, memo) + fibonacciDinamico(n-2, memo)
        memo[n] = resultado

        return resultado

if __name__=='__main__':
    sys.setrecursionlimit(100002)
    n = int(input('ingrese un entero para calcular su numero de fibonacci: '))
    resultado=fibonacciDinamico(n)
    print(f'el numero de fibonacci para {n} es {resultado}')