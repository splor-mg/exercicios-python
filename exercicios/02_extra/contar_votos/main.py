def resposta(votos):
    contagem = {}
    for voto in votos:
        contagem[f"{voto}"] = votos.count(voto)
    return contagem
