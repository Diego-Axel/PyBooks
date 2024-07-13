'''Arquivo das Funções das VENDAS'''

'''imports'''
import interfaces
import validadores
import len_vendas
import fun_cliente
import fun_estoque
import pickle
import os
import datetime
import time

'''Pegando a Data Atual'''
data = datetime.date.today()
dia = data.day
mes = data.month
ano = data.year

#################################################
#####           DICIONÁRIO VENDAS           #####
#################################################

vendas = {} # Dicionário onde sera Salvo os Dados das Vendas
try:
  arq_vendas = open("vendas.dat", "rb")
  vendas = pickle.load(arq_vendas)
except:
  arq_vendas = open("vendas.dat", "wb")
arq_vendas.close()

################################################
#####          DICIONÁRIO CLIENTES         #####
################################################

clientes = {}  # Dicionário onde sera Salvo os Dados dos Clientes
try:
  arq_clientes = open("clientes.dat", "rb")
  clientes = pickle.load(arq_clientes)
except:
  arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()

#################################################
#####          DICIONÁRIO ESTOQUE           #####
#################################################

produtos = {} # Dicionário onde sera Salvo os Dados dos Produtos(Livros)
try:
  arq_produtos = open("produtos.dat", "rb")
  produtos = pickle.load(arq_produtos)
except:
  arq_produtos = open("produtos.dat", "wb")
arq_produtos.close()

#################################################
#####          FUNÇÕES DAS VENDAS           #####
#################################################
#-----------------------------------------------

#################################################
#####            CADASTRAR VENDA            #####
#################################################

def cadastrar_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("############################################")
  print("#####         Cadastrar Venda          #####")
  print("#####       <ENTER> - Prosseguir       #####")
  print("#####           0 - Cancelar           #####")
  print("############################################")
  print()
  confirmacao = input("Entrando em 'Cadastro de Venda' -> Digite '0' Para Cancelar e <ENTER> para prosseguir: ")
  if confirmacao == "0":
    return
  else:
    print("Iniciando cadastro.")
    time.sleep(3)
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("############################################")
  print("#####         Cadastrar Venda          #####")
  print("############################################")
  print()
  code_venda = len(vendas) + 1
  data_venda = len_vendas.ler_data()
  print()
  nome_cliente_venda = len_vendas.ler_nome()
  cliente_encontrado = False
  for cliente in clientes.values(): # Verificando se o nome do cliente inserido está presente no dicionário 'Clientes'
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
    fun_cliente.cadastrar_cliente_venda()
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("############################################")
  print("#####         Cadastrar Venda          #####")
  print("############################################")
  print()
  print("##### Cliente Cadastrado! Por favor, continue o cadastro da venda.")
  print()
  print(f"##### Nome do Cliente: {nome_cliente_venda}")
  print()
  livro_comprado = len_vendas.ler_livro()
  livro_encontrado = False
  for livro in produtos.values():
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
    fun_estoque.cadastrar_produto_venda()
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print("############################################")
  print("#####         Cadastrar Venda          #####")
  print("############################################")
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
  vendas[code_venda] = [data_venda, nome_cliente_venda, livro_comprado, unidades, valor, forma_pgto, ativo_venda] # Dados sendo guardados dentro do Dicionário vendas, onde o indeteficador daquele dado será o código da venda, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print(f"Venda cadastrada com sucesso sob código: {code_venda}")
  print()
  input("Tecle <ENTER> para continuar...")
#-----------------------------------------------


#################################################
#####         EXIBIR DADOS DA VENDA         #####
#################################################

