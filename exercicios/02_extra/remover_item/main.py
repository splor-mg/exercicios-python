def resposta(lista, item):
    if item in lista:
        lista.remove(item)
        return lista
    else:
        return lista
