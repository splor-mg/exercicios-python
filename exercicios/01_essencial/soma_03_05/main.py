def resposta(n):
    somatorio = 0
    while n > 0: 
        if (n - 1) % 3 == 0 or (n - 1) % 5 == 0:
            somatorio = somatorio + (n - 1)
        n = n - 1            
    return somatorio

