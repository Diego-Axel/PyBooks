# imports
import os
import datetime
import re
import pickle

# Pega a data Atual ->
data = datetime.date.today()
dia = data.day
mes = data.month
ano = data.year



################################################################
################################################################
##########                DICIONARIOS                 ##########
################################################################
################################################################

clientes = {}
try:
  arq_clientes = open("clientes.dat", "rb")
  clientes = pickle.load(arq_clientes)
except:
  arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()

produtos = {}
try:
  arq_produtos = open("produtos.dat", "rb")
  produtos = pickle.load(arq_produtos)
except:
  arq_produtos = open("produtos.dat", "wb")
arq_produtos.close()


vendas = {}
try:
  arq_vendas = open("vendas.dat", "rb")
  vendas = pickle.load(arq_vendas)
except:
  arq_vendas = open("vendas.dat", "wb")
arq_vendas.close()

################################################################
################################################################
##########               VERIFICADORES                ##########
################################################################
################################################################


def validar_email(email): # Função para verificar se o e-mail é válido (GPT)
  padrao = re.compile(r'^[\w-]+@[a-z\d]+\.[\w]{2,3}$')
  return padrao.match(email) is not None


def validar_numero(numero): # Função para validar telefone (GPT)
  padrao = re.compile(r'^\(\d{2}\) \d{4,5}-\d{4}$')
  return padrao.match(numero) is not None


################################################################
################################################################
##########               F U N Ç Õ E S                ##########
################################################################
################################################################



def menu_principal(): # Funcão do Menu Principal
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("""
        
       _ _                  _      
      | (_)_ ___ _ __ _ _ _(_)__ _ 
      | | \ V / '_/ _` | '_| / _` |
      |_|_|\_/|_| \__,_|_| |_\__,_|   
  
         .--.                   .---.   
     .---|__|           .-.     |~~~|   
  .--|===|--|_          |_|     |~~~|--.
  |  |===|  |'\     .---!~|  .--|   |--|
  |==|   |  |.'\    |===| |--|==|   |  |
  |==|   |  |\.'\   |   | |__|  |   |  |
  |  |   |  | \  \  |===| |==|  |   |  |
  |  |   |__|  \.'\ |   |_|__|  |~~~|__|
  |  |===|--|   \.'\|===|~|--|==|~~~|--|
  ^--^---'--^    `-'`---^-^--^--^---'--'

  """)

  print("############################################")
  print("######  Sistema de Gestão - Livraria  ######")
  print("############################################")
  print("#####      1 - Módulo Clientes         #####")
  print("#####      2 - Módulo Estoque          #####")
  print("#####      3 - Módulo Vendas           #####")
  print("#####      4 - Módulo Relatório        #####")
  print("#####      5 - Módulo Informações      #####")
  print("#####      0 - Sair                    #####")
  print("############################################")
  print()
  op_princ = input("##### Escolha o Módulo Desejado: ")
  return op_princ


