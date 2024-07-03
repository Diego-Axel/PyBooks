'''Arquivo das Funções de CLIENTES'''

'''imports'''
import validadores
import pickle
import os
import time

#################################################
#####          DICIONÁRIO CLIENTE           #####
#################################################

clientes = {}  # Dicionário onde sera Salvo os Dados dos Clientes
try:
  arq_clientes = open("clientes.dat", "rb")
  clientes = pickle.load(arq_clientes)
except:
  arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()

#################################################
#####          FUNÇÕES DE CLIENTES          #####
#################################################
#-----------------------------------------------

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
  code_cliente = len(clientes) + 1
  nome_cliente = input("##### Nome: ")
  print()
  verificador = True # Maneira de usar while atraves de variaveis que guardam operadoes lógicos, dica de Matheus Diniz.
  while verificador:
    email = input("#### E-mail: ")
    if validadores.validar_email(email):
      print("E-mail válido!")
      verificador = False
    else:
      print("O e-mail não é válido, veja se você não esquceu o '@'/domínio/'.com'. Por favor digite novamente.")
      print()
  print()
  verificador = True
  while verificador:
    print("##### Digite o Celular com DDD e o 9 adicional seguinddo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
    celular = input("##### Digite seu Celular: ")
    if validadores.validar_numero(celular):
      print("Numero válido!")
      verificador = False
    else:
      print("Número não válido. Digite um número válido.")
  print()
  cpf = input("##### CPF: ")
  print()
  ativo = True
  clientes[code_cliente] = [nome_cliente, email, celular, cpf, ativo] # Dados sendo guardados dentro do Dicionário Clientes, onde o indeteficador daquele dado será o código do Cliente, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
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
  code_cliente = len(clientes) + 1
  nome_cliente = input("##### Nome: ")
  print()
  verificador = True # Maneira de usar while atraves de variaveis que guardam operadoes lógicos, dica de Matheus Diniz.
  while verificador:
    email = input("#### E-mail: ")
    if validadores.validar_email(email):
      print("E-mail válido!")
      verificador = False
    else:
      print("O e-mail não é válido, veja se você não esquceu o '@'/domínio/'.com'. Por favor digite novamente.")
      print()
  print()
  verificador = True
  while verificador:
    print("##### Digite o Celular com DDD e o 9 adicional seguinddo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
    celular = input("##### Digite seu Celular: ")
    if validadores.validar_numero(celular):
      print("Numero válido!")
      verificador = False
    else:
      print("Número não válido. Digite um número válido.")
  print()
  cpf = input("##### CPF: ")
  print()
  ativo = True
  clientes[code_cliente] = [nome_cliente, email, celular, cpf, ativo] # Dados sendo guardados dentro do Dicionário Clientes, onde o indeteficador daquele dado será o código do Cliente, que aqui, funciona como um chave do tipo SERIAL, é única e não se repete
  print(f"Cliente cadastrado com sucesso sob código: {code_cliente}")
  print()
  input("Tecle <ENTER> para continuar...")
  #---------------------------------------------------------------------


#################################################
#####          EXIBIR DADOS CLIENTE         #####
#################################################

def exibir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  resp = ""
  while resp != "0":
    os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    print()
    print("############################################")
    print("#####      Exibir Dados do Cliente     #####")
    print("############################################")
    print("##### 0 - Retornar ao Menu Clientes    #####")
    print("############################################")
    print()
    verificador = True
    while verificador:
      try:
        code_cliente = int(input("##### Digite o Código do Cliente: "))
        verificador = False
      except ValueError:
        print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
    if code_cliente == 0:
      return
    if (code_cliente in clientes) and (clientes[code_cliente][4]):
      print()
      print("#################################################################################################################################")
      print("#################################################       Dados do Cliente        #################################################")
      print("#################################################################################################################################")
      print("|---------------------------------------------|---------------------------------------------|------------------|----------------|")
      print("|                Nome Completo                |                    E-mail                   |      Celular     |       CPF      |")
      print("|---------------------------------------------|---------------------------------------------|------------------|----------------|")
      print("| %-43s "%(clientes[code_cliente][0]), end='') # 1
      print("| %-43s "%(clientes[code_cliente][1]), end='') # 2
      print("| %-16s "%(clientes[code_cliente][2]), end='') # 3
      print("| %-13s "%(clientes[code_cliente][3]))         # 4
      print("---------------------------------------------------------------------------------------------------------------------------------")
      print()
    else:
        print("Cliente inexistente ou inativo!")
        print()
    resp = input("tecle <ENTER> para continuar ou 0 para retornar ao Menu Clientes: ")
  print()
   #---------------------------------------------------------------------


#################################################
#####         ALTERAR DADOS CLIENTE         #####
#################################################

def alterar_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####     Alterar Dados do Cliente     #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_cliente = int(input("##### Digite o Código do Cliente: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  verificador = True
  while verificador:
    os.system('celar || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
    if (code_cliente in clientes) and (clientes[code_cliente][4]):
      print()
      print("#################################################################################################################################")
      print("#################################################       Dados do Cliente        #################################################")
      print("#################################################       0 - Para Cancelar       #################################################")
      print("#################################################################################################################################")
      print("|---------------------------------------------|---------------------------------------------|------------------|----------------|")
      print("|                Nome Completo                |                    E-mail                   |      Celular     |       CPF      |")
      print("|---------------------------------------------|---------------------------------------------|------------------|----------------|")
      print("| %-43s "%(clientes[code_cliente][0]), end='') # 1
      print("| %-43s "%(clientes[code_cliente][1]), end='') # 2
      print("| %-16s "%(clientes[code_cliente][2]), end='') # 3
      print("| %-13s "%(clientes[code_cliente][3]))         # 4
      print("---------------------------------------------------------------------------------------------------------------------------------")
      print()        
      resp = input("#### Qual dado deseja alterar (0 Para Cancelar)? ")
      resp = resp.upper()
      print()
      ativo = True
      clientes[code_cliente][4] = ativo
      if (resp == "NOME"):
        nome_cliente = input("##### Digite o novo nome: ")
        clientes[code_cliente][0] = nome_cliente
        print("Dado alterado com sucesso!")
        print("--------------------------")
        print()
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "E-MAIL") or (resp == "EMAIL"):
        verificador = True
        while verificador:
          email = input("##### Digite o novo e-mail: ")
          if validadores.validar_email(email):
            print("E-mail válido e alterado com sucesso!")
            print("-------------------------------------")
            print()
            clientes[code_cliente][1] = email
            verificador = False
          else:
            print("O e-mail não é válido, veja se você não esquceu o '@'/domínio/'.com'. Por favor digite novamente.")
            print()
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "CELULAR") or (resp == "TELEFONE"):
        verificador = True
        while verificador:
          print("##### Digite o novo, lembre-se Celular com DDD e o 9 adicional seguinddo este exemplo: (xx) xxxxx-xxxx (NÚMERO DE EXEMPLO)")
          celular = input("##### Novo Celular: ")
          if validadores.validar_numero(celular):
            print("Número válido e alterado com sucesso!")
            print("-------------------------------------")
            clientes[code_cliente][2] = celular
            verificador = False
          else:
            print("Número não válido. Digite um número válido.")
        resp = input("#### Deseja Alterar mais dados(S/N)? ")
        resp = resp.upper()
        if (resp == "NÃO") or (resp == "NAO") or (resp == "N"):
          verificador = False
          print()
        else:
          print()
          verificador = True
      elif (resp == "CPF"):
        cpf = input("##### Digite o novo CPF: ")
        print("Dado alterado com sucesso!")
        print("--------------------------")
        clientes[code_cliente][3] = cpf
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
      print("Cliente inexistente ou inativo!")   
      verificador = False 
  print()
  input("Tecle <ENTER> para continuar...")
#---------------------------------------------------------------------


#################################################
#####         EXCLUIR DADOS CLIENTE         #####
#################################################

def excluir_cliente():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("############################################")
  print("#####          Excluir Cliente         #####")
  print("############################################")
  print()
  verificador = True
  while verificador:
    try:
      code_cliente = int(input("##### Digite o Código do Cliente: "))
      verificador = False
    except ValueError:
      print("!!!! Resposta não reconhecida como um número INTEIRO. Tente novamente.")
  if (code_cliente in clientes) and (clientes[code_cliente][4]):
    print()
    print("#################################################################################################################################")
    print("#################################################       Dados do Cliente        #################################################")
    print("#################################################################################################################################")
    print("|---------------------------------------------|---------------------------------------------|------------------|----------------|")
    print("|                Nome Completo                |                    E-mail                   |      Celular     |       CPF      |")
    print("|---------------------------------------------|---------------------------------------------|------------------|----------------|")
    print("| %-43s "%(clientes[code_cliente][0]), end='') # 1
    print("| %-43s "%(clientes[code_cliente][1]), end='') # 2
    print("| %-16s "%(clientes[code_cliente][2]), end='') # 3
    print("| %-13s "%(clientes[code_cliente][3]))         # 4
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print()
    decisao = input(" -> Tem certeza que deseja EXCLUIR esse Cliente (S/N)? ")
    decisao = decisao.upper()
    if (decisao == "SIM") or (decisao == "S"):
      print()
      '''
      Para não acontecer de, ser excluido um cliente de cód 2, exemplo, e quando for cadastrar outro cliente, esse cliente não pegar
      o mesmo cód que foi excluido, deixando um pouco bagunçado... Cada cliente fica com um ativo em seus dados, estiver on = True, for excluído, ativo = False -> Assim, o cód_cliente é unico e não se repete!      

      '''
      clientes[code_cliente][4] = False 
      print("Cliente excluído(a) com sucesso!")
    else:
      print("Exclusão não realizada!")
  else:
    print("Cliente inexistente ou inativo!")
    print()
  print()
  input("Tecle <ENTER> para continuar...")  
#---------------------------------------------------------------------


#################################################
#####       RELATÓRIO CLIENTES ATIVOS       #####
#################################################

def relatorio_clientes_on():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("#######################################################################################################################################")
  print("#################################################     Relatório de Clientes Ativos        #############################################")
  print("#######################################################################################################################################")
  print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
  print("| Cod |               Nome Completo                 |                    E-mail                   |      Celular     |       CPF      |")
  print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
  for code_cliente in clientes:
    if clientes[code_cliente][4]:
      print("| %-3s "%(code_cliente), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(clientes[code_cliente][0]), end='') # 2
      print("| %-43s "%(clientes[code_cliente][1]), end='') # 3
      print("| %-16s "%(clientes[code_cliente][2]), end='') # 4
      print("| %-14s "%(clientes[code_cliente][3]))         # 5
  print("--------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")    
#---------------------------------------------------------------------


###################################################
#####       RELATÓRIO CLIENTES INATIVOS       #####
###################################################

def relatorio_clientes_off():
  os.system('clear || cls') # se for Linux use 'clear' e se for Windowns use 'cls'
  print()
  print("#######################################################################################################################################")
  print("#################################################     Relatório de Clientes Inativos      #############################################")
  print("#######################################################################################################################################")
  print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
  print("| Cod |               Nome Completo                 |                    E-mail                   |      Celular     |       CPF      |")
  print("|-----|---------------------------------------------|---------------------------------------------|------------------|----------------|")
  for code_cliente in clientes:
    if clientes[code_cliente][4] == False:
      print("| %-3s "%(code_cliente), end="") # Para o %-3s(expl) é so pegar esses traçoes '-' e a contagem deles diminuir de 2.
      print("| %-43s "%(clientes[code_cliente][0]), end='') # 2
      print("| %-43s "%(clientes[code_cliente][1]), end='') # 3
      print("| %-16s "%(clientes[code_cliente][2]), end='') # 4
      print("| %-14s "%(clientes[code_cliente][3]))         # 5
  print("--------------------------------------------------------------------------------------------------------------------------------------")
  print()
  input("tecle <ENTER> para continuar...")          
  #---------------------------------------------------------------------


###################################################
#####        SALVANDO DADOS - CLIENTES        #####
###################################################

def salvar_dados_clientes():
  arq_clientes = open("clientes.dat", "wb")
  pickle.dump(clientes, arq_clientes)
  arq_clientes.close()