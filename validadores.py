'''Validações'''

'''imports'''
import datetime # Para ver se a data inserida é valida.
import re

#################################################
#####            VALIDAR -EMAIL             #####
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
#####              VALIDAR DATA             #####
#################################################

data = datetime.date.today()

dia = data.day
mes = data.month
ano = data.year

def validar_data(data_final):
    verificador = True
    while verificador:
        try:
            dia_venda = int(input("Insira o dia da venda: "))
            if (dia_venda <= 31):
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
            if (mes_venda <= 12):
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
            if (ano_venda <= ano):
                verificador = False
            else:
                print("OPS! Aparentemente você colocou um ano inválido. Tente novamante.")
                print()
        except ValueError:
            print("Coloque um ano válido ou certifique-se que está inserindo um número inteiro. Por favor, digite novamente.")
            print()
    print()
    data_final = ("%02d/%02d/%d"%(dia_venda,mes_venda,ano_venda))
    return data_final