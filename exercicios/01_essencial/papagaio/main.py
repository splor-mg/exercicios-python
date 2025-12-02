def resposta(falando, hora):
    if falando == False: 
        return False
    if falando == True:
        if hora < 7 or hora > 20:
            return True 
        else: 
            return False
