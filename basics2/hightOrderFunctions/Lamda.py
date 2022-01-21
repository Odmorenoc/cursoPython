def run():
    # se crea una lamda function para el ejercicio de palindromo.py realizado en basics/texto
    pregunta= """por favor ingrese el texto a evaluar como palindromo: 
    """
    palindromo = lambda string: (print("es palindrono") if string == string[::-1] else print("no es palindromo"))
    print(palindromo(input(print(pregunta))))
    

if __name__ == "__main__":
    run()