def read():
    n=[]
    with open("./archivos/numbers.txt", "r" ) as f:
        for l in f:
            n.append(int(l))
    print(n)
    pass


def write():
    names=["facundo", "Oscar", "Leidy", "David", "Paola"]
    with open("./archivos/names.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    pass


def run():
    read()
    write()


if __name__=="__main__":
    run()