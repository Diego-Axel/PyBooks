'''Arquivo das Funções do ESTOQUE'''

'''imports'''
import pickle
import os

#################################################
#####          DICIONÁRIO ESTOQUE           #####
#################################################

produtos = {} # Dicionário onde sera Salvo os Dados dos Produtos(Livros)
try:
  arq_produtos = open("produtos.dat", "rb")
  produtos = pickle.load(arq_produtos)
except:
  arq_produtos = open("produtos.dat", "wb")
arq_produtos.close()


#################################################
#####          FUNÇÕES DO ESTOQUE           #####
#################################################
#-----------------------------------------------

#################################################
#####           CADASTRAR PRODUTO           #####
#################################################

def cadastrar_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Produto         #####")
  print("############################################")
  print()
  code_produto = len(produtos) + 1
  print()
  nome_livro = input("##### Nome do Livro: ")
  print()
  descricao = input("##### Descrição: ")
  print()
  autor = input("##### Autor: ")
  print()
  ano = input("##### Ano: ")
  print()
  tipo_capa = input("##### Tipo de Capa: ")
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
  print()
  verificador = True
  while verificador:
    try:
      qtd_estoque = int(input("##### Quantidade em Estoque (NÚMERO INTEIRO): "))
      verificador = False
    except ValueError:
      print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
  print()
  verificador = True
  while verificador:
    try:
      valor_livro = float(input("##### Valor desse Livro (R$ -> NÚMERO DECIMAL): "))
      verificador = False
    except ValueError:
      print("'!!! Resposta não reconhecida como um número DECIMAL. Tente novamente !!!")
  ativo_prd = True
  produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque, valor_livro, ativo_prd] # Dados sendo guardados dentro do Dicionário produtos, onde o indeteficador daquele dado será o código do Produto, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print()
  print("Produto cadastrado com sucesso!")
  print()
  input("Tecle <ENTER> para continuar...")
  #-----------------------------------------------


#################################################
#####          EXIBIR DADOS PRODUTO         #####
#################################################

