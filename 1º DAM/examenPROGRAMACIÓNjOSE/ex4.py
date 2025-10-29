"""
Crea una funcion que verifique si un contrasinal pasado por in parametro ten polo menos
un numero. A funcion retornara un valor booleano indicando se ten numero ou non
"""
def comprobarContrasinal(numeros):
    contrasinal= input("Introduce un contrasinal: ")
    contrasinal = len(contrasinal)
    numeros= (1,2,3,4,5,6,7,8,9,0)
    if numeros in contrasinal:

        print(True)
    else:
        print(False)


comprobarContrasinal()