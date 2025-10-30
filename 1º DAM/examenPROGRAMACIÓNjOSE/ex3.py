"""Crea una funcion que comprobe si un contrasinal pasado por parámetro
ten polo menos unha letra mayuscula A función retornará un valor booleano indicando si ten letra mayuscula ou non.
"""

def comprobarContrasialMayus(contraseña):
    mayusculas= ["ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"]
    for letra in contraseña :
        for mayuscula in mayusculas :
         if letra == mayuscula:
            return True

comprobarContrasialMayus()

def comprobarContrasinal(contraseña):
    for letra in contraseña:
        if letra == letra.upper():
            return True

def comprobarCOntrasinalNumero(contraseña):
    for caracter in contraseña:
        if caracter.isNumeric():
            return True