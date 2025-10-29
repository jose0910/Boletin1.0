"""
Crea una funcion que verifique si un contrasinal pasado por in parametro ten un caracter
especial dos que se mostran a continuación: !, @, #, %, &, *, _
"""



def comprobarContrasinal(contrasinal):
    contrasinal= input("Introduce un contrasinal: ")


    si= True
    no= False
    for caracter in contrasinal:
        caracter = ["!", "@", "#", "%", "&", "*", "_"]
        print("Si ten un caracter especial")
    else:
        print(si)


comprobarContrasinal()