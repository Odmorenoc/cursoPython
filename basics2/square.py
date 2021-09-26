def run():
    # nums = []
    # sqrt = []
    # non3 = []
    # si3 = []


    # for i in range (0,101):
    #     nums.append(i)
    #     sqrt.append(i**2)
    #     if i%3 != 0 or i==0:
    #         non3.append("no")
    #     else:
    #         si3.append(i**2)
    #         non3.append("si")


    # for i in nums:
    #     print(nums[i], " es raiz de: ", sqrt[i], " y ", non3[i], " es multiplo de 3 ")
    
    
    # print("Los cuadrados de los multiplos de 3 son: ")
    # for i in si3:
    #     print(i, "Es el cuadrado de ", i**0.5)
    

    nums=[i for i in range(1,101)]
    sqrt=[i**2 for i in range(1,101)]
    non3 = [i**2 for i in range(1,101) if i%3 != 0]
    si3 = [i**2 for i in range(1,101) if i%3 == 0]

    # for i in non3:
    #     print(i)

    print("los numeros de 1 a 100 son: ", nums, "sus cuadrados son: ", sqrt)
    print("Los cuadrados de los numeros que no son multiplos de 3 son: ", non3, " y los que si son multiplos son: ", si3) 

if __name__=="__main__":
    run()