'''Arquivo para a leitura dos dados das vendas e ações de decisão.'''

'''imports'''
import datetime

data = datetime.date.today()
dia = data.day
mes = data.month
ano = data.year


def ler_data():
    data = ("%02d/%02d/%d"%(dia, mes, ano))
    return data


def ler_nome():
    nome_cliente_venda = input("##### Nome do Cliente: ")
    return nome_cliente_venda


def ler_livro():
    livro_comprado = input("##### Nome do Livro Comprado: ")
    return livro_comprado


def ler_unidades():
    verificador = True
    while verificador:
        try:
            unidades = int(input("##### Unidades Vendidas (NÚMERO INTEIRO): "))
            if (unidades >= 1):
                verificador = False
            else:
                print("-> Insira uma quantidade válida!")
                print()
        except ValueError:
            print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
    return unidades


def ler_valor():
    verificador = True
    while verificador:
        try:
            valor = float(input("##### Valor de Venda (R$ -> DECIMAL): "))
            if (valor >= 0):
                verificador = False
            else:
                print("Insira um valor(R$) válido!")
                print()
        except ValueError:
            print("!!! Resposta não reconhecida como número DECIMAL(R$). Tente novamente !!!")
    return valor


def ler_forma_pgto():
    forma_pgto = input("##### Forma de pagamento: ")
    return forma_pgto


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