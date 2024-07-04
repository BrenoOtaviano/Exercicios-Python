#CONVERSOR DE MOEDAS NA COTACAO DO DIA 03/07/24

real = float(input('Quanto de dinheiro voce tem na carteira? R$ '))
dolar = real / 5.56
euro = real / 6
iene = real / 0.034
dolarCan = real / 4.07
print('Com {:.0f} reais, voce consegue ter {:.2f} em Dolar!'.format(real, dolar))
print('Com {:.0f} reais, voce consegue ter {:.2f} em Euro!'.format(real, euro))
print('Com {:.0f} reais, voce consegue ter {:.2f} em Iene!'.format(real, iene))
print('Com {:.0f} reais, voce consegue ter {:.2f} em Dolar Canadense!'.format(real, dolarCan))
