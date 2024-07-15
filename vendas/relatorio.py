import os
import vendas.dicionario as arqv_vd
import vendas.interfaces as interfaces

#################################################
#####          RELATÓRIO DE VENDAS          #####
#################################################

def relatorio_vendas_on():   
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls' 
  interfaces.tabela_relatorio_vendas_atv()
  for code_venda in arqv_vd.vendas:
    if arqv_vd.vendas[code_venda][6]:
      print("| %-3s "%(code_venda), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-10s "%(arqv_vd.vendas[code_venda][0]), end="") # 2
      print("| %-43s "%(arqv_vd.vendas[code_venda][1]), end="") # 3
      print("| %-43s "%(arqv_vd.vendas[code_venda][2]), end="") # 4
      print("| %-2s "%(arqv_vd.vendas[code_venda][3]), end="")  # 5
      print("| %-6s "%(arqv_vd.vendas[code_venda][4]), end="")  # 6
      print("| %-10s "%(arqv_vd.vendas[code_venda][5]))         # 7
  print("------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------


#########################################################
#####          RELATÓRIO DE VENDAS DELETADAS        #####
#########################################################

def relatorio_vendas_off():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  interfaces.tabela_relatorio_vendas_intv()
  for code_venda in arqv_vd.vendas:
    if arqv_vd.vendas[code_venda][6] == False:
      print("| %-3s "%(code_venda), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-10s "%(arqv_vd.vendas[code_venda][0]), end="") # 2
      print("| %-43s "%(arqv_vd.vendas[code_venda][1]), end="") # 3
      print("| %-43s "%(arqv_vd.vendas[code_venda][2]), end="") # 4
      print("| %-2s "%(arqv_vd.vendas[code_venda][3]), end="")  # 5
      print("| %-6s "%(arqv_vd.vendas[code_venda][4]), end="")  # 6
      print("| %-10s "%(arqv_vd.vendas[code_venda][5]))         # 7
  print("------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------