def exibir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados de Vendas      #####")
    print("#####        0 - Para Retornar         #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_venda = int(input("##### Digite o Código de Venda ou Digite '0' Para Retornar: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if code_venda == 0:
      return
    if (code_venda in vendas) and (vendas[code_venda][6]):
      print()
      interfaces.tabela_venda()
      print("| %-10s "%(vendas[code_venda][0]), end="") # 1
      print("| %-43s "%(vendas[code_venda][1]), end="") # 2
      print("| %-43s "%(vendas[code_venda][2]), end="") # 3
      print("| %-2s "%(vendas[code_venda][3]), end="")  # 4
      print("| %-6s "%(vendas[code_venda][4]), end="")  # 5
      print("| %-10s "%(vendas[code_venda][5]))         # 6
      print("-------------------------------------------------------------------------------------------------------------------------------------")
    else:
      print()
      print("Venda inexistente ou deletada!")
      print()
    resp = input("tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes: ")
  print()
#-----------------------------------------------


#################################################
#####          ALTERAR DADOS VENDA          #####
#################################################

def alterar_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####      Alterar Dados de Venda      #####")
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
  verificador = True
  while verificador:
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_venda in vendas) and (vendas[code_venda][6]):
      print()
      interfaces.tabela_alteracao_vendas()
      print("| %-10s "%(vendas[code_venda][0]), end="") # 1
      print("| %-43s "%(vendas[code_venda][1]), end="") # 2
      print("| %-43s "%(vendas[code_venda][2]), end="") # 3
      print("| %-2s "%(vendas[code_venda][3]), end="")  # 4
      print("| %-6s "%(vendas[code_venda][4]), end="")  # 5
      print("| %-10s "%(vendas[code_venda][5]))         # 6
      print("-------------------------------------------------------------------------------------------------------------------------------------")
      print()
      resp = input("#### Qual dado deseja alterar? ")
      resp = resp.upper()
      print()
      ativo_venda = True
      vendas[code_venda][6] = ativo_venda
      if (resp == "DATA DE VENDA") or (resp == "DATA") or (resp == "DATA VENDA"):
        data_venda = validadores.validar_data()
        vendas[code_venda][0] = data_venda
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "NOME DO CLIENTE") or (resp == "NOME CLIENTE") or (resp == "CLIENTE") or (resp == "COMPRADOR") or (resp == "NOME DO COMPRADOR"):    
        nome_cliente_venda = len_vendas.ler_nome()
        vendas[code_venda][1] = nome_cliente_venda
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "LIVRO COMPRADO") or (resp == "LIVRO") or (resp == "NOME DO LIVRO"):
        livro_comprado = len_vendas.ler_livro()
        vendas[code_venda][2] = livro_comprado
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "UNIDADES") or (resp == "UNIDADES ADQUIRIDAS") or (resp == "UNIDADES VENDIDAS") or (resp == "UN"):
        unidades = len_vendas.ler_unidades()
        vendas[code_venda][3] = unidades
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "VALOR R$") or (resp == "VALOR DE VENDA") or (resp == "R$") or (resp == "VALOR"):
        valor = len_vendas.ler_valor()
        vendas[code_venda][4] = valor
        print()
        interfaces.confirmar_alteracao()
        print()
        verificador = len_vendas.ler_decisao_alteracao()
      elif (resp == "FORMA DE PAGAMENTO") or (resp == "PAGAMENTO") or (resp == "Forma Pgt") or (resp == "Forma Pgt."):
        forma_pgto = len_vendas.ler_forma_pgto()
        vendas[code_venda][5] = forma_pgto
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
  if (code_venda in vendas) and (vendas[code_venda][6]):
    print()
    interfaces.tabela_venda()
    print("| %-10s "%(vendas[code_venda][0]), end="") # 1
    print("| %-43s "%(vendas[code_venda][1]), end="") # 2
    print("| %-43s "%(vendas[code_venda][2]), end="") # 3
    print("| %-2s "%(vendas[code_venda][3]), end="")  # 4
    print("| %-6s "%(vendas[code_venda][4]), end="")  # 5
    print("| %-10s "%(vendas[code_venda][5]))         # 6
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print()
    decisao = input("Tem certeza que deseja EXCLUIR essa Venda (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      vendas[code_venda][6] = False
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


#################################################
#####          RELATÓRIO DE VENDAS          #####
#################################################

def relatorio_vendas_on():   
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls' 
  interfaces.tabela_relatorio_vendas_atv()
  for code_venda in vendas:
    if vendas[code_venda][6]:
      print("| %-3s "%(code_venda), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-10s "%(vendas[code_venda][0]), end="") # 2
      print("| %-43s "%(vendas[code_venda][1]), end="") # 3
      print("| %-43s "%(vendas[code_venda][2]), end="") # 4
      print("| %-2s "%(vendas[code_venda][3]), end="")  # 5
      print("| %-6s "%(vendas[code_venda][4]), end="")  # 6
      print("| %-10s "%(vendas[code_venda][5]))         # 7
  print("------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------


#########################################################
#####          RELATÓRIO DE VENDAS DELETADAS        #####
#########################################################

def relatorio_vendas_off():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  interfaces.tabela_relatorio_vendas_intv()
  for code_venda in vendas:
    if vendas[code_venda][6] == False:
      print("| %-3s "%(code_venda), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-10s "%(vendas[code_venda][0]), end="") # 2
      print("| %-43s "%(vendas[code_venda][1]), end="") # 3
      print("| %-43s "%(vendas[code_venda][2]), end="") # 4
      print("| %-2s "%(vendas[code_venda][3]), end="")  # 5
      print("| %-6s "%(vendas[code_venda][4]), end="")  # 6
      print("| %-10s "%(vendas[code_venda][5]))         # 7
  print("------------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")
#-----------------------------------------------


###################################################
#####         SALVANDO DADOS - VENDAS         #####
###################################################

def salvar_dados_vendas():
  arq_vendas = open("vendas.dat", "wb")
  pickle.dump(vendas, arq_vendas)
  arq_vendas.close()