def menu_cliente(): # Função do Menu Clientes
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####   Você está no Módulo Clientes   #####")
  print("############################################")
  print("##### 1 - Cadastrar Cliente            #####")
  print("##### 2 - Exibir Dados do Cliente      #####")
  print("##### 3 - Alterar Dados do Cliente     #####")
  print("##### 4 - Excluir Cliente              #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  print("############################################")
  print()
  op_cliente = input("##### Escolha sua opção: ")
  return op_cliente


def cadastrar_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Cliente         #####")
  print("############################################")
  print()
  code_cliente = len(clientes) + 1
  nome_cliente = input("##### Nome: ")
  print()
  verificador = True # Maneira de usar while atraves de variaveis que guardam operadoes lógicos, dica de Matheus Diniz.
  while verificador:
    email = input("#### E-mail: ")
    if validar_email(email):
      print("E-mail válido!")
      verificador = False
    else:
      print("O e-mail não é válido. Por favor digite novamente.")
      print()
  print()
  verificador = True
  while verificador:
    print("##### Digite o Celular com DDD e o 9 adicional seguinddo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
    celular = input("##### Digite seu Celular: ")
    if validar_numero(celular):
      print("Numero válido!")
      verificador = False
    else:
      print("Número não válido. Digite um número válido.")
  print()
  cpf = input("##### CPF: ")
  print()
  ativo = True
  clientes[code_cliente] = [nome_cliente, email, celular, cpf, ativo]
  print()
  print("Cliente cadastrado com sucesso!")
  print()
  input("Tecle <ENTER> para continuar...")


def exibir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados do Cliente     #####")
    print("############################################")
    print("##### 0 - Retornar ao Menu Clientes    #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_cliente = int(input("##### Digite o Código do Cliente: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if (code_cliente in clientes) and (clientes[code_cliente][4]):
      print()
      print("##### Nome: ",clientes[code_cliente][0])
      print("##### E-mail: ",clientes[code_cliente][1])
      print("##### Celular: ",clientes[code_cliente][2])
      print("##### CPF: ",clientes[code_cliente][3])
      print()
    else:
        print("Cliente inexistente ou inativo!")
        print()
    resp = input("Deseja continuar (tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes)? ")
  print()


def alterar_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####     Alterar Dados do Cliente     #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_cliente = int(input("##### Digite o Código do Cliente: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  verificador = True
  while verificador:
    os.system('celar || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_cliente in clientes) and (clientes[code_cliente][4]):
      print()
      print("###########################################")
      print("######     Dados Atuais do Cliente    #####")
      print("###########################################")
      print("##### 0 - Cancelar e Retornar         #####")
      print("###########################################")
      print()
      print("##### Nome: ",clientes[code_cliente][0])
      print("##### E-mail: ",clientes[code_cliente][1])
      print("##### Celular: ",clientes[code_cliente][2])
      print("##### CPF: ",clientes[code_cliente][3])
      print()        
      resp = input("#### Qual dado deseja alterar (0 Para Cancelar)? ")
      resp = resp.upper()
      print()
      ativo = True
      clientes[code_cliente][4] = ativo
      if (resp == "NOME"):
        nome_cliente = input("##### Digite o novo nome: ")
        clientes[code_cliente][0] = nome_cliente
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "E-MAIL") or (resp == "EMAIL"):
        verificador = True
        while verificador:
          email = input("##### Digite o novo e-mail: ")
          if validar_email(email):
            print("E-mail válido e alterado com sucesso!")
            print("-------------------------------------")
            print()
            clientes[code_cliente][1] = email
            verificador = False
          else:
            print("O e-mail não é válido. Por favor digite novamente.")
            print()
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "CELULAR") or (resp == "TELEFONE"):
        verificador = True
        while verificador:
          print("##### Digite o novo, lembre-se Celular com DDD e o 9 adicional seguinddo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
          celular = input("##### Novo Celular: ")
          if validar_numero(celular):
            print("Número válido e alterado com sucesso!")
            print("-------------------------------------")
            clientes[code_cliente][2] = celular
            verificador = False
          else:
            print("Número não válido. Digite um número válido.")
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "CPF"):
        cpf = input("##### Digite o novo CPF: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        clientes[code_cliente][3] = cpf
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
      print("Cliente inexistente ou inativo!")   
      verificador = False
  print()
  input("Tecle <ENTER> para continuar...")


def excluir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####          Excluir Cliente         #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_cliente = int(input("##### Digite o Código do Cliente: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  if (code_cliente in clientes) and (clientes[code_cliente][4]):
    print()
    print("##### Nome: ",clientes[code_cliente][0])
    print("##### E-mail: ",clientes[code_cliente][1])
    print("##### Celular: ",clientes[code_cliente][2])
    print("##### CPF: ",clientes[code_cliente][3])
    print()
    decisao = input("Tem certeza que deseja EXCLUIR esse Cliente (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      clientes[code_cliente][4] = False
      print("Cliente excluído(a) com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Cliente inexistente ou inativo!")
    print()
  input("Tecle <ENTER> para continuar...")  


def menu_estoque(): # Função do Menu de Estoque
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####    Você está no Módulo Estoque   #####")
  print("############################################")
  print("##### 1 - Cadastrar Produto            #####")
  print("##### 2 - Exibir Dados do Produto      #####")
  print("##### 3 - Alterar Dados do Produto     #####")
  print("##### 4 - Excluir Produto              #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  print("############################################")
  print()
  op_estoque = input("##### Escolha sua opção: ")
  return op_estoque


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
  print("| 1 - Ação \n| 2 - Ficção \n| 3 - Suspense \n| 4 - Educativo \n| 5 - Infantil \n| 6 - Recreativo \n| 7 - Amplo")
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
  ativo_prd = True
  print()
  produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque, ativo_prd]
  print()
  print("Produto cadastrado com sucesso!")
  print()
  input("Tecle <ENTER> para continuar...")


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
    if (code_produto in produtos) and (produtos[code_produto][7]):
      print()
      print("##### Nome do Livro: ",produtos[code_produto][0])
      print("##### Descrição: ",produtos[code_produto][1])
      print("##### Autor: ",produtos[code_produto][2])
      print("##### Ano: ",produtos[code_produto][3])
      print("##### Tipo de Capa: ",produtos[code_produto][4])
      print("##### Gênero: ", produtos[code_produto][5])
      print("##### Quantidade Em Estoque: ",produtos[code_produto][6])
      print()
    else:
      print("Produto inexiste ou deletado!")
      print()
    resp = input("Deseja continuar (tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes)? ")
  print()
 

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
    if (code_produto in produtos) and (produtos[code_produto][7]):
      print()
      print("###########################################")
      print("######    Dados Atuais do Produto     #####")
      print("###########################################")
      print("##### 0 - Cancelar e Retornar         #####")
      print("###########################################")
      print()
      print("##### Nome do Livro: ",produtos[code_produto][0])
      print("##### Descrição: ",produtos[code_produto][1])
      print("##### Autor: ",produtos[code_produto][2])
      print("##### Ano: ",produtos[code_produto][3])
      print("##### Tipo de Capa: ",produtos[code_produto][4])
      print("##### Gênero: ", produtos[code_produto][5])
      print("##### Quantidade Em Estoque: ",produtos[code_produto][6])
      print()
      resp = input("#### Qual dado deseja alterar (0 Para Cancelar)? ")
      resp = resp.upper()
      print()
      ativo_prd = True
      produtos[code_produto][7] = ativo_prd
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
        print("| 1 - Ação \n| 2 - Ficção \n| 3 - Suspense \n| 4 - Educativo \n| 5 - Infantil \n| 6 - Recreativo \n| 7 - Amplo")
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
      elif (resp == "0"):
        print("Alteração Cancelada!")
        verificador = False 
    else:
      print()
      print("Produto inexistente ou deletado!")
    print()
  input("Tecle <ENTER> para continuar...")


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
  if (code_produto in produtos) and (produtos[code_produto][7]):
    print()
    print("##### Nome do Livro: ",produtos[code_produto][0])
    print("##### Descrição: ",produtos[code_produto][1])
    print("##### Autor: ",produtos[code_produto][2])
    print("##### Ano: ",produtos[code_produto][3])
    print("##### Tipo de Capa: ",produtos[code_produto][4])
    print("##### Gênero: ", produtos[code_produto][5])
    print("##### Quantidade Em Estoque: ",produtos[code_produto][6])
    print()
    decisao = input("Tem certeza que deseja EXCLUIR esse Produto (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      produtos[code_produto][7] = False
      print("Produto excluído com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Produto inexistente ou deletado!")
    verificador = False
    print()
  input("Tecle <ENTER> para continuar...")


def menu_vendas(): # Função do Menu de Vendas
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("#############################################")
  print("#####    Você está no Módulo Vendas     #####")
  print("#############################################")
  print("##### 1 - Cadastrar uma Venda           #####")
  print("##### 2 - Exibir Dados de Venda         #####")
  print("##### 3 - Alterar Dados de Venda        #####")
  print("##### 4 - Excluir Venda                 #####")
  print("##### 0 - Retornar ao Menu Principal    #####")
  print("#############################################")
  print()
  op_vendas = input("##### Escolha sua opção: ")
  return op_vendas


def cadastrar_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("############################################")
  print("#####         Cadastrar Venda          #####")
  print("############################################")
  print()
  code_venda = len(vendas) + 1
  data_venda = ("%02d/%02d/%d"%(dia, mes, ano))
  print()
  nome_cliente_venda = input("##### Nome do Cliente: ")
  print()
  livro_comprado = input("##### Nome do Livro Comprado: ")
  print()
  verificador = True
  while verificador:
    try:
      unidades = int(input("##### Unidades Vendidas (NÚMERO INTEIRO): "))
      verificador = False
    except ValueError:
      print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
  print()
  verificador = True
  while verificador:
    try:
      valor = float(input("##### Valor de Venda (R$ -> DECIMAL): "))
      verificador = False
    except ValueError:
      print("!!! Resposta não reconhecida como número DECIMAL(R$). Tente novamente !!!")
  print()
  forma_pgto = input("##### Forma de pagamento: ")
  ativo_venda = True
  print()
  vendas[code_venda] = [data_venda, nome_cliente_venda, livro_comprado, unidades, valor, forma_pgto, ativo_venda]
  print()
  print("Venda cadastrada com sucesso!")
  print()
  input("Tecle <ENTER> para continuar...")


def exibir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados do Vendas      #####")
    print("############################################")
    print("##### 0 - Retornar ao Menu Vendas     #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_venda = int(input("##### Digite o Código de Venda: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if (code_venda in vendas) and (vendas[code_venda][6]):
      print()
      print("##### Data de venda: ",vendas[code_venda][0])
      print("##### Nome do Cliente: ",vendas[code_venda][1])
      print("##### Livro Comprado: ",vendas[code_venda][2])
      print("##### Unidades Vendias: ",vendas[code_venda][3])
      print("##### Valor R$ da Venda",vendas[code_venda][4])
      print("##### Forma de Pagamento: ",vendas[code_venda][5])
      print()
    else:
      print()
      print("Venda inexistente ou deletada!")
      print()
    resp = input("Deseja continuar (tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes)? ")
  print()


def alterar_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####      Alterar Dados de Venda      #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_venda = int(input("##### Digite o Código da Venda: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  verificador = True
  while verificador:
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_venda in vendas) and (vendas[code_venda][6]):
      print()
      print("###########################################")
      print("######      Dados Atuais da Venda     #####")
      print("###########################################")
      print("##### 0 - Cancelar e Retornar         #####")
      print("###########################################")
      print()
      print("##### Data de venda: ",vendas[code_venda][0])
      print("##### Nome do Cliente: ",vendas[code_venda][1])
      print("##### Livro Comprado: ",vendas[code_venda][2])
      print("##### Unidades Vendias: ",vendas[code_venda][3])
      print("##### Valor R$ de Venda",vendas[code_venda][4])
      print("##### Forma de Pagamento: ",vendas[code_venda][5])
      print()
      resp = input("#### Qual dado deseja alterar? ")
      resp = resp.upper()
      print()
      ativo_venda = True
      vendas[code_venda][6] = ativo_venda
      if (resp == "DATA DE VENDA") or (resp == "DATA"):
        data_venda = ("%02d/%02d/%d"%(dia, mes, ano))
        print("Data modificada para o dia de hoje!")
        print("-----------------------------------")
        print()
        vendas[code_venda][0] = data_venda
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "NOME DO CLIENTE") or (resp == "NOME CLIENTE") or (resp == "CLIENTE"):    
        nome_cliente_venda = input("##### Digite o nome do Cliente: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        vendas[code_venda][1] = nome_cliente_venda
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "LIVRO COMPRADO") or (resp == "LIVRO") or (resp == "NOME DO LIVRO"):
        livro_comprado = input("##### Digite o nome do livro Comprado: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        vendas[code_venda][2] = livro_comprado
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "UNIDADES") or (resp == "UNIDADES ADQUIRIDAS") or (resp == "UNIDADES VENDIDAS"):
        verificador = True
        while verificador:
          try:
            unidades = int(input("##### Unidades Vendidas (NÚMERO INTEIRO): "))
            print("Dado alterado com sucesso!")
            print("--------------------------")
            vendas[code_venda][3] = unidades
            verificador = False
          except ValueError:
            print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "VALOR R$") or (resp == "VALOR DE VENDA") or (resp == "R$") or (resp == "VALOR"):
        verificador = True
        while verificador:
          try:
            valor = float(input("##### Valor de Venda (R$ -> DECIMAL): "))
            print("Dado alterado com sucesso!")
            print("--------------------------")
            print()
            vendas[code_venda][4] = valor
            verificador = False
          except ValueError:
            print("!!! Resposta não reconhecida como número DECIMAL(R$). Tente novamente !!!")
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "FORMA DE PAGAMENTO") or (resp == "PAGAMENTO"):
        forma_pgto = input("##### Digite a Forma de pagamento: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        vendas[code_venda][5] = forma_pgto
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
      print("Venda inexistente ou deletada!")
      verificador = False
    print()
  input("tecle <ENTER> para continuar...")


def excluir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####           Excluir Venda          #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_venda = int(input("##### Digite o Código da Venda: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  if (code_venda in vendas) and (vendas[code_venda][6]):
    print()
    print("##### Data de venda: ",vendas[code_venda][0])
    print("##### Nome do Cliente: ",vendas[code_venda][1])
    print("##### Livro Comprado: ",vendas[code_venda][2])
    print("##### Unidades Vendidas: ",vendas[code_venda][3])
    print("##### Valor R$ de Venda",vendas[code_venda][4])
    print("##### Forma de Pagamento: ",vendas[code_venda][5])
    print()
    decisao = input("Tem certeza que deseja EXCLUIR essa Venda (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      vendas[code_venda][6] = False
      print("Venda excluída com sucesso!")
      print()
  else:
    print("##### Venda inexistente ou deletada!")
    print()
  input("tecle <ENTER> para continuar...")


def menu_relatorio(): # Função do Menu dos Relatórios
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("#################################################")
  print("#####     Você está no Módulo Relatório     #####")
  print("#################################################")
  print("##### 1 - Ver Relatório de Clientes         #####")
  print("##### 2 - Ver Relatório de Estoque          #####")
  print("##### 3 - Ver Relatório de Vendas           #####")
  print("##### 0 - Retornar ao Menu Principal        #####")
  print("#################################################")
  print()
  op_relatorio = input("#### Escolha sua opção: ")
  return op_relatorio


def relatorio_clientes():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("#################################################")
    print("#####          Relatório de Clientes        #####")
    print("#################################################")
    print("##### 1 - Ver Clientes Ativos               #####")
    print("##### 2 - Ver Clientes Inativos             #####")
    print("##### 0 - Retornar ao Menu Relatório        #####")
    print("#################################################")
    print()
    resp = input("##### Escolha sua opção: ")
    if resp == "1":
      os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
      print()
      print("#############################################################################################################################")
      print("#######################################         Relatório de Clientes Ativos      ###########################################")
      print("#############################################################################################################################")
      print("|-------|---------------------------------------------|--------------------------|---------------------|--------------------|")
      print("|  Cod  |                Nome Completo                |          E-mail          |       Celular       |         CPF        |")
      print("|-------|---------------------------------------------|--------------------------|---------------------|--------------------|")
      for code_cliente in clientes:
        if clientes[code_cliente][4]:
          print("| %-5s "%(code_cliente), end='') # Para o %-5s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
          print("| %-43s "%(clientes[code_cliente][0]), end='') # 2
          print("| %-24s "%(clientes[code_cliente][1]), end='') # 3
          print("| %-19s "%(clientes[code_cliente][2]), end='') # 4
          print("| %-17s "%(clientes[code_cliente][3]))         # 5
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print()
      input("tecle <NETER> para continuar...")          
    elif resp == "2":
      os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
      print()
      print("#############################################################################################################################")
      print("#######################################         Relatório de Clientes Inativos      #########################################")
      print("#############################################################################################################################")
      print("|-------|---------------------------------------------|--------------------------|---------------------|--------------------|")
      print("|  Cod  |                Nome Completo                |          E-mail          |       Celular       |         CPF        |")
      print("|-------|---------------------------------------------|--------------------------|---------------------|--------------------|")
      for code_cliente in clientes:
        if clientes[code_cliente][4] == False:
          print("| %-5s "%(code_cliente), end='') # Para o %-5s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
          print("| %-43s "%(clientes[code_cliente][0]), end='') # 2
          print("| %-24s "%(clientes[code_cliente][1]), end='') # 3
          print("| %-19s "%(clientes[code_cliente][2]), end='') # 4
          print("| %-17s "%(clientes[code_cliente][3]))         # 5 
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print()
      input("tecle <NETER> para continuar...")          



def relatorio_estoque():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("#################################################")
    print("#####          Relatório de Estoque         #####")
    print("#################################################")
    print("##### 1 - Ver Produtos Em Estoque           #####")
    print("##### 2 - Ver Produtos Deletados            #####")
    print("##### 0 - Retornar ao Menu Relatório        #####")
    print("#################################################")
    print()
    resp = input("#### Escolha sua opção: ")
    if resp == "1":
      os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
      print()
      print("################################################################################################")
      print("########################        Relatório de Produtos em Estoque        ########################")
      print("################################################################################################")
      print("|-----|----------------------------------|--------------------|-------|--------|---------------|")
      print("| Cod |           Nome do Livro          |       Autor        |  Ano  | Gênero | Qtde. Estoque |")
      print("|-----|----------------------------------|--------------------|-------|--------|---------------|")
      for code_produto in produtos:
        if produtos[code_produto][7]:
          print("| %-3s "%(code_produto), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
          print("| %-32s "%(produtos[code_produto][0]), end="") # 2
          print("| %-18s "%(produtos[code_produto][2]), end="") # 3
          print("| %-5s "%(produtos[code_produto][3]), end="")  # 4
          print("| %-6s "%(produtos[code_produto][5]), end="")  # 5
          print("| %-13s "%(produtos[code_produto][6]))         # 6
      print("|-----------------------------------------------------------------------------------------------")
      print()
      input("tecle <ENTER> para continuar...")
    elif resp == "2":
      os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
      print()
      print("################################################################################################")
      print("########################        Relatório de Produtos Deletados         ########################")
      print("################################################################################################")
      print("|-----|----------------------------------|--------------------|-------|--------|---------------|")
      print("| Cod |           Nome do Livro          |       Autor        |  Ano  | Gênero | Qtde. Estoque |")
      print("|-----|----------------------------------|--------------------|-------|--------|---------------|")
      for code_produto in produtos:
        if produtos[code_produto][7] == False:
          print("| %-3s "%(code_produto), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
          print("| %-32s "%(produtos[code_produto][0]), end="") # 2
          print("| %-18s "%(produtos[code_produto][2]), end="") # 3
          print("| %-5s "%(produtos[code_produto][3]), end="")  # 4
          print("| %-6s "%(produtos[code_produto][5]), end="")  # 5
          print("| %-13s "%(produtos[code_produto][6]))         # 6
      print("|-----------------------------------------------------------------------------------------------")
      print()
      input("tecle <ENTER> para continuar...")



def relatorio_vendas():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("#################################################")
    print("#####          Relatório de Vendas          #####")
    print("#################################################")
    print("##### 1 - Ver Vendas                        #####")
    print("##### 2 - Ver Vendas Deletadas              #####")
    print("##### 0 - Retornar ao Menu Relatório        #####")
    print("#################################################")
    print()
    resp = input("##### Escolha sua opção: ")
    if resp == "1":
      os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
      print()
      print("#############################################################################################################################")
      print("#####################################              Relatório de Vendas          #############################################")
      print("#############################################################################################################################")
      print("|-----|---------------|--------------------------|----------------------------|----------|------------|---------------------|")
      print("| Cod | Data da Venda |      Nome do Cliente     |       Livro Comprado       | Unidades | Valor (R$) | Forma de Pagamaneto |")
      print("|-----|---------------|--------------------------|----------------------------|----------|------------|---------------------|")
      for code_venda in vendas:
        if vendas[code_venda][6]:
          print("| %-3s "%(code_venda), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
          print("| %-13s "%(vendas[code_venda][0]), end="") # 2
          print("| %-24s "%(vendas[code_venda][1]), end="") # 3
          print("| %-26s "%(vendas[code_venda][2]), end="") # 4
          print("| %-8s "%(vendas[code_venda][3]), end="")  # 5
          print("| %-10s "%(vendas[code_venda][4]), end="") # 6
          print("| %-19s "%(vendas[code_venda][5]))         # 7
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print()
      input("tecle <ENTER> para continuar...")
    elif resp == "2":
      os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
      print()
      print("#############################################################################################################################")
      print("#####################################       Relatório de Vendas Deletadas         ###########################################")
      print("#############################################################################################################################")
      print("|-----|---------------|--------------------------|----------------------------|----------|------------|---------------------|")
      print("| Cod | Data da Venda |      Nome do Cliente     |       Livro Comprado       | Unidades | Valor (R$) | Forma de Pagamaneto |")
      print("|-----|---------------|--------------------------|----------------------------|----------|------------|---------------------|")
      for code_venda in vendas:
        if vendas[code_venda][6] == False:
          print("| %-3s "%(code_venda), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
          print("| %-13s "%(vendas[code_venda][0]), end="") # 2
          print("| %-24s "%(vendas[code_venda][1]), end="") # 3
          print("| %-26s "%(vendas[code_venda][2]), end="") # 4
          print("| %-8s "%(vendas[code_venda][3]), end="")  # 5
          print("| %-10s "%(vendas[code_venda][4]), end="") # 6
          print("| %-19s "%(vendas[code_venda][5]))         # 7
      print("-----------------------------------------------------------------------------------------------------------------------------")
      print()
      input("tecle <ENTER> para continuar...")



def menu_informacao():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("#############################################")
  print("#####  Você está no Módulo Informações  #####")
  print("#############################################")
  print("##### Projeto de Gestão de uma Livraria #####")
  print("##### Desenvolvido por: Diêgo Axel      #####")
  print("##### Instagram: @diegoaxelbsr          #####")
  print("##### E-mail: diegoaxelbsr@gmail.com    #####")
  print("##### Telefone: 55 (84) 99977-4459      #####")
  print("##### Projeto do curso de: BSI  ->      #####")
  print("##### Sistemas de Informação - UFRN     #####")
  print("##### GitHub: Diego-Axel | Olha lá ;)   #####")
  print("#############################################")
  print()
  input("Tecle <ENTER> para retornar ao Menu Principal...")


def salvar_dados(): # Função para guardar os dados de CLIENTES, PRODUTOS e VENDAS
  # Gravando os dados no arquivo:
  arq_clientes = open("clientes.dat", "wb")
  pickle.dump(clientes, arq_clientes)
  arq_clientes.close()

  arq_produtos = open("produtos.dat", "wb")
  pickle.dump(produtos, arq_produtos)
  arq_produtos.close()

  arq_vendas = open("vendas.dat", "wb")
  pickle.dump(vendas, arq_vendas)
  arq_vendas.close()