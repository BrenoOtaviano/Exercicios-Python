#REAJUSTE DE SALARIO EM PYTHON

salario = float(input("Digite seu salario para o reajuste: "))
reajuste = salario + (salario * 15 / 100)

print('-' *56)
print('O salario de R${:.0f} com o reajuste passou a ficar R${:.0f}'.format(salario, reajuste))
print('-' *56)