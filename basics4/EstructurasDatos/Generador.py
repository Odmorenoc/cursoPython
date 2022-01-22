from typing import Any, Generator, Iterator


def myGen()-> Generator:
    print('hola mundo')
    n: int = 0
    yield n

    print('hola cielo')
    n = 1
    yield n

    print('hola infierno')
    n = 2
    yield n

a:Iterator[Any] = myGen()

print(next(a))
print(next(a))
print(next(a))