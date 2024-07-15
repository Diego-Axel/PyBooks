import os

#################################################
#####       INTERFACE MENU RELATÓRIO        #####
#################################################

def menu_relatorio(): # Função do Menu dos Relatórios
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print('''
       ___     _      _           _ 
      | _ \___| |__ _| |_ ___ _ _(_)___ ___
      |   / -_) / _` |  _/ _ \ '_| / _ (_-<
      |_|_\___|_\__,_|\__\___/_| |_\___/__/                                 
  ''')
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