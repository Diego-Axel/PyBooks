############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

# imports
import time
import os
import datetime
import re

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

# Dados para Testes

clientes = {
    1: ['Jaqueline', 'jaqueline@gmail.com', '(84)99977-2243', '123.321.123-33', True],
    2: ['Carlos', 'carlos@gmail.com', '(84)99977-5500', '123.321.123-11', True],
    3: ['Thomas Daniel', 'TDaniel@gmail.com', '(84)99911-0000', '123.321.123-07', True],
    4: ['Joaqum Dutra', 'joaquim@gmail.com', '(84)99911-0000', '123.321.123-07', False]
    
}

produtos = {
    1: ['Harry Potter', 'Um bruxinho que embarca em uma aventura cheia de fantasia.', 'Diego Axel', '2001', 'Dura', 2, 2, True],
    2: ['Clean Code', 'Livro para programadores que querem deixar seu código mais legível e limpo.', 'Flavius Gorgônio', '2005', 'Dura', 4, 6, False],
    3: ['Python Básico', 'Aprenda Python do Zero!', 'FULANO', '1999', 'Mole', 4, 10, True]
}

vendas = {
    1: [datetime.date(2024, 5, 1), 'Axel', 'Harry Potter', '4', 20.43, 'Cartão', True],
    2: [datetime.date(2024, 5, 1), 'Denise', 'Clean Code', '5', 15.67, 'Débito', True],
    3: [datetime.date(2024, 5, 1), 'Carlos', 'Jurassic Park', '1', 20.23, 'Dinheiro', False]
}



################################################################
################################################################
##########               VERIFICADORES                ##########
################################################################
################################################################


def validar_email(email): # Função para verificar se o e-mail é válido (GPT)
  padrao = re.compile(r'^[\w-]+@[a-z\d]+\.[\w]{2,3}$')
  return padrao.match(email) is not None


def validar_numero(numero):
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
  nome = input("##### Nome: ")
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
    print("##### Digite o Celular com DDD e o 9 adicional seguinddo este exemplo: (84) 99977-3321 (NÚMERO DE EXEMPLO)")
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
  clientes[code_cliente] = [nome, email, celular, cpf, ativo]
  print()
  print(clientes)
  print("Cliente cadastrado com sucesso!")
  print()
  input("Tecle <ENTER> para continuar...")


def exibir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####      Exibir Dados do Cliente     #####")
  print("############################################")
  print()
  code_cliente = int(input("##### Digite o Código do Cliente: "))
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
  input("Tecle <ENTER> para continuar...")


def alterar_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####     Alterar Dados do Cliente     #####")
  print("############################################")
  print()
  code_cliente = int(input("##### Digite o Código do Cliente: "))
  if (code_cliente in clientes) and (clientes[code_cliente][4]):
    print()
    print("###########################################")
    print("######    Dados Atuais do Cliente     #####")
    print("###########################################")
    print()
    print("##### Nome: ",clientes[code_cliente][0])
    print("##### E-mail: ",clientes[code_cliente][1])
    print("##### Celular: ",clientes[code_cliente][2])
    print("##### CPF: ",clientes[code_cliente][3])
    print()        
    print("##### Informe os novos dados do Cliente:")
    nome = input("##### Nome: ")
    print()
    verificador = True
    while verificador:
      email = input("##### E-mail: ")
      if validar_email(email):
        print("E-mail válido!")
        print()
        verificador = False
      else:
        print("O e-mail não é válido. Por favor digite novamente.")
        print()
    celular = input("##### Celular: ")
    print()
    cpf = input("##### CPF: ")
    print()
    ativo = True
    clientes[code_cliente] = [nome, email, celular, cpf, ativo]
  else:
    print()
    print("Cliente inexistente ou inativo!")   
  print()
  input("Tecle <ENTER> para continuar...")


def excluir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####          Excluir Cliente         #####")
  print("############################################")
  print()
  code_cliente = int(input("##### Digite o Código do Cliente: "))
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
  print(produtos)
  print("Produto cadastrado com sucesso!")
  print()
  input("Tecle <ENTER> para continuar...")


