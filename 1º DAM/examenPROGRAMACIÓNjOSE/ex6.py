"""
Crear a funcion que solicite un nome e un contrasinal verifica si el contrasinal ten como minimo 8 caracteres,
algun numero y alguna mayuscula, si cumple las reglas que imprima por pantalla contraseña valiva si no contraseña invalida
"""
def comprobarContrasinal(contrasinal):
    contrasinal= input("Introduce un contrasinal: ")


    si= True
    no= False
    for caracter in contrasinal:

        caracter = ["!", "@", "#", "%", "&", "*", "_"]
        print("Contraseña valida")
    else:
        print(si)