def exibir_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados do Produto     #####")
    print("############################################")
    print("##### 0 - Retornar ao Menu Estoque     #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_produto = int(input("##### Digite o Código do Produto: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if (code_produto in produtos) and (produtos[code_produto][8]):
      print()
      print("##########################################################################################################################################################################")
      print("####################################################################    Dados do Produto    ##############################################################################")
      print("##########################################################################################################################################################################")
      print("|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
      print("|              Nome do Livro                  |                Descrição                 |                  Autor                  |  Ano  | Tp.Cp. | Gên. | Qtd.|   R$  |")
      print("|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
      print("| %-43s "%(produtos[code_produto][0]), end="") # 1
      print("| %-40s "%(produtos[code_produto][1]), end="") # 2
      print("| %-39s "%(produtos[code_produto][2]), end="") # 3
      print("| %-5s "%(produtos[code_produto][3]), end="")  # 4
      print("| %-6s "%(produtos[code_produto][4]), end="")  # 5
      print("| %-4s "%(produtos[code_produto][5]), end="")  # 6
      print("| %-3s "%(produtos[code_produto][6]), end="")  # 7
      print("| %-5s "%(produtos[code_produto][7]))          # 8
      print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      print()
    else:
      print("Produto inexiste ou deletado!")
      print()
    resp = input("tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes:  ")
  print()
  #-----------------------------------------------


#################################################
#####         ALTERAR DADOS PRODUTO         #####
#################################################

def alterar_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####     Alterar Dados do Produto     #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_produto = int(input("##### Digite o Código do Produto: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  verificador = True
  while verificador:
    os.system('celar || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_produto in produtos) and (produtos[code_produto][8]):
      print()
      print("##########################################################################################################################################################################")
      print("####################################################################    Dados do Produto    ##############################################################################")
      print("####################################################################    0 - Para Cancelar   ##############################################################################")
      print("##########################################################################################################################################################################")
      print("|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
      print("|              Nome do Livro                  |                Descrição                 |                  Autor                  |  Ano  | Tp.Cp. | Gên. | Qtd.|   R$  |")
      print("|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
      print("| %-43s "%(produtos[code_produto][0]), end="") # 1
      print("| %-40s "%(produtos[code_produto][1]), end="") # 2
      print("| %-39s "%(produtos[code_produto][2]), end="") # 3
      print("| %-5s "%(produtos[code_produto][3]), end="")  # 4
      print("| %-6s "%(produtos[code_produto][4]), end="")  # 5
      print("| %-4s "%(produtos[code_produto][5]), end="")  # 6
      print("| %-3s "%(produtos[code_produto][6]), end="")  # 7
      print("| %-5s "%(produtos[code_produto][7]))          # 8
      print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      print()
      resp = input("#### Qual dado deseja alterar (0 Para Cancelar)? ")
      resp = resp.upper()
      print()
      ativo_prd = True
      produtos[code_produto][8] = ativo_prd
      if (resp == "NOME") or (resp == "NOME DO LIVRO") or (resp == "LIVRO"):
        nome_livro = input("##### Digite o novo nome do Livro: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        produtos[code_produto][0] = nome_livro
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "DESCRIÇÃO"):
        descricao = input("##### Digite a nova descrição: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        produtos[code_produto][1] = descricao
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "AUTOR"):
        autor = input("##### Digite o novo nome do Autor: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        produtos[code_produto][2] = autor
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "ANO"):
        ano = input("##### Digite o novo ano deste livro: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        produtos[code_produto][3] = ano
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "TIPO DE CAPA") or (resp == "CAPA"):
        tipo_capa = input("##### Digite o novo tipo de capa: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        produtos[code_produto][4] = tipo_capa
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "GENERO") or (resp == "GÊNERO") or (resp == "GÊNERO TEXTUAL"):
        print("###########################")
        print("##### GÊNERO TEXTUTAL #####")
        print("###########################")
        print("| 1 - Ação \n| 2 - Ficção \n| 3 - Suspense \n| 4 - Educativo \n| 5 - Infantil \n| 6 - Recreativo \n| 7 - Romance \n| 8 - Amplo")
        print()
        verificador = True
        while verificador:
          try:
            genero = int(input("##### Digite o novo tipo de Gênero (NÚMERO INTEIRO): "))
            print("Dado alterado com sucesso!")
            print("--------------------------")
            produtos[code_produto][5] = genero
            verificador = False
          except ValueError:
            print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
        print()
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "QUANTIDADE EM ESTOQUE") or (resp == "QUANTIDADE") or (resp == "ESSTOQUE"):
        verificador = True
        while verificador:
          try:
            qtd_estoque = int(input("##### Quantidade em Estoque (NÚMERO INTEIRO): "))
            print("Dado alterado com sucesso!")
            print("--------------------------")
            produtos[code_produto][6] = qtd_estoque
            verificador = False
          except ValueError:
            print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
        print()
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True 
      elif (resp == "R$") or (resp == "VALOR") or (resp == "VALOR DO LIVRO"):
        verificador = True
        while verificador:
          try:
            valor_livro = float(input("##### Valor desse Livro (R$ -> NÚMERO DECIMAL): "))
            print("Dado alterado com sucesso!")
            print("--------------------------")
            produtos[code_produto][7] = valor_livro
            verificador = False
          except ValueError:
            print("!!! Resposta não reconheicda como um número DECIMAL. Tente novamente !!!")
          print()
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "0"):
        print("Alteração Cancelada!")
        verificador = False 
    else:
      print()
      print("Produto inexistente ou deletado!")
      verificador = False
    print()
  input("Tecle <ENTER> para continuar...")
  #-----------------------------------------------


#################################################
#####         EXCLUIR DADOS PRODUTO         #####
#################################################

def excluir_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####          Excluir Produto         #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_produto = int(input("##### Digite o Código do Produto: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  if (code_produto in produtos) and (produtos[code_produto][8]):
    print()
    print("##########################################################################################################################################################################")
    print("####################################################################    Dados do Produto    ##############################################################################")
    print("##########################################################################################################################################################################")
    print("|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
    print("|              Nome do Livro                  |                Descrição                 |                  Autor                  |  Ano  | Tp.Cp. | Gên. | Qtd.|   R$  |")
    print("|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
    print("| %-43s "%(produtos[code_produto][0]), end="") # 1
    print("| %-40s "%(produtos[code_produto][1]), end="") # 2
    print("| %-39s "%(produtos[code_produto][2]), end="") # 3
    print("| %-5s "%(produtos[code_produto][3]), end="")  # 4
    print("| %-6s "%(produtos[code_produto][4]), end="")  # 5
    print("| %-4s "%(produtos[code_produto][5]), end="")  # 6
    print("| %-3s "%(produtos[code_produto][6]), end="")  # 7
    print("| %-5s "%(produtos[code_produto][7]))          # 8
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    decisao = input("Tem certeza que deseja EXCLUIR esse Produto (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      '''
      Para não acontecer de, ser excluido um produto de cód 2, exemplo, e quando for cadastrar outro produto, esse produto não pegar
      o mesmo cód que foi excluido, deixando um pouco bagunçado... Cada produto fica com um ativo em seus dados, estiver on = True, for excluído, ativo = False -> Assim, o cód_produto é unico e não se repete! 
      
      '''
      produtos[code_produto][7] = False
      print("Produto excluído com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Produto inexistente ou deletado!")
    verificador = False
    print()
  print()
  input("Tecle <ENTER> para continuar...")
#-----------------------------------------------


#################################################
#####         RELATÓRIO DE PRODUTOS         #####
#################################################

def relatorio_estoque_on():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("################################################################################################################################################################################")
  print("#################################################################     Relatório de Produtos     ################################################################################")
  print("################################################################################################################################################################################")
  print("|-----|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
  print("| Cod |              Nome do Livro                  |                Descrição                 |                  Autor                  |  Ano  | Tp.Cp. | Gên. | Qtd.|   R$  |")
  print("|-----|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
  for code_produto in produtos:
    if produtos[code_produto][8]:
      print("| %-3s "%(code_produto), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(produtos[code_produto][0]), end="") # 2
      print("| %-40s "%(produtos[code_produto][1]), end="") # 3
      print("| %-39s "%(produtos[code_produto][2]), end="") # 4
      print("| %-5s "%(produtos[code_produto][3]), end="")  # 5
      print("| %-6s "%(produtos[code_produto][4]), end="")  # 6
      print("| %-4s "%(produtos[code_produto][5]), end="")  # 7
      print("| %-3s "%(produtos[code_produto][6]), end="")  # 8
      print("| %-5s "%(produtos[code_produto][7]))          # 9
  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------


#######################################################
#####       RELATÓRIO DE PRODUTOS DELETADOS       #####
#######################################################

def relatorio_estoque_off():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("################################################################################################################################################################################")
  print("##########################################################       Relatório de Produtos Deletados       #########################################################################")
  print("################################################################################################################################################################################")
  print("|-----|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
  print("| Cod |              Nome do Livro                  |                Descrição                 |                  Autor                  |  Ano  | Tp.Cp. | Gên. | Qtd.|   R$  |")
  print("|-----|---------------------------------------------|------------------------------------------|-----------------------------------------|-------|--------|------|-----|-------|")
  for code_produto in produtos:
    if produtos[code_produto][8] == False:
      print("| %-3s "%(code_produto), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(produtos[code_produto][0]), end="") # 2
      print("| %-40s "%(produtos[code_produto][1]), end="") # 3
      print("| %-39s "%(produtos[code_produto][2]), end="") # 4
      print("| %-5s "%(produtos[code_produto][3]), end="")  # 5
      print("| %-6s "%(produtos[code_produto][4]), end="")  # 6
      print("| %-4s "%(produtos[code_produto][5]), end="")  # 7
      print("| %-3s "%(produtos[code_produto][6]), end="")  # 8
      print("| %-5s "%(produtos[code_produto][7]))          # 9
  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------


###################################################
#####        SALVANDO DADOS - PRODUTOS        #####
###################################################

def salvar_dados_produtos():
  arq_produtos = open("produtos.dat", "wb")
  pickle.dump(produtos, arq_produtos)
  arq_produtos.close()