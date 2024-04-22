############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

# imports
import os

op_princ = ""
while op_princ != "0":
  os.system('clear || cls')

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
    op_cliente = ""
    while op_cliente != "0":
      os.system('clear || cls')
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
      input("Tecle <ENTER> para continuar...")
    
  elif op_princ == "2":
    op_estoque = ""
    while op_estoque != "0":
      os.system('clear || cls')
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
      input("Tecle <ENTER> para continuar...")

  elif op_princ == "3":
    op_vendas = ""
    while op_vendas != "0":
      os.system('clear || cls')
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
      print()
      input("Tecle <ENTER> para continuar...")
      
  elif op_princ == "4":
    op_relatorio = ""
    while op_relatorio != "0":
      os.system('clear || cls')
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
    os.system('clear || cls')
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


os.system('clear || cls')
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