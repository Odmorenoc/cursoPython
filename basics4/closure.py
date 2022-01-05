from typing import Any, Callable

def repetidor(multiplicador: int) -> Callable:
    return lambda cadena: cadena*multiplicador if type(cadena) == str else "solo cadenas "

cadena : str = '1'

duplicar: Callable = repetidor(2)
triplicar: Callable = repetidor(3)

duplicado: Callable = duplicar(cadena)
triplicado: Callable = triplicar(cadena)
repetidorX18: Callable = triplicar(duplicar(triplicar(cadena)))
print(repetidorX18)
