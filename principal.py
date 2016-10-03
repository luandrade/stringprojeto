import StringUtil
'''texto = input("digite o texto:")
StringUtil.output("Tamanho:",StringUtil.tamanho(texto))
StringUtil.output("Texto maiúsculo:",StringUtil.maiusculo(texto))
StringUtil.output("Texto minusculo:",StringUtil.minusculo(texto))'''
texto = input("digite um texto:")
letra = input("digite a letra a ser encontrada:")
repetições = StringUtil.contador(texto,letra)
StringUtil.output("a letra %s foi encontrada %i vezes" %(letra,repetições))
