#TABUADA SIMPLES

print("--------------")
tabuada=int(input("Digite um numero para gerar a tabuada: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
print("--------------")