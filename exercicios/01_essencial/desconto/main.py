def resposta(preço, desconto):
    desconto = preço * (desconto / 100)
    valor_final = preço - desconto
    return (desconto, valor_final)

