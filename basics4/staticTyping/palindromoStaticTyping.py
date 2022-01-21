def run(texto: str):
    # texto: str =input(print(pregunta))
    texto=texto.replace(" ","").lower()
    inverso: str =texto[::-1]
    if texto==inverso:
        print("el texto es un palindromo")
    else :
        print("el texto no es un palindromo")


if __name__=="__main__":
    pregunta= """por favor ingrese el texto a evaluar como palindromo: 
    """
    run(1000)