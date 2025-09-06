'''
Escreva um programa que, dado o número de competidores, 
a pontuação mínima e as notas das duas fases, 
calcule quantos competidores serão convidados (soma ≥ mínima e sem zerar em nenhuma fase).
'''


N = int(input())
P = int(input())
cont = 0

for i in range(N):
    X = int(input())
    Y = int(input())
    soma = X+Y

    if soma>=P:
        cont +=1
        qntd_final = cont

    else:
        qntd_final = cont - 1

print(qntd_final)


    