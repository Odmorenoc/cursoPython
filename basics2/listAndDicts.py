def run():
    list = [1, "helo", True, 4.5]
    dict = {
        "firstName": "Oscar",
        "LastName": "Moreno" 
    }

    superList = [{
        "firstName":"Miguel",
        "LastName":"Torres" 
    },
    {
        "firstName":"Pepe",
        "LastName":"Rodelo" 
    },
    {
        "firstName":"Susana",
        "LastName":"Martinez" 
    },
    {
        "firstName":"Jose",
        "LastName":"Garcia" 
    }]

    SuperDict = {
        "Super_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in SuperDict.items():
        print(key, "=", value)
    
    for i in superList:
        print(i["LastName"], i["firstName"])

    for i in superList:
        print(i)


if __name__ == "__main__":
    run()
