############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

# imports
import interfaces # Arquvio com as minhas interfaces (modularização)
import fun_cliente # Arquivo com as minhas funções de Clientes (modularização)
import fun_estoque # Arquivo com as minhas funções do Estoque (modularização)
import fun_vendas # Arquivo com as minhas funções  de Vendas (modularização)
import os

################################################################
################################################################
##########            PROGRAMA PRINCIPAL              ##########
################################################################
################################################################

op_princ = ""
while op_princ != "0":
  op_princ = interfaces.menu_principal()
  print()
  if op_princ == "1":
    op_cliente = ""
    while op_cliente != "0":
      op_cliente = interfaces.menu_cliente()
      print()
      if op_cliente == "1":
        fun_cliente.cadastrar_cliente()
      elif op_cliente == "2":
        fun_cliente.exibir_cliente()
      elif op_cliente == "3":
        fun_cliente.alterar_cliente()
      elif op_cliente == "4":
        fun_cliente.excluir_cliente()
  elif op_princ == "2":
    op_estoque = ""
    while op_estoque != "0":
      op_estoque = interfaces.menu_estoque()
      print()
      if op_estoque == "1":
        fun_estoque.cadastrar_produto()
      elif op_estoque == "2":
        fun_estoque.exibir_produto()
      elif op_estoque == "3":
        fun_estoque.alterar_produto()
      elif op_estoque == "4":
        fun_estoque.excluir_produto()
  elif op_princ == "3":
    op_vendas = ""
    while op_vendas != "0":
      op_vendas = interfaces.menu_vendas()
      print()
      if op_vendas == "1":
        fun_vendas.cadastrar_venda()
      elif op_vendas == "2":
        fun_vendas.exibir_venda()
      elif op_vendas == "3":
        fun_vendas.alterar_venda()
      elif op_vendas == "4":
        fun_vendas.excluir_venda()
  elif op_princ == "4":
    op_relatorio = ""
    while op_relatorio != "0":
      op_relatorio = interfaces.menu_relatorio()
      print()
      if op_relatorio == "1":
        op_relatorio_clientes = ""
        while op_relatorio_clientes != "0":
          op_relatorio_clientes = interfaces.menu_relatorio_clientes()
          print()
          if op_relatorio_clientes == "1":
            fun_cliente.relatorio_clientes_on()
          elif op_relatorio_clientes == "2":
            fun_cliente.relatorio_clientes_off()
      elif op_relatorio == "2":
        op_relatorio_estoque = ""
        while op_relatorio_estoque != "0":
          op_relatorio_estoque = interfaces.menu_relatorio_estoque()
          print()
          if op_relatorio_estoque == "1":
            fun_estoque.relatorio_estoque_on()
          elif op_relatorio_estoque == "2":
            fun_estoque.relatorio_estoque_off()
      elif op_relatorio == "3":
        op_relatorio_vendas = ""
        while op_relatorio_vendas != "0":
          op_relatorio_vendas = interfaces.menu_relatorio_vendas()
          print()
          if op_relatorio_vendas == "1":
            fun_vendas.relatorio_vendas_on()
          elif op_relatorio_vendas == "2":
            fun_vendas.relatorio_vendas_off()
  elif op_princ == "5":
    interfaces.menu_informacao()

os.system('claer || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
print()
print("Programa encerrado. Até breve...")
print()
interfaces.encerramento() 
fun_cliente.salvar_dados_clientes() # Função para guardar os dados de CLIENTES,
fun_estoque.salvar_dados_produtos() # Função para guardar os dados de PRODUTOS,
fun_vendas.salvar_dados_vendas() # Função para guardar os dados de VENDAS