import os
import estoque.dicionario as arqv_es
import estoque.interfaces as interfaces

#################################################
#####         RELATÓRIO DE PRODUTOS         #####
#################################################

def relatorio_estoque_on():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  interfaces.tabela_relatorio_produtos_atv()
  for code_produto in arqv_es.produtos:
    if arqv_es.produtos[code_produto][8]:
      print("| %-3s "%(code_produto), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(arqv_es.produtos[code_produto][0]), end="") # 2
      print("| %-40s "%(arqv_es.produtos[code_produto][1]), end="") # 3
      print("| %-39s "%(arqv_es.produtos[code_produto][2]), end="") # 4
      print("| %-5s "%(arqv_es.produtos[code_produto][3]), end="")  # 5
      print("| %-6s "%(arqv_es.produtos[code_produto][4]), end="")  # 6
      print("| %-4s "%(arqv_es.produtos[code_produto][5]), end="")  # 7
      print("| %-3s "%(arqv_es.produtos[code_produto][6]), end="")  # 8
      print("| %-5s "%(arqv_es.produtos[code_produto][7]))          # 9
  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------


#######################################################
#####       RELATÓRIO DE PRODUTOS DELETADOS       #####
#######################################################

def relatorio_estoque_off():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  interfaces.tabela_relatorio_produtos_intv()
  for code_produto in arqv_es.produtos:
    if arqv_es.produtos[code_produto][8] == False:
      print("| %-3s "%(code_produto), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(arqv_es.produtos[code_produto][0]), end="") # 2
      print("| %-40s "%(arqv_es.produtos[code_produto][1]), end="") # 3
      print("| %-39s "%(arqv_es.produtos[code_produto][2]), end="") # 4
      print("| %-5s "%(arqv_es.produtos[code_produto][3]), end="")  # 5
      print("| %-6s "%(arqv_es.produtos[code_produto][4]), end="")  # 6
      print("| %-4s "%(arqv_es.produtos[code_produto][5]), end="")  # 7
      print("| %-3s "%(arqv_es.produtos[code_produto][6]), end="")  # 8
      print("| %-5s "%(arqv_es.produtos[code_produto][7]))          # 9
  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------