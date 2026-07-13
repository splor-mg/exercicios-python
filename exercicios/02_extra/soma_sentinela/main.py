def resposta(numeros):
    soma = 0
    cont = 0

    while cont < len(numeros):
        if numeros[cont] == 0:
            break

        soma += numeros[cont]
        cont += 1

    return soma
