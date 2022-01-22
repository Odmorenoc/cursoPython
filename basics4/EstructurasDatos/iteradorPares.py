from typing import Iterator, Optional, Iterable


class PARES:
    def __init__(self, max: int = None) -> None:
        self.max: Optional[int] = max
    
    def __iter__(self) -> Iterator:
        self.num: int = 0
        return self
    
    def __next__(self) -> int:
        if not self.max or self.num <= self.max:
            result: int = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    a:Iterable = PARES(10)

    for i in a:
        print(i)
