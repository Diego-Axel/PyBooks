import os
import time
import vendas.dicionario as arqv_vd
import vendas.len_vendas as len_vendas
import clientes.dicionario as arqv_cl
import clientes.cadastrar as cadastrar_cl
import estoque.dicionario as arqv_es
import estoque.cadastrar as cadastrar_es
import vendas.interfaces as interfaces

#################################################
#####            CADASTRAR VENDA            #####
#################################################

def cadastrar_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  interfaces.confirmar_cadastro()
  print()
  confirmacao = input("Entrando em 'Cadastro de Venda' -> Digite '0' Para Cancelar e <ENTER> para prosseguir: ")
  if confirmacao == "0":
    return
  else:
    print("Iniciando cadastro.")
    time.sleep(3)
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  interfaces.cadastro()
  print()
  code_venda = len(arqv_vd.vendas) + 1
  data_venda = len_vendas.ler_data()
  print()
  nome_cliente_venda = len_vendas.ler_nome()
  cliente_encontrado = False
  for cliente in arqv_cl.clientes.values(): # Verificando se o nome do cliente inserido está presente no dicionário 'Clientes'
    if cliente[0] == nome_cliente_venda:
      cliente_encontrado = True
      break
  if cliente_encontrado:
    print("##### Ok! Cliente cadastrado na base de dados!")
  else:
    print("##### OPS! Cliente não cadastrado")
    print()
    print("##### Por favor, cadastre esse cliente para dar prosseguimento ao cadastro!")
    print()
    input("tecle <ENTER> para prosseguir para o cadastro de cliente...")
    cadastrar_cl.cadastrar_cliente_venda()
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  interfaces.cadastro()
  print()
  print("##### Cliente Cadastrado! Por favor, continue o cadastro da venda.")
  print()
  print(f"##### Nome do Cliente: {nome_cliente_venda}")
  print()
  livro_comprado = len_vendas.ler_livro()
  livro_encontrado = False
  for livro in arqv_es.produtos.values():
    if livro[0] == livro_comprado:
      livro_encontrado = True
      break
  if livro_encontrado:
    print("##### Ok! Livro cadastrado na base de dados!")
  else:
    print("##### OPS! Livro não cadastrado")
    print()
    print("##### Por favor, cadastre esse livro para dar prosseguimento ao cadastro!")
    print()
    input("tecle <ENTER> para prosseguir para o cadastro de livro...")
    cadastrar_es.cadastrar_produto_venda()
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  interfaces.cadastro()
  print()
  print("Finalizando cadastro de Venda.")
  print()
  print(f"##### Nome do Cliente: {nome_cliente_venda}")
  print()
  print(f"##### Livro Comprado: {livro_comprado}")
  print()
  unidades = len_vendas.ler_unidades()   
  print()
  valor = len_vendas.ler_valor()
  print()
  forma_pgto = len_vendas.ler_forma_pgto()
  ativo_venda = True
  arqv_vd.vendas[code_venda] = [data_venda, nome_cliente_venda, livro_comprado, unidades, valor, forma_pgto, ativo_venda] # Dados sendo guardados dentro do Dicionário vendas, onde o indeteficador daquele dado será o código da venda, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print(f"Venda cadastrada com sucesso sob código: {code_venda}")
  print()
  input("Tecle <ENTER> para continuar...")
#-----------------------------------------------