def exibir_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####      Exibir Dados do Produto     #####")
  print("############################################")
  print()
  code_produto = int(input("##### Digite o Código do Produto: "))
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
  input("Tecle <ENTER> para continuar...")
 

def alterar_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####     Alterar Dados do Produto     #####")
  print("############################################")
  print()
  code_produto = int(input("##### Digite o Código do Produto: "))
  if (code_produto in produtos) and (produtos[code_produto][7]):
    print()
    print("###########################################")
    print("######    Dados Atuais do Produto     #####")
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
    print("##### Informe os novos dados do Produto:")
    nome_livro = input("##### Nome do Livro: ")
    print()
    descricao = input("Descrição: ")
    print()
    autor = input("Autor: ")
    print()
    ano = input("Ano: ")
    print()
    tipo_capa = input("Tipo de Capa: ")
    print()
    print("###########################")
    print("##### GÊNERO TEXTUTAL #####")
    print("###########################")
    print("| 1 - Ação \n| 2 - Ficção \n| 3 - Suspense \n| 4 - Educativo \n| 5 - Infantil \n| 6 - Recreativo \n| 7 - Amplo")
    print()
    verificador = True
    while verificador:
      try:
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
    produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque, ativo_prd]
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
  code_produto = int(input("##### Digite o Código do Produto: "))
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
  nome_venda = input("##### Nome do Cliente: ")
  print()
  livro_comprado = input("##### Nome do Livro Comprado: ")
  print()
  verificador = True
  while verificador:
    try:
      unidades = int(input("##### Unidades Adquiridas (NÚMERO INTEIRO): "))
      verificador = False
    except ValueError:
      print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
  print()
  verificador = True
  while verificador:
    try:
      valor = float(input("##### Valor da compra (R$ -> DECIMAL): "))
      verificador = False
    except ValueError:
      print("!!! Resposta não reconhecida como número DECIMAL(R$). Tente novamente !!!")
  print()
  forma_pgto = input("##### Forma de pagamento: ")
  ativo_venda = True
  print()
  vendas[code_venda] = [data_venda, nome_venda, livro_comprado, unidades, valor, forma_pgto, ativo_venda]
  print(vendas)
  print()
  print("Venda cadastrada com sucesso!")
  print()
  input("Tecle <ENTER> para continuar...")


def exibir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####      Exibir Dados do Vendas      #####")
  print("############################################")
  print()
  code_venda = int(input("##### Digite o Código de Venda: "))
  if (code_venda in vendas) and (vendas[code_venda][6]):
    print()
    print("##### Data de venda: ",vendas[code_venda][0])
    print("##### Nome do Cliente: ",vendas[code_venda][1])
    print("##### Livro Comprado: ",vendas[code_venda][2])
    print("##### Unidades Adquiridas: ",vendas[code_venda][3])
    print("##### Valor R$",vendas[code_venda][4])
    print("##### Forma de Pagamento: ",vendas[code_venda][5])
    print()
  else:
    print()
    print("Venda inexistente ou deletada!")
    print()
  input("tecle <ENTER> para continuar...")


def alterar_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####      Alterar Dados de Venda      #####")
  print("############################################")
  print()
  code_venda = int(input("##### Digite o Código da Venda: "))
  if (code_venda in vendas) and (vendas[code_venda][6]):
    print()
    print("##### Data de venda: ",vendas[code_venda][0])
    print("##### Nome do Cliente: ",vendas[code_venda][1])
    print("##### Livro Comprado: ",vendas[code_venda][2])
    print("##### Unidades Adquiridas: ",vendas[code_venda][3])
    print("##### Valor R$",vendas[code_venda][4])
    print("##### Forma de Pagamento: ",vendas[code_venda][5])
    print()
    print("##### Informe os novos dados da Venda: ")
    print()
    data_venda = ("%02d/%02d/%d"%(dia, mes, ano))
    nome_venda = input("##### Nome do Cliente: ")
    print()
    livro_comprado = input("##### Livro Comprado: ")
    print()
    verificador = True
    while verificador:
      try: 
        unidades = int(input("##### Unidades Adquiridas (NÚMERO INTEIRO): "))
        verificador = False
      except ValueError:
        print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
    print()
    verificador = True
    while verificador:
      try:
        valor = float(input("##### Valor da compra (R$ -> DECIMAL): "))
        verificador = False
      except ValueError:
        print("!!! Resposta não reconhecida como número DECIMAL(R$). Tente novamente !!!")
    print()
    forma_pgto = input("##### Forma de Pagamento: ")
    print()
    ativo_venda = True
    vendas[code_venda] = [data_venda, nome_venda, livro_comprado, unidades, valor, forma_pgto, ativo_venda]
  else:
    print()
    print("Venda inexistente ou deletada!")
    print()
  input("tecle <ENTER> para continuar...")


