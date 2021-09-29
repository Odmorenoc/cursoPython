DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run ():
    # filtro1: todos los devs de python.

    filter1 = [worker["name"] for worker in DATA if worker["language"]== "python"]
    
    #print(filter1)
    # for worker in filter1:
    #     print(worker)
    
    # filtro2: todos los devs de Platzi
    filter2 = [worker["age"] for worker in DATA if worker["organization"]=="Platzi"]
    # print(filter2)

    #filtro3: todos los mayores de edad
    # filter3 = [worker["name"] for worker in DATA if worker["age"]>=18]
    # print(filter3)

    #filtro3: todos los mayores de edad con la HOF filter, pero se obtiene todo el diccionario.
    filter3=list(filter(lambda worker: worker["age"]>=18, DATA))
    ## para obtener solo el nombre del trabajador mayor de edad se utiliza map.
    # filter3=list(map(lambda worker: worker["name"], filter3))
    # print(filter3)

    #filtro4: agregar una nueva llave con valores booleanos si el trabajador supera los 70 años.
    filter4=list(map(lambda worker: worker | {"old": worker["age"]>=18}, DATA))
    print(filter4)
    pass


if __name__=="__main__":
    run()