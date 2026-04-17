def resposta(temperatura, tipo):
    if tipo == "F":
        temperatura = (temperatura - 32) * 5 / 9
    else:
        temperatura = (9 * temperatura / 5) + 32
    return temperatura
