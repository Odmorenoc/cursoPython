pregunta= """por favor ingrese el texto a evaluar como palindromo: 
"""
def palindromo():
    texto=input(print(pregunta))
    texto=texto.replace(" ","").lower()
    inverso=texto[::-1]
    if texto==inverso:
        print("el texto es un palindromo")
    else :
        print("el texto no es un palindromo")


palindromo()