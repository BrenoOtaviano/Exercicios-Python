#ALUGUEL DE CARROS

km = int(input("Quantos KM foram percorridos? "))
dias = int(input("Quantos dias de locação? "))
pago = (dias * 60) + (km * 0.15)
print("Diante das informacoes recebidas, o valor a ser pago fica em: R${:.2f}".format(pago))