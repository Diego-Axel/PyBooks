import os
import estoque.dicionario as arqv_es
import estoque.interfaces as interfaces

#################################################
#####         EXCLUIR DADOS PRODUTO         #####
#################################################

'''
Para não acontecer de, ser excluido um produto de cód 2, exemplo, e quando for cadastrar outro produto, esse produto não pegar
o mesmo cód que foi excluido, deixando um pouco bagunçado... Cada produto fica com um ativo em seus dados, estiver on = True, for excluído, ativo = False -> Assim, o cód_produto é unico e não se repete! 

'''

def excluir_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####          Excluir Produto         #####")
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
    decisao = input("Tem certeza que deseja EXCLUIR esse Produto (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      arqv_es.produtos[code_produto][8] = False
      print("Produto excluído com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Produto inexistente ou deletado!")
    verificador = False
    print()
  print()
  input("Tecle <ENTER> para continuar...")
#-----------------------------------------------