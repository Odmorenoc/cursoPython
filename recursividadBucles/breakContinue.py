def run ():
    for i in range (500):
        if i%2!=0:
            continue
        elif i==100:
            break
        print(i)


if __name__=="__main__":
    run()