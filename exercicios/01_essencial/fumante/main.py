def resposta(cigarros, anos):
    total_cigarros = int(anos) * 365 * int(cigarros)
    minutos = total_cigarros*10
    dias = minutos / (60 * 24)
    return (int(dias))