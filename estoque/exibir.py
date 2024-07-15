import os
import estoque.dicionario as arqv_es
import estoque.interfaces as interfaces

#################################################
#####          EXIBIR DADOS PRODUTO         #####
#################################################

def exibir_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados do Produto     #####")
    print("#####         0 - Para Retornar        #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_produto = int(input("##### Digite o Código do Produto ou Digite '0' Para Retornar: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if code_produto == 0:
      return
    if (code_produto in arqv_es.produtos) and (arqv_es.produtos[code_produto][8]):
      print()
      interfaces.tabela_produto()
      print("| %-43s "%(arqv_es.produtos[code_produto][0]), end="") # 1
      print("| %-40s "%(arqv_es.produtos[code_produto][1]), end="") # 2
      print("| %-39s "%(arqv_es.produtos[code_produto][2]), end="") # 3
      print("| %-5s "%(arqv_es.produtos[code_produto][3]), end="")  # 4
      print("| %-6s "%(arqv_es.produtos[code_produto][4]), end="")  # 5
      print("| %-4s "%(arqv_es.produtos[code_produto][5]), end="")  # 6
      print("| %-3s "%(arqv_es.produtos[code_produto][6]), end="")  # 7
      print("| %-5s "%(arqv_es.produtos[code_produto][7]))          # 8
      print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
      print()
    else:
      print("Produto inexiste ou deletado!")
      print()
    resp = input("tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes:  ")
  print()
  #-----------------------------------------------