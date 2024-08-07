import os

#################################################
#####        INTERFACE MENU VENDAS          #####
#################################################

def menu_vendas(): # Função do Menu de Vendas
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print('''
        __   __           _         
        \ \ / /__ _ _  __| |__ _ ___
         \ V / -_) ' \/ _` / _` (_-<
          \_/\___|_||_\__,_\__,_/__/
  ''')
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


########################################################
#####           INTERFACE TABELA VENDAS            #####
########################################################

def tabela_venda():
  print("#####################################################################################################################################")
  print("##########################################               Dados da Venda              ################################################")
  print("#####################################################################################################################################")
  print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
  print("| Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
  print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
#--------------------------------------------------------------------------------


#################################################################
#####            INTERFACE TABELA VENDAS ALTERAÇÃO          #####
#################################################################

def tabela_alteracao_vendas():
  print("#####################################################################################################################################")
  print("##########################################               Dados da Venda              ################################################")
  print("##########################################              0 - Para Cancelar            ################################################")
  print("#####################################################################################################################################")
  print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
  print("| Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
  print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
#--------------------------------------------------------------------------------


###########################################################################
#####           INTERFACE TABELA RELATÓRIO VENDAS NO SISTEMA          #####
###########################################################################

def tabela_relatorio_vendas_atv():
  print("###########################################################################################################################################")
  print("############################################            Relatório de Vendas            ####################################################")
  print("###########################################################################################################################################")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
  print("| Cod | Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
#--------------------------------------------------------------------------------


##########################################################################
#####           INTERFACE TABELA RELATÓRIO VENDAS DELETADAS          #####
##########################################################################

def tabela_relatorio_vendas_intv():
  print("###########################################################################################################################################")
  print("##########################################           Relatório de Vendas  Deletadas         ###############################################")
  print("###########################################################################################################################################")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
  print("| Cod | Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
#--------------------------------------------------------------------------------

######################################################
#####       INTERFACE ALTERAÇÃO REALIZADA        #####
######################################################

def confirmar_alteracao():
  print("##############################")
  print("| Dado alterado com sucesso! |")
  print("##############################")


#################################################
#####            CADASTRAR VENDA            #####
#################################################

def confirmar_cadastro():
  print("############################################")
  print("#####         Cadastrar Venda          #####")
  print("#####       <ENTER> - Prosseguir       #####")
  print("#####           0 - Cancelar           #####")
  print("############################################")


def cadastro():
  print("############################################")
  print("#####         Cadastrar Venda          #####")
  print("############################################")


#################################################
#####         EXIBIR DADOS DA VENDA         #####
#################################################

def exibir():
  print("############################################")
  print("#####      Exibir Dados de Vendas      #####")
  print("#####        0 - Para Retornar         #####")
  print("############################################")


#################################################
#####          ALTERAR DADOS VENDA          #####
#################################################

def alterar():
  print("############################################")
  print("#####      Alterar Dados de Venda      #####")
  print("#####         0 - Para Retornar        #####")
  print("############################################")


#################################################
#####          EXCLUIR DADOS VENDA          #####
#################################################

def excluir():
  print("############################################")
  print("#####           Excluir Venda          #####")
  print("#####         0 - Para Retornar        #####")
  print("############################################")