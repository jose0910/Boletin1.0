"""Crea una funcion que comprobe si un contrasinal pasado por parámetro
ten mais de 8 caracteres. A función retornará un valor booleano indicando si ten máis ou non.
"""
def comprobarContrasinal():
    contrasinal= input("Introduce un contrasinal: ")
    contrasinal = len(contrasinal)
    si= True
    no= False
    if contrasinal > 8:
        print(no)
    else:
        print(si)


comprobarContrasinal()