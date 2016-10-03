def output(texto):
    print(texto)

def tamanho(texto):

    tamanho = len(texto)
    return tamanho

def maiusculo(texto):

    maiusculo = texto.upper()
    return maiusculo

def minusculo(texto):

    minusculo=texto.lower()
    return minusculo

def contador(texto,letra):
    repetições = 0
    for i in texto:
        if i == letra:
            repetições += 1
    return repetições

