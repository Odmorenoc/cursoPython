from audioop import mul


def run ():
    nomultiplos2=[]
    for i in range (500):
        if i%2!=0:
            nomultiplos2.append(i)
            continue
        elif i==100:
            break
    print(nomultiplos2)
    


if __name__=="__main__":
    run()