'''Arquivo das Funções das VENDAS'''

'''imports'''
import pickle
import os
import datetime

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
  print("############################################")
  print()
  code_venda = len(vendas) + 1
  data_venda = ("%02d/%02d/%d"%(dia, mes, ano))
  print()
  nome_cliente_venda = input("##### Nome do Cliente: ")
  print()
  livro_comprado = input("##### Nome do Livro Comprado: ")
  print()
  verificador = True
  while verificador:
    try:
      unidades = int(input("##### Unidades Vendidas (NÚMERO INTEIRO): "))
      verificador = False
    except ValueError:
      print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
  print()
  verificador = True
  while verificador:
    try:
      valor = float(input("##### Valor de Venda (R$ -> DECIMAL): "))
      verificador = False
    except ValueError:
      print("!!! Resposta não reconhecida como número DECIMAL(R$). Tente novamente !!!")
  print()
  forma_pgto = input("##### Forma de pagamento: ")
  ativo_venda = True
  print()
  vendas[code_venda] = [data_venda, nome_cliente_venda, livro_comprado, unidades, valor, forma_pgto, ativo_venda] # Dados sendo guardados dentro do Dicionário vendas, onde o indeteficador daquele dado será o código da venda, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print()
  print("Venda cadastrada com sucesso!")
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
    print("############################################")
    print("##### 0 - Retornar ao Menu Vendas      #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_venda = int(input("##### Digite o Código de Venda: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if code_venda == 0:
      return
    if (code_venda in vendas) and (vendas[code_venda][6]):
      print()
      print("#####################################################################################################################################")
      print("##########################################               Dados da Venda              ################################################")
      print("#####################################################################################################################################")
      print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
      print("| Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
      print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
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
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_venda = int(input("##### Digite o Código da Venda: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  verificador = True
  while verificador:
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_venda in vendas) and (vendas[code_venda][6]):
      print()
      print("#####################################################################################################################################")
      print("##########################################               Dados da Venda              ################################################")
      print("##########################################              0 - Para Cancelar            ################################################")
      print("#####################################################################################################################################")
      print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
      print("| Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
      print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
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
        data_venda = ("%02d/%02d/%d"%(dia, mes, ano))
        print("Data modificada para o dia de hoje!")
        print("-----------------------------------")
        print()
        vendas[code_venda][0] = data_venda
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "NOME DO CLIENTE") or (resp == "NOME CLIENTE") or (resp == "CLIENTE") or (resp == "COMPRADOR") or (resp == "NOME DO COMPRADOR"):    
        nome_cliente_venda = input("##### Digite o nome do Cliente: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        vendas[code_venda][1] = nome_cliente_venda
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "LIVRO COMPRADO") or (resp == "LIVRO") or (resp == "NOME DO LIVRO"):
        livro_comprado = input("##### Digite o nome do livro Comprado: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        vendas[code_venda][2] = livro_comprado
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "UNIDADES") or (resp == "UNIDADES ADQUIRIDAS") or (resp == "UNIDADES VENDIDAS") or (resp == "UN"):
        verificador = True
        while verificador:
          try:
            unidades = int(input("##### Unidades Vendidas (NÚMERO INTEIRO): "))
            print("Dado alterado com sucesso!")
            print("--------------------------")
            vendas[code_venda][3] = unidades
            verificador = False
          except ValueError:
            print("!!! Resposta não reconhecida como número INTEIRO. Tente novamente !!!")
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "VALOR R$") or (resp == "VALOR DE VENDA") or (resp == "R$") or (resp == "VALOR"):
        verificador = True
        while verificador:
          try:
            valor = float(input("##### Valor de Venda (R$ -> DECIMAL): "))
            print("Dado alterado com sucesso!")
            print("--------------------------")
            print()
            vendas[code_venda][4] = valor
            verificador = False
          except ValueError:
            print("!!! Resposta não reconhecida como número DECIMAL(R$). Tente novamente !!!")
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "FORMA DE PAGAMENTO") or (resp == "PAGAMENTO") or (resp == "Forma Pgt") or (resp == "Forma Pgt."):
        forma_pgto = input("##### Digite a Forma de pagamento: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        vendas[code_venda][5] = forma_pgto
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
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

def excluir_venda():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####           Excluir Venda          #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_venda = int(input("##### Digite o Código da Venda: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  if (code_venda in vendas) and (vendas[code_venda][6]):
    print()
    print("#####################################################################################################################################")
    print("##########################################               Dados da Venda              ################################################")
    print("#####################################################################################################################################")
    print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
    print("| Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
    print("|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
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
      '''
      Para não acontecer de, ser excluido uma venda de cód 2, exemplo, e quando for cadastrar outra venda, essa venda não pegar
      o mesmo cód que foi excluido, deixando um pouco bagunçado... Cada venda fica com um ativo em seus dados, estiver on = True, for excluído, ativo = False -> Assim, o cód_venda é unico e não se repete!

      '''
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
  print("###########################################################################################################################################")
  print("############################################            Relatório de Vendas            ####################################################")
  print("###########################################################################################################################################")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
  print("| Cod | Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
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
  print("###########################################################################################################################################")
  print("##########################################           Relatório de Vendas  Deletadas         ###############################################")
  print("###########################################################################################################################################")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
  print("| Cod | Data Venda |        Nome do Cliente/Comprador            |                 Livro Comprado              | UN |   R$   | Forma Pgt. |")
  print("|-----|------------|---------------------------------------------|---------------------------------------------|----|--------|------------|")
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