def excluir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####           Excluir Venda          #####")
  print("############################################")
  print()
  code_venda = int(input("##### Digite o Código da Venda: "))
  if (code_venda in vendas) and (vendas[code_venda][6]):
    print()
    print("##### Data de venda: ",vendas[code_venda][0])
    print("##### Nome do Cliente: ",vendas[code_venda][1])
    print("##### Livro Comprado: ",vendas[code_venda][2])
    print("##### Unidades Adquiridas: ",vendas[code_venda][3])
    print("##### Valor R$",vendas[code_venda][4])
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
  print()
  print("#################################################")
  print("#####          Relatório de Clientes        #####")
  print("#################################################")
  print()
  print("---------------------------------------")
  for code_cliente in clientes:
    if clientes[code_cliente][4]:
      print("##### Código do Cliente: ",code_cliente)
      print("##### Nome: ",clientes[code_cliente][0])
      print("##### E-mail: ",clientes[code_cliente][1])
      print("##### Celular: ",clientes[code_cliente][2])
      print("##### CPF: ",clientes[code_cliente][3])
    else:
      print("################################")
      print("#####  CLIENTE NÃO ATIVO!  #####")
      print("################################")
      print("##### Código do Cliente: ",code_cliente)
      print("##### Nome: ",clientes[code_cliente][0])
      print("##### E-mail: ",clientes[code_cliente][1])
      print("##### Celular: ",clientes[code_cliente][2])
      print("##### CPF: ",clientes[code_cliente][3])
    print("---------------------------------------")
  input("tecle <ENTER> para continuar...")


def relatorio_estoque():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("#################################################")
  print("#####          Relatório de Estoque         #####")
  print("#################################################")
  print()
  print("-----------------------------------------------------------------------")
  for code_produto in produtos:
    if produtos[code_produto][7]:
      print("##### Código do Produto: ",code_produto)
      print("##### Nome do Livro: ",produtos[code_produto][0])
      print("##### Descrição: ",produtos[code_produto][1])
      print("##### Autor: ",produtos[code_produto][2])
      print("##### Ano: ",produtos[code_produto][3])
      print("##### Tipo de Capa: ",produtos[code_produto][4])
      print("##### Gênero: ", produtos[code_produto][5])
      print("##### Quantidade Em Estoque: ",produtos[code_produto][6])
    else:
        print("################################")
        print("#####   PRODUTO DELETADO   #####")
        print("################################")
        print("##### Nome do Livro: ",produtos[code_produto][0])
        print("##### Descrição: ",produtos[code_produto][1])
        print("##### Autor: ",produtos[code_produto][2])
        print("##### Ano: ",produtos[code_produto][3])
        print("##### Tipo de Capa: ",produtos[code_produto][4])
        print("##### Gênero: ", produtos[code_produto][5])
        print("##### Quantidade Em Estoque: ",produtos[code_produto][6])
    print("-----------------------------------------------------------------------")
  input("tecle <ENTER> para continuar...")  


