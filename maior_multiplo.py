'''
Encontre o maior múltiplo de M menor ou igual a N, ou informe que não existe.
'''
M = int(input())
N = int(input())

maior = 0
for i in range(1,N+1):
    if (i % M == 0):
        maior = i

if maior>0:
    print(maior)
else:
    print(f"sem multiplos menores que {N}")