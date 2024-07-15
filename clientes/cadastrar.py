import os
import time
import clientes.dicionario as arqv_cl # -> arquivo cliente
import clientes.len_cliente as len_cliente

#################################################
#####           CADASTRAR CLIENTE           #####
#################################################

def cadastrar_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Cliente         #####")
  print("#####       <ENTER> - Prosseguir       #####")
  print("#####           0 - Cancelar           #####")
  print("############################################")
  print()
  confirmacao = input("Entrando em 'Cadastro de Cliente' -> Digite '0' Para Cancelar e <ENTER> para prosseguir: ")
  if confirmacao == "0":
    return
  else:
    print("Iniciando cadastro.")
    time.sleep(3)
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Cliente         #####")
  print("############################################")
  print()
  code_cliente = len(arqv_cl.clientes) + 1
  nome_cliente = len_cliente.ler_nome()
  print()
  email = len_cliente.ler_email()
  print()
  celular = len_cliente.ler_celular()  
  print()
  cpf = len_cliente.ler_cpf()
  print()
  ativo = True
  arqv_cl.clientes[code_cliente] = [nome_cliente, email, celular, cpf, ativo] # Dados sendo guardados dentro do Dicionário Clientes, onde o indeteficador daquele dado será o código do Cliente, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print(f"Cliente cadastrado com sucesso sob código: {code_cliente}")
  print()
  input("Tecle <ENTER> para continuar...")
  #---------------------------------------------------------------------


########################################################
#####          CADASTRAR CLIENTE NA VENDA          #####
########################################################

def cadastrar_cliente_venda(): # Estou usando essa função no meu arquivo de vendas, para cadastro de cliente se o mesmo não possuir cadastro
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####         Cadastrar Cliente        #####")
  print("############################################")
  print()
  code_cliente = len(arqv_cl.clientes) + 1
  nome_cliente = len_cliente.ler_nome()
  print()
  email = len_cliente.ler_email()
  print()
  celular = len_cliente.ler_celular()  
  print()
  cpf = len_cliente.ler_cpf()
  print()
  ativo = True
  arqv_cl.clientes[code_cliente] = [nome_cliente, email, celular, cpf, ativo] # Dados sendo guardados dentro do Dicionário Clientes, onde o indeteficador daquele dado será o código do Cliente, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print(f"Cliente cadastrado com sucesso sob código: {code_cliente}")
  print()
  input("Tecle <ENTER> para continuar...")
  #---------------------------------------------------------------------