def relatorio_vendas():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("#################################################")
  print("#####          Relatório de Vendas          #####")
  print("#################################################")
  print()
  print("-------------------------------------")
  for code_venda in vendas:
    if vendas[code_venda][6]:
      print("##### Código de Venda: ",code_venda)
      print("##### Data de venda: ",vendas[code_venda][0])
      print("##### Nome do Cliente: ",vendas[code_venda][1])
      print("##### Livro Comprado: ",vendas[code_venda][2])
      print("##### Unidades Adquiridas: ",vendas[code_venda][3])
      print("##### Valor R$",vendas[code_venda][4])
      print("##### Forma de Pagamento: ",vendas[code_venda][5])
    else:
        print("################################")
        print("#####    VENDA DELETADA    #####")
        print("################################")
        print("##### Código de Venda: ",code_venda)
        print("##### Data de venda: ",vendas[code_venda][0])
        print("##### Nome do Cliente: ",vendas[code_venda][1])
        print("##### Livro Comprado: ",vendas[code_venda][2])
        print("##### Unidades Adquiridas: ",vendas[code_venda][3])
        print("##### Valor R$",vendas[code_venda][4])
        print("##### Forma de Pagamento: ",vendas[code_venda][5])
    print("-------------------------------------")
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


# Programa Principal

op_princ = ""
while op_princ != "0":
  op_princ = menu_principal()
  print()
  if op_princ == "1":
    op_cliente = ""
    while op_cliente != "0":
      op_cliente = menu_cliente()
      print()
      if op_cliente == "1":
        cadastrar_cliente()
      elif op_cliente == "2":
        exibir_cliente()
      elif op_cliente == "3":
        alterar_cliente()
      elif op_cliente == "4":
        excluir_cliente()
  elif op_princ == "2":
    op_estoque = ""
    while op_estoque != "0":
      op_estoque = menu_estoque()
      print()
      if op_estoque == "1":
        cadastrar_produto()
      elif op_estoque == "2":
        exibir_produto()
      elif op_estoque == "3":
        alterar_produto()
      elif op_estoque == "4":
        excluir_produto()
  elif op_princ == "3":
    op_vendas = ""
    while op_vendas != "0":
      op_vendas = menu_vendas()
      print()
      if op_vendas == "1":
        cadastrar_venda()
      elif op_vendas == "2":
        exibir_venda()
      elif op_vendas == "3":
        alterar_venda()
      elif op_vendas == "4":
        excluir_venda()
  elif op_princ == "4":
    op_relatorio = ""
    while op_relatorio != "0":
      op_relatorio = menu_relatorio()
      print()
      if op_relatorio == "1":
        relatorio_clientes()
      elif op_relatorio == "2":
        relatorio_estoque()
      elif op_relatorio == "3":
        relatorio_vendas()
  elif op_princ == "5":
    menu_informacao()

os.system('claer || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
print()
print("Programa encerrado.")
print()
print("""
  ___                         _     _    _                      _   ___  _                  _           _ 
 |   \ ___ ______ _ ___ _____| |_ ___)__| |___   _ __ ___ _ _  (_) |   \(_)___ __ _ ___    /_\ __ _____| |
 | |) / -_)_-< -_) ' \ V / _ \ \ V / / _` / _ \ | '_ \ _ \ '_|  _  | |) | / -_) _` / _ \  / _ \ \ \ /-_) |
 |___/\___/__\___|_||_\_/\___/_|\_/|_\__,_\___/ | .__\___/_|   (_) |___/|_\___\__, \___/ /_/ \_\_\_\___|_|
                                                |_|                           |___/                       
                                             ______________         
                                            ||            ||        
                                            ||            ||        
                                            ||    < / >   ||        
                                            ||            ||        
                                            ||____________||        
                                            |______________|        
                                            \  ############ \       
                                             \  ############ \      
                                              \      ____     \     
                                               \_____\___\____ \        
                                             
  """)    
# ASCCI(s) feitas no site: https://ascii-art.botecodigital.dev.br/  ;)

# def validar_telefone(numero): Função para validar telefone (GPT)
#     # Regex para validar um número de telefone brasileiro
#     # Formato esperado: (xx) xxxxx-xxxx ou (xx) xxxx-xxxx
#     padrao = re.compile(r'^\(\d{2}\) \d{4,5}-\d{4}$')
#     return padrao.match(numero) is not None

# # Exemplo de uso
# telefone = "(84) 99999-9999"
# if validar_telefone(telefone):
#     print("O número de telefone é válido.")
# else:
#     print("O número de telefone é inválido.")