"""Crea una funcion que comprobe si un contrasinal pasado por parámetro
ten mais de 8 caracteres. A función retornará un valor booleano indicando si ten máis ou non.
"""

usuContra = ["Manuel", "canMorto"], ["Pepe", "Juan"]

def comprobarContrasinal(listaUsuarios):
    existeUsuario = False
    nomeUsuario= input("Introduce un nome de usuario?: ")
    contraseña= input("Introduce un contrasinal: ")
    for usuarioContrasinal in listaUsuarios:
        if usuarioContrasinal[0] == nomeUsuario:
            if usuarioContrasinal[1] == contraseña:
                existeUsuario = True

    return existeUsuario

