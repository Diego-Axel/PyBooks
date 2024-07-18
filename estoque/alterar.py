import os
import estoque.dicionario as arqv_es
import estoque.interfaces as interfaces
import estoque.len_estoque as len_estoque

#################################################
#####         ALTERAR DADOS PRODUTO         #####
#################################################

def alterar_produto():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  interfaces.alterar()
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
  verificador = True
  while verificador:
    os.system('celar || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_produto in arqv_es.produtos) and (arqv_es.produtos[code_produto][8]):
      print()
      interfaces.tabela_alteracao_produtos()
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
      resp = input("#### Qual dado deseja alterar (0 Para Cancelar)? ")
      resp = resp.upper()
      print()
      ativo_prd = True
      arqv_es.produtos[code_produto][8] = ativo_prd
      if (resp == "NOME") or (resp == "NOME DO LIVRO") or (resp == "LIVRO"):
        nome_livro = len_estoque.ler_nome()
        arqv_es.produtos[code_produto][0] = nome_livro
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "DESCRIÇÃO"):
        descricao = len_estoque.ler_descricao()
        arqv_es.produtos[code_produto][1] = descricao
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "AUTOR"):
        autor = len_estoque.ler_autor()
        arqv_es.produtos[code_produto][2] = autor
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "ANO"):
        ano = len_estoque.ler_ano()
        arqv_es.produtos[code_produto][3] = ano
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "TIPO DE CAPA") or (resp == "CAPA"):
        tipo_capa = len_estoque.ler_capa()
        arqv_es.produtos[code_produto][4] = tipo_capa
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "GENERO") or (resp == "GÊNERO") or (resp == "GÊNERO TEXTUAL"):
        genero = len_estoque.ler_genero()
        arqv_es.produtos[code_produto][5] = genero
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "QUANTIDADE EM ESTOQUE") or (resp == "QUANTIDADE") or (resp == "ESSTOQUE"):
        qtd_estoque = len_estoque.ler_qtd()
        arqv_es.produtos[code_produto][6] = qtd_estoque
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()
      elif (resp == "R$") or (resp == "VALOR") or (resp == "VALOR DO LIVRO"):
        valor_livro = len_estoque.ler_valor()
        arqv_es.produtos[code_produto][7] = valor_livro    
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_estoque.ler_decisao_alteracao()   
      elif (resp == "0"):
        print("Alteração Cancelada!")
        verificador = False 
    else:
      print()
      print("Produto inexistente ou deletado!")
      verificador = False
    print()
  input("Tecle <ENTER> para continuar...")
  #-----------------------------------------------