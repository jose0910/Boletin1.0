'''
Verificar dia/mes --- booleano

Verificar formato:
booleano
lonxitude total, dd, mm, aaaa
dd mm aaaa con caracteres numericos
'/' nas posicions adecuadas
evitar espazos inicio y fin

'''
def verificarFormatoData(data):
    verificacion = False
    data = data.strip()
    if len(data) == 10:
        if data[2] == "/" and data[5] == "/":
            dataSeparada = data.split("/")
            if len(dataSeparada[0]) == 2 and len(dataSeparada[1]) == 2 and len(dataSeparada[2]) == 4:
                if dataSeparada[0].isdecimal() and dataSeparada[1] .isdecimal() and dataSeparada[2].isdecimal():
                    verificacion = True

        return verificacion
print(verificarFormatoData("02/03/2001"))
print(int("02/05/2023"[0:2]))


def verificarFormatoData(data):
    diaMes = { 1:31,
               2:28,
               3:31,
               4:30,
               5:31,
               6:30,
               7:31,
               8:31,
               9:30,
               10:31,
               11:30,
               12:31}
    d = int(data[:2])
    m = int(data[2:4])
    a = int(data[4:])
    if m == 2:
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            diaMes[m] = diaMes[m] + 1
    if d < diaMes[m] and d < 0:
        return True
    else:
        return False










