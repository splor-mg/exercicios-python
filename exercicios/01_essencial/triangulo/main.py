def resposta(x, y, z):
    if (x + y) <= z or (x + z) <= y or (y + z <= x):
        return "não forma triângulo"
    else:
        if x == y and x == z:
            return "equilátero"
        elif x == y or x == z or y == z:
            return "isósceles"
        else:
            return "escaleno"
