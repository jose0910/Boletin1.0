import random

def xerarContraseña(n):
    # tupla con números, letras minúsculas y mayúsculas
    l = (
        "1234567890",
        "abcdefghijklmnopqrstvwxyz",
        "ABCDEFGHIJKLMNOPQRSTVXYZ",
        "!@#$%&*+-_=?"
    )

    contrasinal = ''

    for i in range(n):
        tipo = random.randint(0, len(l) - 1)  # elige grupo
        iSim = random.randint(0, len(l[tipo]) - 1)  # elige carácter dentro del grupo
        contrasinal += l[tipo][iSim]

    return contrasinal


# Programa principal
while True:
    n = int(input("Introduce a lonxitude do contrasinal (0 para saír): "))

    if n == 0:
        break
    elif 6 <= n <= 12:
        print("Contrasinal xerado:", xerarContraseña(n))
    else:
        print("⚠️ A lonxitude válida é entre 6 e 12 caracteres.")


        print(abs )
