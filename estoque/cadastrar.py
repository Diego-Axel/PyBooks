import os
import time
import estoque.dicionario as arqv_es
import estoque.len_estoque as len_estoque

#################################################
#####           CADASTRAR PRODUTO           #####
#################################################

def cadastrar_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Produto         #####")
  print("#####       <ENTER> - Prosseguir       #####")
  print("#####           0 - Cancelar           #####")
  print("############################################")
  print()
  confirmacao = input("Entrando em 'Cadastro de Produto' -> Digite '0' Para Cancelar e <ENTER> para prosseguir: ")
  if confirmacao == "0":
    return
  else:
    print("Iniciando cadastro.")
    time.sleep(3)
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Produto         #####")
  print("############################################")
  print()
  code_produto = len(arqv_es.produtos) + 1
  print()
  nome_livro = len_estoque.ler_nome()
  print()
  descricao = len_estoque.ler_descricao()
  print()
  autor = len_estoque.ler_autor()
  print()
  ano = len_estoque.ler_ano()
  print()
  tipo_capa = len_estoque.ler_capa()
  print()
  genero = len_estoque.ler_genero()
  print()
  qtd_estoque = len_estoque.ler_qtd()
  print()
  valor_livro = len_estoque.ler_valor()
  print()
  ativo_prd = True
  arqv_es.produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque, valor_livro, ativo_prd] # Dados sendo guardados dentro do Dicionário produtos, onde o indeteficador daquele dado será o código do Produto, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print(f"Produto cadastrado com sucesso sob código: {code_produto}")
  print()
  input("Tecle <ENTER> para continuar...")
  #-----------------------------------------------


#########################################################
#####           CADASTRAR PRODUTO NA VENDA          #####
#########################################################

def cadastrar_produto_venda(): # Estou usando essa função no meu arquivo de vendas, para cadastro de produto se o mesmo não possuir cadastro
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####        Cadastrar Produto         #####")
  print("############################################")
  print()
  code_produto = len(arqv_es.produtos) + 1
  print()
  nome_livro = len_estoque.ler_nome()
  print()
  descricao = len_estoque.ler_descricao()
  print()
  autor = len_estoque.ler_autor()
  print()
  ano = len_estoque.ler_ano()
  print()
  tipo_capa = len_estoque.ler_capa()
  print()
  genero = len_estoque.ler_genero()
  print()
  qtd_estoque = len_estoque.ler_qtd()
  print()
  valor_livro = len_estoque.ler_valor()
  print()
  ativo_prd = True
  arqv_es.produtos[code_produto] = [nome_livro, descricao, autor, ano, tipo_capa, genero, qtd_estoque, valor_livro, ativo_prd] # Dados sendo guardados dentro do Dicionário produtos, onde o indeteficador daquele dado será o código do Produto, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print()
  print(f"Produto cadastrado com sucesso sob código: {code_produto}")
  print()
  input("Tecle <ENTER> para continuar...")
  #-----------------------------------------------