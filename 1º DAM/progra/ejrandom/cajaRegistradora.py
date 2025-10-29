
"""
-Calculo importe por caixa
-Calculo importe total
-Impresion contido caixa
-Impresion contido total
"""

efectivo = [
    ["500", 0],
    ["200", 0],
    ["50", 13],
    ["20", 5]
]

monedas = [
    ["2", 0],
    ["1", 0],
    ["0.50", 10],
    ["0.20", 13]
]


# --- Cálculo del importe por caja ---
def calcular_importe(caja):
    total = 0
    for valor, cantidad in caja:
        total += float(valor) * cantidad
    return total


# --- Impresión del contenido y totales ---
def imprimir_caja(nombre, caja):
    print(f"\nContenido de la caja de {nombre}:")
    for valor, cantidad in caja:
        print(f"  {cantidad} unidades de {valor} €")
    print(f"Importe total en {nombre}: {calcular_importe(caja):.2f} €")


# --- Programa principal ---
print("=== CÁLCULO DE IMPORTE TOTAL ===")

imprimir_caja("billetes", efectivo)
imprimir_caja("monedas", monedas)

importe_total = calcular_importe(efectivo) + calcular_importe(monedas)

print("El impoorte total es: " + str(importe_total) + "€")
