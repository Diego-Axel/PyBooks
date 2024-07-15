import os 
import clientes.dicionario as arqv_cl # -> arquivo cliente
import clientes.interfaces as interfaces
import clientes.len_cliente as len_cliente

#################################################
#####         ALTERAR DADOS CLIENTE         #####
#################################################

def alterar_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####     Alterar Dados do Cliente     #####")
  print("#####         0 - Para Retornar        #####")
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
  verificador = True
  while verificador:
    os.system('celar || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_cliente in arqv_cl.clientes) and (arqv_cl.clientes[code_cliente][4]):
      print()
      interfaces.tabela_alteracao_clientes()
      print("| %-43s "%(arqv_cl.clientes[code_cliente][0]), end='') # 1
      print("| %-43s "%(arqv_cl.clientes[code_cliente][1]), end='') # 2
      print("| %-16s "%(arqv_cl.clientes[code_cliente][2]), end='') # 3
      print("| %-13s "%(arqv_cl.clientes[code_cliente][3]))         # 4
      print("---------------------------------------------------------------------------------------------------------------------------------")
      print()        
      resp = input("#### Qual dado deseja alterar (0 Para Cancelar)? ")
      resp = resp.upper()
      print()
      ativo = True
      arqv_cl.clientes[code_cliente][4] = ativo
      if (resp == "NOME") or (resp == "CLIENTE"):
        nome_cliente = len_cliente.ler_nome()
        arqv_cl.clientes[code_cliente][0] = nome_cliente
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_cliente.ler_decisao_alteracao()
      elif (resp == "E-MAIL") or (resp == "EMAIL"):
        email = len_cliente.ler_email()
        arqv_cl.clientes[code_cliente][1] = email
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_cliente.ler_decisao_alteracao()
      elif (resp == "CELULAR") or (resp == "TELEFONE"):
        celular = len_cliente.ler_celular()
        arqv_cl.clientes[code_cliente][2] = celular
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_cliente.ler_decisao_alteracao()
      elif (resp == "CPF"):
        cpf = len_cliente.ler_cpf()
        arqv_cl.clientes[code_cliente][3] = cpf
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_cliente.ler_decisao_alteracao()
      elif (resp == "0"):
        print("Alteração Cancelada!")
        verificador = False
    else:
      print()
      print("Cliente inexistente ou inativo!")   
      verificador = False 
  print()
  input("Tecle <ENTER> para continuar...")
#---------------------------------------------------------------------