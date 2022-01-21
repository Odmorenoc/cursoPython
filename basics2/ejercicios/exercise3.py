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

def run():
    #ejercicio de crear un filtro que guarde solo los nombres de los trabajadores que dominan el lenguage python con una combinación de las HOF filter y map
    all_python_devs_names=list(map(lambda worker: worker["name"], filter(lambda worker: worker["language"]=="python", DATA)))
    print("los programadores que manejan python son: ",all_python_devs_names)

    #ejercicio de crear un filtro que guarde solo los nombres de los trabajadores que dominan el lenguage python con una combinación de las HOF filter y map
    all_platzi_workers=list(map(lambda worker: worker["name"], filter(lambda worker: worker["organization"]=="Platzi", DATA)))
    print("los desarrolladores de Platzi son: ",all_platzi_workers)

    # ejericio crear una list Comprehension de el diccionario DATA agregando la llave boleana "old" 
    old_people=[worker | {"old": worker["age"]>=70} for worker in DATA]
    print("el diccionario con la nueva llave es: ",old_people)

    # Ejercicio crear una list comprehension con los nombres de los trabajadores que son mayores de edad.
    adults = [worker["name"] for worker in DATA if worker["age"]>=18]
    print("Los trabajadores mayores de edad son:", adults)

    pass

if __name__=="__main__":
    run()