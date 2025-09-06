''' 
    Transportar mochila com ate 18kg
    a entrada deve parar quando um novo livro exceder a capacidade da mochila.
 '''

limite = 18
cont = 0
peso_livro = 0

while True:
    livro_add = float(input())
    cont += 1
    peso_livro += livro_add
    if peso_livro > limite:
        qnt_possivel = cont - 1
        break

print(qnt_possivel)
