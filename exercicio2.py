#MEDIA DE ALUNOS

n1 = int(input("Digite a primeira nota do aluno: "))
n2 = int(input("Digite a segunda nota do aluno: "))

media = (n1 + n2) /2

if (media < 7):
    print('Aluno reprovado')
else:
    print("Aluno aprovado, boas ferias!")

print("Sua nota final foi: {:.0f}".format(media))