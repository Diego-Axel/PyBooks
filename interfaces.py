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