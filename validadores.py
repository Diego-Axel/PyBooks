
'''Validações'''

'''imports'''
import datetime # Para ver se a data inserida é valida.
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
#####             VALIDAR CPF               #####
#################################################

def validar_cpf(cpf): # Vou colocar ainda
    pass