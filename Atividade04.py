# -*- coding: latin1 -*-

#Programa de implementar uma função que retorne verdadeiro se o número for primo(falso caso contrário). Testar de 1 a 100.
def verificaPrimo(num):
    bPrimo = True
    if num >= 2:
        for i in range (2,num):
            if (num % i == 0):
                bPrimo = False
                break
    else:
        bPrimo = False

    return bPrimo

valueInput = int(input("Digite um número inteiro para verificar se é primo: "))
primo = verificaPrimo(valueInput)
if primo :
    print(f"{valueInput} é primo!")
else:
    print(f"{valueInput} não é primo!")
