'''
    Ler um número inteiro Y e até 20 inteiros (parando em -1), contando quantas vezes Y aparece 
    e calculando a média dos positivos fora do intervalo [15,20].
'''

cont1 = 0
cont2=0
soma = 0
Y = int(input())

for i in range(1,21):
    M = int(input())
    if M == -1:
        break
    else:
        if M == Y:
            cont1+= 1
        if (0<M<15) or (M>20):
            cont2+=1
            soma += M

print(f"O número {Y} apareceu {cont1} vez(es)")

if cont2>0:
    media = soma/cont2
    print(f'A média dos números foi de: {media:.2f}')

else:
    print("Sem valores para calcular a média")

