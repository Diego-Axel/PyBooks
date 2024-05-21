############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

# imports
import funcoes # Arquivo com as minhas funções (modularização)
import os # função para limpar a tela do terminal
import pickle

################################################################
################################################################
##########            PROGRAMA PRINCIPAL              ##########
################################################################
################################################################

op_princ = ""
while op_princ != "0":
  op_princ = funcoes.menu_principal()
  print()
  if op_princ == "1":
    op_cliente = ""
    while op_cliente != "0":
      op_cliente = funcoes.menu_cliente()
      print()
      if op_cliente == "1":
        funcoes.cadastrar_cliente()
      elif op_cliente == "2":
        funcoes.exibir_cliente()
      elif op_cliente == "3":
        funcoes.alterar_cliente()
      elif op_cliente == "4":
        funcoes.excluir_cliente()
  elif op_princ == "2":
    op_estoque = ""
    while op_estoque != "0":
      op_estoque = funcoes.menu_estoque()
      print()
      if op_estoque == "1":
        funcoes.cadastrar_produto()
      elif op_estoque == "2":
        funcoes.exibir_produto()
      elif op_estoque == "3":
        funcoes.alterar_produto()
      elif op_estoque == "4":
        funcoes.excluir_produto()
  elif op_princ == "3":
    op_vendas = ""
    while op_vendas != "0":
      op_vendas = funcoes.menu_vendas()
      print()
      if op_vendas == "1":
        funcoes.cadastrar_venda()
      elif op_vendas == "2":
        funcoes.exibir_venda()
      elif op_vendas == "3":
        funcoes.alterar_venda()
      elif op_vendas == "4":
        funcoes.excluir_venda()
  elif op_princ == "4":
    op_relatorio = ""
    while op_relatorio != "0":
      op_relatorio = funcoes.menu_relatorio()
      print()
      if op_relatorio == "1":
        funcoes.relatorio_clientes()
      elif op_relatorio == "2":
        funcoes.relatorio_estoque()
      elif op_relatorio == "3":
        funcoes.relatorio_vendas()
  elif op_princ == "5":
    funcoes.menu_informacao()

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

# Gravando os dados no arquivo:
funcoes.salvar_dados() # Função para guardar os dados de CLIENTES, PRODUTOS e VENDAS