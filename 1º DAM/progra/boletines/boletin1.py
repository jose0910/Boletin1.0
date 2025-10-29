def potencia():
    print("Calcularanse potencia de dous números")
    n1 = input("Ingrese un número enteiro: ")
    n2 = input("Ingrese otro número enteiro: ")

    for x in range(int(n1), int(n2)):


        print(f"El cuadrado de {x} es {x * x}")

    print("É todo por agora")





potencia()
#con 3 y 5 nos da los valores de 9 y 16 porque son los cuadrados de 3 y 4
#con 3 y 3 no nos devuelve ningun valor que que es el mismo numero
#con 5 y 3 no nos devuelve nada porque 5 es mayor que 3 en todo caso tendriamos que poner
# ", -1" para que los diera el resultado al reves

print("==============================")


def hola():
    nombre= input("Ingrese su nombre ")
    print(f"Hola {nombre}")
hola()
print("=============================")
def produto():
    n1= int(input("ingrese un numero: "))
    n2= int(input("ingrese un numero: "))
    resultado= n1 * n2
    print(f"El produto de {n1} y {n2} es {resultado}")
produto()
print("=============================")

def cuadrado():
    n1= int(input("altura: "))
    n2= int(input("base: "))
    area= n1 * n2
    perimetro= (n1 + n2)*2
    print(f"la area del cuadrado es: {area}")
    print(f"el perimetro del cuadrado es: {perimetro}")

cuadrado()

import math  # para usar o número pi

def circulo():
    print("Cálculo do perímetro e da área dun círculo.")
    r = float(input("Introduce o radio do círculo: "))

    perimetro = 2 * math.pi * r
    area = math.pi * r ** 2

    print(f"O perímetro do círculo é: {perimetro:.2f}")
    print(f"A área do círculo é: {area:.2f}")

circulo()

for i in range(5):
    a = i + 1
    print(a)
    print (i * i)
print("=============================")
for i in range(2,6):
    print(f" 2 elevado a {i} = ")
    print (i, 2**i)
print("=============================")
for d in [3, 1, 4, 1, 5]:
    print (d,)
print("=============================")
for x in range(2, 4 ):
    print(x)

print("Introduce dos numeros para saber su multiplicacion, suma y resta.")
n1 = int(input("Ingrese un numero"))
n2 = int(input("Ingrese otro numero"))
suma= n1 + n2
resta= n1 - n2
multiplicacion= n1 * n2
if n2 != 0:
    division= n1 / n2
else:
    division= "no se puede dividir entre 0"
print(f"la suma es: {suma} la resta es: {resta} \nla multiplicacion es: {multiplicacion} \n la division es: {division}")

n = int(input("Ingrese un numero"))
print(f"la tabla de multiplicar de {n} es: ")
for x in range(1, 11):
    multiplicacion = n * x
    print(multiplicacion)


x = input("Ingrese una palabra: ")

def imprimir_pabla():
    for x in range(100):
        print(x)
        print(" ")
imprimir_pabla()


# Pedir unha palabra ao usuario
palabra = input("Introduce unha palabra: ")

# Repetila 1000 veces con espazos intermedios
resultado = (palabra + " ") * 1000

# Amosar o resultado
print(resultado)


