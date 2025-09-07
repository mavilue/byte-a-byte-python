'''
Um número inteiro é dito perfeito se o dobro dele é igual à soma de todos os seus divisores.
Escreva um programa que liste todos os números perfeitos menores que um inteiro n dado.
'''
n = int(input())

for num in range(1, n):
    soma = 0
    for i in range(1, num + 1):
        if num % i == 0:
            soma += i
    if soma == 2 * num:
        print(num)