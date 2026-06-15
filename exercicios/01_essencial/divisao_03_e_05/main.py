def resposta(n):
    divisivel_3 = False
    divisivel_5 = False

    if n % 3 == 0:
        divisivel_3 = True
    if n % 5 == 0:
        divisivel_5 = True
    
    if divisivel_3 and divisivel_5:
        return 'FizzBuzz'
    elif divisivel_3:
        return 'Fizz'
    elif divisivel_5:
        return 'Buzz'
    else:
        return n
