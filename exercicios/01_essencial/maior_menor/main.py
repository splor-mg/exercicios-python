def resposta(n1, n2, n3):
    if n1 >= n2:
        maior_numero = n1
        menor_numero = n2
    else:
        maior_numero = n2
        menor_numero = n1
    if maior_numero <= n3:
        maior_numero = n3
    if menor_numero >= n3:
        menor_numero = n3
    return (maior_numero, menor_numero)

