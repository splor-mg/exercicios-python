def resposta(texto):
    texto = texto.lower()
    palavras = texto.split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem
