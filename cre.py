''' Exiba a matrícula do aluno com menor CRE e o CRE médio da turma '''

soma_cre = 0
qnt_cre = 0
qnt_matricula = 0
menor = float('inf')
menor_matricula = ""

while True:
    matricula = input()
    if matricula == '999':
        break
    cre = float(input())
    soma_cre += cre
    qnt_cre += 1

    if cre < menor:
        menor = cre
        menor_matricula = matricula

media_cre = soma_cre/qnt_cre
print(menor_matricula)
print(f'{media_cre:.2f}')