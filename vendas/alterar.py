import os 
import vendas.dicionario as arqv_vd
import vendas.interfaces as interfaces
import vendas.len_vendas as len_vendas
import validadores

#################################################
#####          ALTERAR DADOS VENDA          #####
#################################################

def alterar_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  interfaces.alterar()
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
  verificador = True
  while verificador:
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_venda in arqv_vd.vendas) and (arqv_vd.vendas[code_venda][6]):
      print()
      interfaces.tabela_alteracao_vendas()
      print("| %-10s "%(arqv_vd.vendas[code_venda][0]), end="") # 1
      print("| %-43s "%(arqv_vd.vendas[code_venda][1]), end="") # 2
      print("| %-43s "%(arqv_vd.vendas[code_venda][2]), end="") # 3
      print("| %-2s "%(arqv_vd.vendas[code_venda][3]), end="")  # 4
      print("| %-6s "%(arqv_vd.vendas[code_venda][4]), end="")  # 5
      print("| %-10s "%(arqv_vd.vendas[code_venda][5]))         # 6
      print("-------------------------------------------------------------------------------------------------------------------------------------")
      print()
      resp = input("#### Qual dado deseja alterar? ")
      resp = resp.upper()
      print()
      ativo_venda = True
      arqv_vd.vendas[code_venda][6] = ativo_venda
      if (resp == "DATA DE VENDA") or (resp == "DATA") or (resp == "DATA VENDA"):
        data_venda = validadores.validar_data()
        arqv_vd.vendas[code_venda][0] = data_venda
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "NOME DO CLIENTE") or (resp == "NOME CLIENTE") or (resp == "CLIENTE") or (resp == "COMPRADOR") or (resp == "NOME DO COMPRADOR"):    
        nome_cliente_venda = len_vendas.ler_nome()
        arqv_vd.vendas[code_venda][1] = nome_cliente_venda
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "LIVRO COMPRADO") or (resp == "LIVRO") or (resp == "NOME DO LIVRO"):
        livro_comprado = len_vendas.ler_livro()
        arqv_vd.vendas[code_venda][2] = livro_comprado
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "UNIDADES") or (resp == "UNIDADES ADQUIRIDAS") or (resp == "UNIDADES VENDIDAS") or (resp == "UN"):
        unidades = len_vendas.ler_unidades()
        arqv_vd.vendas[code_venda][3] = unidades
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "VALOR R$") or (resp == "VALOR DE VENDA") or (resp == "R$") or (resp == "VALOR"):
        valor = len_vendas.ler_valor()
        arqv_vd.vendas[code_venda][4] = valor
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "FORMA DE PAGAMENTO") or (resp == "PAGAMENTO") or (resp == "Forma Pgt") or (resp == "Forma Pgt."):
        forma_pgto = len_vendas.ler_forma_pgto()
        arqv_vd.vendas[code_venda][5] = forma_pgto
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "0"):
        print("Alteração Cancelada!")
        verificador = False
    else:
      print()
      print("Venda inexistente ou deletada!")
      verificador = False
    print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------