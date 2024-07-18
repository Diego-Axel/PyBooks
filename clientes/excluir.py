import os
import clientes.dicionario as arqv_cl # -> arquivo cliente
import clientes.interfaces as interfaces

#################################################
#####         EXCLUIR DADOS CLIENTE         #####
#################################################

'''
Para não acontecer de, ser excluido um cliente de cód 2, exemplo, e quando for cadastrar outro cliente, esse cliente não pegar o mesmo cód que foi excluido, deixando um pouco bagunçado... Cada cliente fica com um ativo em seus dados, estiver on = True, for excluído, ativo = False -> Assim, o cód_cliente é unico e não se repete!      

'''

def excluir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  interfaces.excluir()
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
    decisao = input(" -> Tem certeza que deseja EXCLUIR esse Cliente (S/N)? ")
    decisao = decisao.upper()
    print()
    if (decisao == "SIM") or (decisao == "S"):
      arqv_cl.clientes[code_cliente][4] = False 
      print("Cliente excluído(a) com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Cliente inexistente ou inativo!")
  print()
  input("Tecle <ENTER> para continuar...")  
#---------------------------------------------------------------------