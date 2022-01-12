from typing import Iterator


class fiboIter:
    
    def __init__(self, max: int = None) -> None:
        if max != None:
            self.max: int = max
        else:
            self.max = 10
    
    def __iter__(self):
        self.n1: int = 0
        self.n2: int = 1
        self.i: int = 0
        return self
    
    def __next__(self):
        if self.i == 0:
            self.i += 1
            return self.n1
        elif self.i == 1:
            self.i += 1
            return self.n2
        else:
            self.aux: int = self.n1 + self.n2

            if not self.i <= self.max:
                raise StopIteration
            else:
                self.n1, self.n2 = self.n2, self.aux
                self.i += 1
        return self.aux


if __name__ == '__main__':
    fibo10 = fiboIter()

    for i in fibo10:
        print(i)