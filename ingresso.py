''' Escreva um programa que leia a idade e o tipo de jogo e verifique,
    conforme regras de idade mínima para cada jogo, se a pessoa pode jogar ou não. '''

idade = int(input())
jogo = input()
lista = ["azar","mmorpg", "moba", "casual"]

if idade<0 or idade>130:
    print("Idade invalida.")

elif jogo not in lista:
    print("Jogo invalido.")

else:
    if idade>=10 and jogo=="moba":
        print("Pode entrar!")

    elif idade>=14 and jogo=="mmorpg":
        print("Pode entrar!")

    elif idade>=21 and jogo=="azar":
        print("Pode entrar!")

    elif jogo=="casual":
        print("Pode entrar!")

    else:
        print("Volte daqui há alguns anos.")