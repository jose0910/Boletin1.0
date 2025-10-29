


for i in range(10, 0, -1):
 print(i)

resultado = input('digite algo: ')
print (resultado + str(22))


resultado = input('digite algo: ')

numero= int(resultado)
print(numero + 2)
str(22)
float("22.23")
bool("un string") #True
bool(None) #False


edad = 22
print(edad > 18 and edad < 30)
print(not (edad >1))


puntuacion = 97
if puntuacion <= 96:
        print("APROBADO")
elif puntuacion >= 50:
    print("aprobado")
else:
    print("REPROBADO")

print("Fuera del if")


temperatura = float(input("digite temperatura: ") )
escala = input ("Es Fahrenheit(F) o es Celsius(C)?: ").lower()
if escala == "f":
    celsius = (temperatura - 32)  * (5/9)
    print(celsius)
elif escala == "c":
    farenheit = temperatura * 1.8 + 32
    print(farenheit)
else:
    print("El valor de escala es incorrecto")



lenguajes = ["Python", "Ruby", "PHP", "Java"]

lenguajes[1] = "Python"
print (lenguajes)
print (lenguajes[1:3])

lenguajes.insert(3, "Go")
print(lenguajes)

lenguajes.remove ("Java")
print("PHP" in lenguajes)
print(len(lenguajes))


i = 1
while i <= 5:
    print(i)
    i = i + 1
