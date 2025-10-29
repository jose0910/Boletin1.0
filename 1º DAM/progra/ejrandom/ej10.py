inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * ( interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * ( interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))