import os
import vendas.dicionario as arqv_vd
import vendas.interfaces as interfaces

#################################################
#####          EXCLUIR DADOS VENDA          #####
#################################################

'''
Para não acontecer de, ser excluido uma venda de cód 2, exemplo, e quando for cadastrar outra venda, essa venda não pegar
o mesmo cód que foi excluido, deixando um pouco bagunçado... Cada venda fica com um ativo em seus dados, estiver on = True, for excluído, ativo = False -> Assim, o cód_venda é unico e não se repete!

'''

def excluir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####           Excluir Venda          #####")
  print("#####         0 - Para Retornar        #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_venda = int(input("##### Digite o Código da Venda ou Digite '0' Para Retornar: "))
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
    print()
    decisao = input("Tem certeza que deseja EXCLUIR essa Venda (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      arqv_vd.vendas[code_venda][6] = False
      print("Venda excluída com sucesso!")
      print()
    else:
      print("Exclusão não realizada!")
  else:
    print("##### Venda inexistente ou deletada!")
    print()
  print()
  input("tecle <ENTER> para continuar...")
  #-----------------------------------------------