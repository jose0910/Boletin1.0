'''
Hacer un programa que de una contrasella
como minimo de 6 a 12
las letras sean minusculas y mayusculas aleatoriamente
que tambien contenga simbolos y numeros
'''
import random
import string

def generar_contrasena():
    # Longitud aleatoria entre 6 y 12
    longitud = random.randint(6, 12)

    # Conjuntos de caracteres
    letras = string.ascii_letters      # a-z + A-Z
    numeros = string.digits            # 0-9
    simbolos = string.punctuation      # !@#$%^&*()_+...

    # Combinar todos los tipos
    todos = letras + numeros + simbolos

    # Asegurar que haya al menos uno de cada tipo
    contrasena = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Completar hasta la longitud deseada
    contrasena += random.choices(todos, k=longitud - len(contrasena))

    # Mezclar los caracteres
    random.shuffle(contrasena)

    # Unir en un string final
    return ''.join(contrasena)

# Ejemplo de uso
print("Tu contraseña generada es:", generar_contrasena())
print("esta contraseña es bastante segura")
'''
def xerarContraseña(n):
t=("123456789",abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTVXYZ)
i= 0 
contrasinal = ''
while i < n:
tipo = random.randint(0,3)
iSim = random.randint(0,len(l[tipo]))
    contrasinal = contrasinal + l[tipo][iSim]
    return contrasinal
while True:
    n= int(input("Introduce la longitud do contrasinal. (0 para "))
    if n >= 6 and n <=12:
        print(xeradorContrasinais(n))
    elif n == 0:
        break
    else:
        print("A lonxitude válida e entre 6 y 12")


'''
