# Programa para realizar operações dadas pelo usuario
# Eduardo Airton
import os


sair = ""
os.system('cls') #Limpa o prompt
while sair.lower() != "nao":

    try:
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("\n-----------------")
        print("ERRO")
        print("Digite um numero valido!")
        print("-----------------")
        print("\n")
        continue

    operacao = input("\nDigite a operação desejada: \n-> + \n-> -\n-> *\n-> /\nResposta: ")

    if operacao == "+":
        resultado = float(numero1) + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2
    else:
        print("Operação invalida!")
        continue

    os.system('cls')
    print("-----------------------------------------")
    print("O resultado de {} {} {} e = {}".format(numero1, operacao, numero2, resultado))
    print("-----------------------------------------")


    sair = input("\nDeseja realizar outra operacao? \n-> SIM\n-> NAO\nResposta: ")
    os.system('cls') #Limpa o prompt

print("Calculadora encerrada!")
