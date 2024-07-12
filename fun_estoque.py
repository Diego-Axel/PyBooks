'''Arquivo das Funções do ESTOQUE'''

'''imports'''
import len_estoque
import interfaces
import pickle
import os
import time

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
  print("#####       <ENTER> - Prosseguir       #####")
  print("#####           0 - Cancelar           #####")
  print("############################################")
  print()
  confirmacao = input("Entrando em 'Cadastro de Produto' -> Digite '0' Para Cancelar e <ENTER> para prosseguir: ")
  if confirmacao == "0":
    return
  else:
    print("Iniciando cadastro.")
    time.sleep(3)
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Produto         #####")
  print("############################################")
  print()
  code_produto = len(produtos) + 1
  print()
  nome_livro = len_estoque.ler_nome()
  print()
  descricao = len_estoque.ler_descricao()
  print()
  autor = len_estoque.ler_autor()
  print()
  ano = len_estoque.ler_ano()
  print()
  tipo_capa = len_estoque.ler_capa()
  print()
  genero = len_estoque.ler_genero()
  print()
  qtd_estoque = len_estoque.ler_qtd()
  print()
  valor_livro = len_estoque.ler_valor()
  print()
  ativo_prd = True
  produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque, valor_livro, ativo_prd] # Dados sendo guardados dentro do Dicionário produtos, onde o indeteficador daquele dado será o código do Produto, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print(f"Produto cadastrado com sucesso sob código: {code_produto}")
  print()
  input("Tecle <ENTER> para continuar...")
  #-----------------------------------------------


#########################################################
#####           CADASTRAR PRODUTO NA VENDA          #####
#########################################################

def cadastrar_produto_venda(): # Estou usando essa função no meu arquivo de vendas, para cadastro de produto se o mesmo não possuir cadastro
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Produto         #####")
  print("############################################")
  print()
  code_produto = len(produtos) + 1
  print()
  nome_livro = len_estoque.ler_nome()
  print()
  descricao = len_estoque.ler_descricao()
  print()
  autor = len_estoque.ler_autor()
  print()
  ano = len_estoque.ler_ano()
  print()
  tipo_capa = len_estoque.ler_capa()
  print()
  genero = len_estoque.ler_genero()
  print()
  qtd_estoque = len_estoque.ler_qtd()
  print()
  valor_livro = len_estoque.ler_valor()
  print()
  ativo_prd = True
  produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque, valor_livro, ativo_prd] # Dados sendo guardados dentro do Dicionário produtos, onde o indeteficador daquele dado será o código do Produto, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print()
  print(f"Produto cadastrado com sucesso sob código: {code_produto}")
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
    print("#####         0 - Para Retornar        #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_produto = int(input("##### Digite o Código do Produto ou Digite '0' Para Retornar: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if code_produto == 0:
      return
    if (code_produto in produtos) and (produtos[code_produto][8]):
      print()
      interfaces.tabela_produto()
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
  print("#####         0 - Para Retornar        #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_produto = int(input("##### Digite o Código do Produto ou Digite '0' Para Retornar: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  if code_produto == 0:
    return
  verificador = True
  while verificador:
    os.system('celar || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_produto in produtos) and (produtos[code_produto][8]):
      print()
      interfaces.tabela_alteracao_produtos()
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
        nome_livro = len_estoque.ler_nome()
        produtos[code_produto][0] = nome_livro
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "DESCRIÇÃO"):
        descricao = len_estoque.ler_descricao()
        produtos[code_produto][1] = descricao
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "AUTOR"):
        autor = len_estoque.ler_autor()
        produtos[code_produto][2] = autor
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "ANO"):
        ano = len_estoque.ler_ano()
        produtos[code_produto][3] = ano
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "TIPO DE CAPA") or (resp == "CAPA"):
        tipo_capa = len_estoque.ler_capa()
        produtos[code_produto][4] = tipo_capa
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "GENERO") or (resp == "GÊNERO") or (resp == "GÊNERO TEXTUAL"):
        genero = len_estoque.ler_genero()
        produtos[code_produto][5] = genero
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "QUANTIDADE EM ESTOQUE") or (resp == "QUANTIDADE") or (resp == "ESSTOQUE"):
        qtd_estoque = len_estoque.ler_qtd()
        produtos[code_produto][6] = qtd_estoque
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "R$") or (resp == "VALOR") or (resp == "VALOR DO LIVRO"):
        valor_livro = len_estoque.ler_valor()
        produtos[code_produto][7] = valor_livro    
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()   
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
  print("#####         0 - Para Retornar        #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_produto = int(input("##### Digite o Código do Produto ou Digite '0' Para Retornar: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  if code_produto == 0:
    return
  if (code_produto in produtos) and (produtos[code_produto][8]):
    print()
    interfaces.tabela_produto()
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
      produtos[code_produto][8] = False
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
  interfaces.tabela_relatorio_produtos_atv()
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
  interfaces.tabela_relatorio_produtos_intv()
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