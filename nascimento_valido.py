dia = int(input())
dia_valido = False
mes_valido = False
ano_valido = False

if not 1 <= dia <= 31:
    print("Dia inexistente")
else:
    lista31 = [1, 3, 5, 7, 8, 10, 12]
    lista30 = [4, 6, 9, 11]
    mes = int(input())
    if 1 <= mes <= 12:
        mes_valido = True
        if not ((1 <= dia <= 31 and mes in lista31) or (1 <= dia <= 30 and mes in lista30) or (1 <= dia <= 29 and mes == 2)):
            print("Esse dia não existe nesse mês")
        else:
            ano = int(input())
            if 1900 <= ano <= 2020:
                ano_valido = True
                
                bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
                if mes == 2:
                    if bissexto:
                        if 1 <= dia <= 29:
                            dia_valido = True
                        else:
                            print("Esse dia não existe nesse mês")
                    else:
                        if 1 <= dia <= 28:
                            dia_valido = True
                        else:
                            print("Esse ano não é bissexto")
                else:
                    dia_valido = True
            else:
                print("Ano inexistente")
    else:
        print("Mês inexistente")

if dia_valido and mes_valido and ano_valido:
    print("Data Validada")