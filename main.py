############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

# imports na main
import os
import interfaces # Arquvio com as minhas interfaces no menu principal

# imports clientes
import clientes.interfaces as interface_cl
import clientes.cadastrar as cadastrar_cl
import clientes.exibir as exibir_cl
import clientes.alterar as alterar_cl
import clientes.excluir as excluir_cl
import clientes.relatorio as relatorio_cl
import clientes.salvar as salvar_cl

# Imports estoque
import estoque.interfaces as interface_es
import estoque.cadastrar as cadastrar_es
import estoque.exibir as exibir_es
import estoque.alterar as alterar_es
import estoque.excluir as excluir_es
import estoque.relatorio as relatorio_es
import estoque.salvar as salvar_es

# imports vendas
import vendas.interfaces as interface_vd
import vendas.cadastrar as cadastrar_vd
import vendas.exibir as exibir_vd
import vendas.alterar as alterar_vd
import vendas.excluir as excluir_vd
import vendas.relatorio as relatorio_vd
import vendas.salvar as salvar_vd


# imports interfaces de relatórios
import relatorios.interfaces as interface_rel



################################################################
##########            PROGRAMA PRINCIPAL              ##########
################################################################

op_princ = ""
while op_princ != "0":
  op_princ = interfaces.menu_principal()
  print()
  if op_princ == "1":
    op_cliente = ""
    while op_cliente != "0":
      op_cliente = interface_cl.menu_cliente()
      print()
      if op_cliente == "1":
        cadastrar_cl.cadastrar_cliente()
      elif op_cliente == "2":
        exibir_cl.exibir_cliente()
      elif op_cliente == "3":
        alterar_cl.alterar_cliente()
      elif op_cliente == "4":
        excluir_cl.excluir_cliente()
  elif op_princ == "2":
    op_estoque = ""
    while op_estoque != "0":
      op_estoque = interface_es.menu_estoque()
      print()
      if op_estoque == "1":
        cadastrar_es.cadastrar_produto()
      elif op_estoque == "2":
        exibir_es.exibir_produto()
      elif op_estoque == "3":
        alterar_es.alterar_produto()
      elif op_estoque == "4":
        excluir_es.excluir_produto()
  elif op_princ == "3":
    op_vendas = ""
    while op_vendas != "0":
      op_vendas = interface_vd.menu_vendas()
      print()
      if op_vendas == "1":
        cadastrar_vd.cadastrar_venda()
      elif op_vendas == "2":
        exibir_vd.exibir_venda()
      elif op_vendas == "3":
        alterar_vd.alterar_venda()
      elif op_vendas == "4":
        excluir_vd.excluir_venda()
  elif op_princ == "4":
    op_relatorio = ""
    while op_relatorio != "0":
      op_relatorio = interface_rel.menu_relatorio()
      print()
      if op_relatorio == "1":
        op_relatorio_clientes = ""
        while op_relatorio_clientes != "0":
          op_relatorio_clientes = interface_rel.menu_relatorio_clientes()
          print()
          if op_relatorio_clientes == "1":
            relatorio_cl.relatorio_clientes_on()
          elif op_relatorio_clientes == "2":
            relatorio_cl.relatorio_clientes_off()
      elif op_relatorio == "2":
        op_relatorio_estoque = ""
        while op_relatorio_estoque != "0":
          op_relatorio_estoque = interface_rel.menu_relatorio_estoque()
          print()
          if op_relatorio_estoque == "1":
            relatorio_es.relatorio_estoque_on()
          elif op_relatorio_estoque == "2":
            relatorio_es.relatorio_estoque_off()
      elif op_relatorio == "3":
        op_relatorio_vendas = ""
        while op_relatorio_vendas != "0":
          op_relatorio_vendas = interface_rel.menu_relatorio_vendas()
          print()
          if op_relatorio_vendas == "1":
            relatorio_vd.relatorio_vendas_on()
          elif op_relatorio_vendas == "2":
            relatorio_vd.relatorio_vendas_off()
  elif op_princ == "5":
    interfaces.menu_informacao()

os.system('claer || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
print()
print("Programa encerrado. Até breve...")
print()
interfaces.encerramento() 
salvar_cl.salvar_dados_clientes() # Função para guardar os dados de CLIENTES,
salvar_es.salvar_dados_produtos() # Função para guardar os dados de PRODUTOS,
salvar_vd.salvar_dados_vendas() # Função para guardar os dados de VENDAS