############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

# imports
import funcoes # Arquivo com as minhas funções (modularização)
import interfaces # Arquvio com as minhas interfaces (modularização)
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
        op_relatorio_clientes = ""
        while op_relatorio_clientes != "0":
          op_relatorio_clientes = funcoes.menu_relatorio_clientes()
          print()
          if op_relatorio_clientes == "1":
            funcoes.relatorio_clientes_on()
          elif op_relatorio_clientes == "2":
            funcoes.relatorio_clientes_off()
      elif op_relatorio == "2":
        op_relatorio_estoque = ""
        while op_relatorio_estoque != "0":
          op_relatorio_estoque = funcoes.menu_relatorio_estoque()
          print()
          if op_relatorio_estoque == "1":
            funcoes.relatorio_estoque_on()
          elif op_relatorio_estoque == "2":
            funcoes.relatorio_estoque_off()
      elif op_relatorio == "3":
        op_relatorio_vendas = ""
        while op_relatorio_vendas != "0":
          op_relatorio_vendas = funcoes.menu_relatorio_vendas()
          print()
          if op_relatorio_vendas == "1":
            funcoes.relatorio_vendas_on()
          elif op_relatorio_vendas == "2":
            funcoes.relatorio_vendas_off()
  elif op_princ == "5":
    interfaces.menu_informacao()

os.system('claer || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
print()
print("Programa encerrado. Até breve...")
print()
interfaces.encerramento() 
funcoes.salvar_dados() # Função para guardar os dados de CLIENTES, PRODUTOS e VENDAS