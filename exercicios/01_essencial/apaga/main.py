def resposta(palavra, index):
    if index >= len(palavra):
        return palavra
    return palavra[:index] + palavra[index+1:]
