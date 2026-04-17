def resposta(valor, horas):
    salario_bruto = valor * horas
    imposto_renda = salario_bruto * 0.11
    imposto_inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    descontos = imposto_renda + imposto_inss + sindicato
    salario_liquido = salario_bruto - descontos
    return (salario_bruto, imposto_renda, imposto_inss, sindicato, salario_liquido)
