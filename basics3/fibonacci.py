def run(n):
    '''Devuelve el numero de fibonacci de un valor dado por el usuario.

    parametro n = int, valor de usuario.

    return = numero fibonacci correspondiente
    '''

    if n == 0 or n == 1:
        return 1
    else:
        return run(n-1) + run(n-2)


if __name__=='__main__':

    n = int(input('ingrese un enteropara calcular su numero de fibonacci: '))
    print(f'el numero de fibonacci para {n} es {run(n)}')