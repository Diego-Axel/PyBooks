
'''Validações'''

import datetime 
data = datetime.date.today()
dia = data.day
mes = data.month
ano = data.year

import re

#################################################
#####            VALIDAR E-MAIL             #####
#################################################

def validar_email(email): # Função para verificar se o e-mail é válido (GPT)
    padrao = re.compile(r'^[\w-]+@[a-z\d]+\.[\w]{2,3}$')
    return padrao.match(email) is not None


#################################################
#####            VALIDAR CELULAR            #####
#################################################

def validar_numero(numero): # Função para validar telefone (GPT)
    padrao = re.compile(r'^\(\d{2}\) \d{4,5}-\d{4}$')
    return padrao.match(numero) is not None


#################################################
#####             VALIDAR DATA              #####
#################################################

def validar_data(): # Função para validar a data (feita por mim - Diêgo Axel)
    verificador = True
    while verificador:
        try:
            dia_venda = int(input("Insira o dia da venda: "))
            if (dia_venda <= 31) and (dia_venda >= 1):
                verificador = False
            else:
                print("OPS! Aparentemente você colocou um dia inválido. Tente novamante.")
                print()
        except ValueError:
            print("Coloque um dia válido ou certifique-se que está inserindo um número inteiro. Por favor, digite novamente.")
            print()
    verificador = True
    while verificador:
        try:
            mes_venda = int(input("Insira o mês da venda: "))
            if (mes_venda <= 12) and (mes_venda >= 1):
                verificador = False
            else:
                print("OPS! Aparentemente você colocou um mês inválido. Tente novamante.")
                print()
        except ValueError:
            print("Coloque um mês válido ou certifique-se que está inserindo um número inteiro. Por favor, digite novamente.")
            print()
    verificador = True
    while verificador:
        try:
            ano_venda = int(input("Insira o ano da venda: "))
            if (ano_venda <= ano) and (ano_venda >= 2000):
                verificador = False
            else:
                print("OPS! Aparentemente você colocou um ano inválido. Tente novamante.")
                print()
        except ValueError:
            print("Coloque um ano válido ou certifique-se que está inserindo um número inteiro. Por favor, digite novamente.")
            print()
    print()
    data_venda = ("%02d/%02d/%d"%(dia_venda,mes_venda,ano_venda))
    print("########################################")
    print("- Data modificada para a dia desejado! -")
    print("########################################")
    return data_venda


#################################################
#####             VALIDAR CPF               #####
#################################################

def validar_cpf(cpf): # Disponibilizada pelo professor Flavius 
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0
    if tam != 11:
        return False
    for i in range(11):
        if (cpf[i]<'0')or(cpf[i]>'9'):
            return False
    for i in range(9):
        soma += (int(cpf[i])*(10 - i))
    d1 = 11 - (soma % 11)
    if (d1 == 10 or d1 == 11):
        d1 = 0
    if d1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += (int(cpf[i])*(11-i))
    d2 = 11 - (soma%11)
    if (d2 == 10 or d2 == 11):
        d2 = 0
    if d2 != int(cpf[10]):
        return False
    return True