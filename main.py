############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

# imports
import os

# Dicionarios
clientes = {}
produtos = {}
vendas = {}

op_princ = ""
while op_princ != "0":
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
  op_princ = input("##### Escolha sua opção: ")
  if op_princ == "1":
    qtd_clientes = 0
    op_cliente = ""
    while op_cliente != "0":
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
      print()
      if op_cliente == "1":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####        Cadastrar Cliente         #####")
        print("############################################")
        print()
        code_cliente = input("##### Digite o Código do Cliente: ")
        qtd_clientes += 1
        print()
        nome = input("##### Nome: ")
        print()
        email = input("#### E-mail: ")
        print()
        celular = input("##### Celular com DDD: ")
        print()
        cpf = input("##### CPF: ")
        clientes[code_cliente] = [nome, email, celular, cpf]
        print()
        print(clientes)
        print("Cliente cadastrado com sucesso!")
        print()
        input("Tecle <ENTER> para continuar...")
      elif op_cliente == "2":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####      Exibir Dados do Cliente     #####")
        print("############################################")
        print()
        print("##### Você tem um TOTAL de %s Clientes Cadastrados"%qtd_clientes)
        decisao = input("##### Deseja ver TODOS seus CLIENTES (S/N)? ")
        decisao = decisao.upper()
        if (decisao == "SIM") or (decisao == "S"):
          print()
          print(clientes , "\n")
        else:
          print()
          code_cliente = input("##### Digite o Código do Cliente: ")
          if code_cliente in clientes:
            print()
            print("##### Nome: ",clientes[code_cliente][0])
            print("##### E-mail: ",clientes[code_cliente][1])
            print("##### Celular: ",clientes[code_cliente][2])
            print("##### CPF: ",clientes[code_cliente][3])
            print()
          else:
            print("Cliente inexistente!")
        print()
        input("Tecle <ENTER> para continuar...")
      elif op_cliente == "3":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####     Alterar Dados do Cliente     #####")
        print("############################################")
        print()
        code_cliente = input("##### Digite o Código do Cliente: ")
        dados_cliente = True
        while dados_cliente:
          os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
          if code_cliente in clientes:
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
            decisao = input("##### Qual dado você deseja ALTERAR? ")
            decisao = decisao.upper()
            if decisao == "NOME":
              print()
              nome = input("##### Digite o novo Nome: ")
              print("Cliente Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if resp == "S" or resp == "SIM":
                print()
              else:
                dados_cliente = False
            elif decisao == "E-MAIL":
              print()
              email = input("#### Digite o novo E-mail: ")
              print()
              print("Cliente Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if resp == "S" or resp == "SIM":
                print()
              else:
                dados_cliente = False
            elif decisao == "CELULAR":  
              print()
              celular = input("##### Digite o novo Celular: ")
              print()
              print("Cliente Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if resp == "S" or resp == "SIM":
                print()
              else:
                dados_cliente = False
            elif decisao == "CPF":
              print()
              cpf = input("##### Digite o novo CPF: ")
              print()
              print("Cliente Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if resp == "S" or resp == "SIM":
                print()
              else:
                dados_cliente = False
            clientes[code_cliente] = [nome, email, celular, cpf]
          else:
            print()
            print("Cliente inexistente!")
            dados_cliente = False
        print()
        input("Tecle <ENTER> para continuar...")
      elif op_cliente == "4":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####          Excluir Cliente         #####")
        print("############################################")
        print()
        code_cliente = input("##### Digite o Código do Cliente: ")
        if code_cliente in clientes:
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
            del clientes[code_cliente]
            print("Cliente excluído(a) com sucesso!")
            qtd_clientes -= 1 
          else:
            print("Exclusão não realizada!")
        else:
          print("Cliente inexistente!")
          print()
        input("Tecle <ENTER> para continuar...")  
  elif op_princ == "2":
    qtd_produtos = 0
    op_estoque = ""
    while op_estoque != "0":
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
      print()
      if op_estoque == "1":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####        Cadastrar Produto         #####")
        print("############################################")
        print()
        code_produto = input("##### Digite o Código do Produto: ")
        qtd_produtos += 1
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
        print("##### GÊNERO TEXTUTAL #####")
        print("| 1 - Ação \n| 2 - Ficção \n| 3 - Suspense \n| 4 - Educativo \n| 5 - Infantil \n| 6 - Recreativo \n| 7 - Amplo")
        print()
        genero = int(input("##### Tipo de Gênero (NÚMERO): "))
        print()
        qtd_estoque = int(input("##### Quantidade em Estoque (NÚMERO): "))
        print()
        produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque]
        print()
        print(produtos)
        print("Produto cadastrado com sucesso!")
        print()
        input("Tecle <ENTER> para continuar...")
      elif op_estoque == "2":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####      Exibir Dados do Produto     #####")
        print("############################################")
        print()
        print("##### Você tem um TOTAL de %s Produtos Cadastrados"%qtd_produtos)
        decisao = input("##### Deseja ver TODOS seus PRODUTOS (S/N)? ")
        decisao = decisao.upper()
        if (decisao == "SIM") or (decisao == "S"):
          print()
          print(produtos)
        else:
          print()
          code_produto = input("##### Digite o Código do Produto: ")
          if code_produto in produtos:
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
            print("Produto inexiste!")
            print()
        input("Tecle <ENTER> para continuar...")
      elif op_estoque == "3":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####     Alterar Dados do Produto     #####")
        print("############################################")
        print()
        code_produto = input("##### Digite o Código do Produto: ")
        dados_produto = True
        while dados_produto:
          os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
          if code_produto in produtos:
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
            decisao = input("##### Qual dado você deseja ALTERAR? ")
            decisao = decisao.upper()
            if (decisao == "NOME") or (decisao == "NOME DO LIVRO"):
              print()
              nome_livro = input("##### Digite o novo Nome do Livro: ")
              print()
              print("Produto Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if (resp == "S") or (resp == "SIM"):
                print()
              else:
                dados_produto = False
            elif (decisao == "DESCRIÇÃO") or (decisao == "DESCRICAO"):
              print()
              descricao = input("##### Digite a nova Descrição: ")
              print()
              print("Produto Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if (resp == "S") or (resp == "SIM"):
                print()
              else:
                dados_produto = False
            elif decisao == "AUTOR":
              print()
              autor = input("##### Digite o novo Autor: ")
              print()
              print("Produto Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if (resp == "S") or (resp == "SIM"):
                print()
              else:
                dados_produto = False
            elif decisao == "ANO":
              print()
              ano = input("##### Digite o novo Ano: ")
              print()
              print("Produto Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if (resp == "S") or (resp == "SIM"):
                print()
              else:
                dados_produto = False
            elif decisao == "TIPO DE CAPA":
              print()
              tipo_capa = input("##### Tipo de Capa: ")
              print()
              print("Produto Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if (resp == "S") or (resp == "SIM"):
                print()
              else:
                dados_produto = False
            elif (decisao == "GÊNERO") or (decisao == "GENERO"):
              print("| 1 - Ação \n| 2 - Ficção \n| 3 - Suspense \n| 4 - Educativo \n| 5 - Infantil \n| 6 - Recreativo \n| 7 - Amplo")
              print()
              genero = int(input("##### Digite o NÚMERO do novo Gênreo: "))
              print()
              print("Produto Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if (resp == "S") or (resp == "SIM"):
                print()
              else:
                dados_produto = False
            elif decisao == "QUANTIDADE EM ESTOQUE":
              print()
              qtd_estoque = int(input("##### Quantidade em Estoque(NÚMERO): "))
              print()
              print("Produto Alterado com sucesso!")
              print()
              resp = input("##### Deseja ALTERAR mais dados (S/N)? ")
              resp = resp.upper()
              if (resp == "S") or (resp == "SIM"):
                print()
              else:
                dados_produto = False
            produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque]
          else:
            print()
            print("Produto inexistente!")
            dados_produto = False
        print()
        input("Tecle <ENTER> para continuar...")
      elif op_estoque == "4":
        os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
        print()
        print("############################################")
        print("#####          Excluir Produto         #####")
        print("############################################")
        print()
        code_produto = input("##### Digite o Código do Produto: ")
        if code_produto in produtos:
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
            del produtos[code_produto]
            print("Produto excluído com sucesso!")
            qtd_produtos -= 1
          else:
            print("Exclusão não realizada!")
        else:
          print("Produto inexistente!")
          print()
        input("Tecle <ENTER> para continuar...")

  elif op_princ == "3":
    op_vendas = ""
    while op_vendas != "0":
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
      if op_vendas == "1":
        print()
      print()
      input("Tecle <ENTER> para continuar...")

  elif op_princ == "4":
    op_relatorio = ""
    while op_relatorio != "0":
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
      print()
      input("Tecle <ENTER> para continuar...")     
  elif op_princ == "5":
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

os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
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