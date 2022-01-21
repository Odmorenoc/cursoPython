# hayar el Maximo común divisor

def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

# hayar el minimo comun multiplo.
def mcm(a, b):
    return (a * b) / mcd(a, b)

# crear una list comprehension de todos los multiplos elegidos por el usuario.
def run(top,a,b):
    nums=[i for i in range(1,top) if i%mcm(a,b) == 0]
    print(nums)
    

if __name__=="__main__":
    top=int(input("ingrese hasta que numero quiere validar los multiplos: "))
    a=int(input("escoja el primer multiplo: "))
    b=int(input("escoja el segundo multiplo: "))
    print("Los multiplos de ", a, " y ", b, " en el rango de 1 a ", top, "son: " )
    run(top, a, b)
