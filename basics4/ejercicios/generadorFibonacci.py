def fiboGen(max):
    
    n1, n2, estado = 0, 1, True

    while estado:
        if  n1 <= max:
            yield n1
            n1, n2 = n2, n1 + n2
        else:
            estado = False

    
if __name__== '__main__':
    fibonacci = fiboGen(100)

    for i in fibonacci:
        print(i)
