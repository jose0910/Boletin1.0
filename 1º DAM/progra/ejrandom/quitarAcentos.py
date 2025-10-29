def quitarAcentos(palabra):
    acentos = "áéíóúÁÉÍÓÚ"
    sin_acentos = "aeiouAEIOU"

    for i in range(len(acentos)):
        palabra = palabra.replace(acentos[i], sin_acentos[i])

    return palabra


# Ejemplo de uso
texto = input("Introduce una palabra: ")
print("Sin acentos:", quitarAcentos(texto))
print("Con acentos: ", texto)


def eliminarAcentos(palabra):
    vocales = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U"
    }

    for k, v in vocales.items():
        palabra = palabra.replace(k, v)

    return palabra


# Programa principal
texto = input("Introduce una palabra: ")
print("Sin acentos:", eliminarAcentos(texto))
print("Con acentos: ", texto)




