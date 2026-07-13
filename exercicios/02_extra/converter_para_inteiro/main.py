def resposta(texto):
    try:
        return int(texto)
    except ValueError:
        return 'Valor inválido'
