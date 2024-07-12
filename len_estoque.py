'''Arquivo para a leitura dos dados dos produtos no estoque e ações de decisão.'''

'''OBS: Irei fazer verificadores para essas funções, ou melhor, uma função só para todas as strings.'''

def ler_nome():
    nome_livro = input("##### Nome do Livro: ")
    return nome_livro


def ler_descricao():
    descricao = input("##### Descrição: ")
    return descricao


def ler_autor():
    autor = input("##### Autor: ")
    return autor


def ler_ano():
    ano = input("##### Ano: ")
    return ano


def ler_capa():
    tipo_capa = input("##### Tipo de Capa: ")
    return tipo_capa


def ler_genero():
    print()
    print("###########################")
    print("##### GÊNERO TEXTUTAL #####")
    print("###########################")
    print("| 1 - Ação \n| 2 - Ficção \n| 3 - Suspense \n| 4 - Educativo \n| 5 - Infantil \n| 6 - Recreativo \n| 7 - Romance \n| 8 - Amplo")
    print()
    verificador = True
    while verificador:
        try: # Tratar exeções junto com o EXCEPT | Estou usando para verificar se o usuário colocou o número como pedido (estudos na internet)
            genero = int(input("##### Tipo de Gênero (NÚMERO INTEIRO): "))
            verificador = False
        except ValueError:
            print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
    return genero


def ler_qtd():
    verificador = True
    while verificador:
        try:
            qtd_estoque = int(input("##### Quantidade em Estoque (NÚMERO INTEIRO): "))
            verificador = False
        except ValueError:
            print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
    return qtd_estoque


def ler_valor():
    verificador = True
    while verificador:
        try:
            valor_livro = float(input("##### Valor desse Livro (R$ -> NÚMERO DECIMAL): "))
            verificador = False
        except ValueError:
            print("'!!! Resposta não reconhecida como um número DECIMAL. Tente novamente !!!")
    return valor_livro


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