cadena = " Hola Mundo "
cadenasSinEspacios= cadena.replace(" ", "")
print(cadenasSinEspacios)

texto = "   hola mundo   "

# Eliminar espacios del inicio
while len(texto) > 0 and texto[0] == " ":
    texto = texto[1:]

# Eliminar espacios del final
while len(texto) > 0 and texto[-1] == " ":
    texto = texto[:-1]

print(texto)


