import os
import clientes.dicionario as arqv_cl # -> arquivo cliente
import clientes.interfaces as interfaces

#################################################
#####       RELATÓRIO CLIENTES ATIVOS       #####
#################################################

def relatorio_clientes_on():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  interfaces.tabela_relatorio_cliente_atv()
  for code_cliente in arqv_cl.clientes:
    if arqv_cl.clientes[code_cliente][4]:
      print("| %-3s "%(code_cliente), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(arqv_cl.clientes[code_cliente][0]), end='') # 2
      print("| %-43s "%(arqv_cl.clientes[code_cliente][1]), end='') # 3
      print("| %-16s "%(arqv_cl.clientes[code_cliente][2]), end='') # 4
      print("| %-14s "%(arqv_cl.clientes[code_cliente][3]))         # 5
  print("--------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")    
#---------------------------------------------------------------------


###################################################
#####       RELATÓRIO CLIENTES INATIVOS       #####
###################################################

def relatorio_clientes_off():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  interfaces.tabela_relatorio_cliente_intv()
  for code_cliente in arqv_cl.clientes:
    if arqv_cl.clientes[code_cliente][4] == False:
      print("| %-3s "%(code_cliente), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(arqv_cl.clientes[code_cliente][0]), end='') # 2
      print("| %-43s "%(arqv_cl.clientes[code_cliente][1]), end='') # 3
      print("| %-16s "%(arqv_cl.clientes[code_cliente][2]), end='') # 4
      print("| %-14s "%(arqv_cl.clientes[code_cliente][3]))         # 5
  print("--------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")          
  #---------------------------------------------------------------------