'''Interfaces'''

'''imports'''
import os


#################################################
#####       INTERFACE MENU PRINCIPAL        #####
#################################################

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
#--------------------------------------------------------------------------------


#################################################
#####       INTERFACE MENU CLIENTES         #####
#################################################

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
#--------------------------------------------------------------------------------


#################################################
#####        INTERFACE MENU ESTOQUE         #####
#################################################

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
#--------------------------------------------------------------------------------


#################################################
#####        INTERFACE MENU VENDAS          #####
#################################################

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
#--------------------------------------------------------------------------------


#################################################
#####       INTERFACE MENU RELATÓRIO        #####
#################################################

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
#--------------------------------------------------------------------------------


#########################################################
#####       INTERFACE MENU RELATÓRIO CLIENTES       #####
#########################################################

def menu_relatorio_clientes():
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
  op_relatorio_clientes = input("##### Escolha sua opção: ")
  return op_relatorio_clientes
#--------------------------------------------------------------------------------


#########################################################
#####       INTERFACE MENU RELATÓRIO PRODUTOS       #####
#########################################################

def menu_relatorio_estoque():
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
  op_relatorio_estoque = input("#### Escolha sua opção: ")
  return op_relatorio_estoque
#--------------------------------------------------------------------------------


#########################################################
#####      INTERFACE MENU RELATÓRIO DE VENDAS       #####
#########################################################

def menu_relatorio_vendas():
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
  op_relatorio_vendas = input("##### Escolha sua opção: ")
  return op_relatorio_vendas
#--------------------------------------------------------------------------------


#################################################
#####      INTERFACE MENU INFORMAÇÃO        #####
#################################################

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
#----------------------------------------------------------------------------------


#################################################
#####      INTERFACE DE ENCERRAMENTO        #####
#################################################

def encerramento(): # Interface ao encerrar o programa
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
    print("ASCCI(s) feitas no site: https://ascii-art.botecodigital.dev.br/") # ;)
    print()