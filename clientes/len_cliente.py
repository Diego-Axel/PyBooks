'''Arquivo para a leitura dos dados dos clientes e ações de decisão.'''

'''imports'''
import validadores


def ler_nome():
    nome = input("##### Nome: ")
    return nome


def ler_email():
    verificador = True # Maneira de usar while atraves de variaveis que guardam operadoes lógicos, dica de Matheus Diniz.
    while verificador:
        email = input("#### E-mail: ")
        if validadores.validar_email(email):
            print("E-mail válido!")
            verificador = False
        else:
            print("O e-mail não é válido, veja se você não esquceu o '@'/domínio/'.com'. Por favor digite novamente.")
    return email


def ler_celular():
    verificador = True
    while verificador:
        print("##### Digite o Celular com DDD e o 9 adicional seguindo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
        celular = input("##### Digite seu Celular: ")
        if validadores.validar_numero(celular):
            print("Numero válido!")
            verificador = False
        else:
            print("Número não válido. Digite um número válido.")
    return celular


def ler_cpf():
    cpf = input("##### CPF: ")
    return cpf


def ler_decisao_alteracao():
    verificador = input("#### Deseja Alterar mais dados(S/N)? ")
    verificador = verificador.upper()
    if (verificador == "NÃO") or (verificador == "NAO") or (verificador == "N"):
        verificador = False
        print()
    else:
        verificador = True
        print()
    return verificador