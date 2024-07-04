#PORCENTAGEM EM PYTHON

produto = float(input('Digite o valor do Produto: '))
desconto = produto - (produto * 5 / 100)
print('O produto que custava R${:.2f}, com 5% de desconto passou a custar: R${:.2f}'.format(produto, desconto))
