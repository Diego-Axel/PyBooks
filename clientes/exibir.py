import os
import clientes.dicionario as arqv_cl # -> arquivo cliente
import clientes.interfaces as interfaces

#################################################
#####          EXIBIR DADOS CLIENTE         #####
#################################################

def exibir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados do Cliente     #####")
    print("#####        0 - Para Retornar         #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_cliente = int(input("##### Digite o Código do Cliente ou Digite '0' Para Retornar: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if code_cliente == 0:
      return
    if (code_cliente in arqv_cl.clientes) and (arqv_cl.clientes[code_cliente][4]):
      print()
      interfaces.tabela_clientes()
      print("| %-43s "%(arqv_cl.clientes[code_cliente][0]), end='') # 1
      print("| %-43s "%(arqv_cl.clientes[code_cliente][1]), end='') # 2
      print("| %-16s "%(arqv_cl.clientes[code_cliente][2]), end='') # 3
      print("| %-13s "%(arqv_cl.clientes[code_cliente][3]))         # 4
      print("---------------------------------------------------------------------------------------------------------------------------------")
      print()
    else:
        print("Cliente inexistente ou inativo!")
        print()
    resp = input("tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes: ")
  print()
  #---------------------------------------------------------------------