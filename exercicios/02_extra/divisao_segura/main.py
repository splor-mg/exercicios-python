def resposta(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Valores inválidos"
