import os
import vendas.dicionario as arqv_vd
import vendas.interfaces as interfaces

#################################################
#####         EXIBIR DADOS DA VENDA         #####
#################################################

def exibir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados de Vendas      #####")
    print("#####        0 - Para Retornar         #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_venda = int(input("##### Digite o Código de Venda ou Digite '0' Para Retornar: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if code_venda == 0:
      return
    if (code_venda in arqv_vd.vendas) and (arqv_vd.vendas[code_venda][6]):
      print()
      interfaces.tabela_venda()
      print("| %-10s "%(arqv_vd.vendas[code_venda][0]), end="") # 1
      print("| %-43s "%(arqv_vd.vendas[code_venda][1]), end="") # 2
      print("| %-43s "%(arqv_vd.vendas[code_venda][2]), end="") # 3
      print("| %-2s "%(arqv_vd.vendas[code_venda][3]), end="")  # 4
      print("| %-6s "%(arqv_vd.vendas[code_venda][4]), end="")  # 5
      print("| %-10s "%(arqv_vd.vendas[code_venda][5]))         # 6
      print("-------------------------------------------------------------------------------------------------------------------------------------")
    else:
      print()
      print("Venda inexistente ou deletada!")
      print()
    resp = input("tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes: ")
  print()
#-----------------------------------------------