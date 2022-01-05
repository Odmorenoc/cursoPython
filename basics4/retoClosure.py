def makeDivisionBy(divisor: int):
    return lambda dividendo: dividendo/divisor

dividirPor3: float = makeDivisionBy(3)
print(dividirPor3(18)) 

dividirPor5: float = makeDivisionBy(5)
print(dividirPor5(100))

dividirPor18: float = makeDivisionBy(18)
print(dividirPor18(54))

print(dividirPor3(dividirPor5(15)))