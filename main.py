############################################################
######       SISTEMA DE GESTÃO DE UMA LIVRARIA        ######
######  MATÉRIA: LÓGICA E ALGORITIMOS DE PROGRAMAÇÃO  ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################

# imports
import os

resp = ""
while resp != "0":
    os.system('clear || cls')
    print("############################################")
    print("######  Sistema de Gestão - Livraria  ######")
    print("############################################")
    print("#####      1 - Módulo Clientes         #####")
    print("#####      2 - Módulo Estoque          #####")
    print("#####      3 - Módulo Compras          #####")
    print("#####      4 - Módulo Vendas           #####")
    print("#####      5 - Módulo Livros/Mangas/HQ #####")
    print("#####      6 - Módulo Informações      #####")
    print("#####      0 - Sair                    #####")
    resp = input("##### Escolha sua opção: ")

    if resp == "1":
        print()
        print("############################################")
        print("#####   Você está no Módulo Clientes    ####")
        print("############################################")
        print()
        input("Tecle <ENTER> para continuar...")
    
    elif resp == "2":
      print()
      print("############################################")
      print("#####    Você está no Módulo Estoque    ####")
      print("############################################")
      print()
      input("Tecle <ENTER> para continuar...")

    elif resp == "3":
      print()
      print("############################################")
      print("#####    Você está no Módulo Compras    ####")
      print("############################################")
      print()
      input("Tecle <ENTER> para continuar...")

    elif resp == "4":
      print()
      print("############################################")
      print("#####     Você está no Módulo Vendas    ####")
      print("############################################")
      print()
      input("Tecle <ENTER> para continuar...")
      
    elif resp == "5":
      print()
      print("#################################################")
      print("#####  Você está no Módulo Livros/Mangas/HQ  ####")
      print("#################################################")
      print()
      input("Tecle <ENTER> para continuar...")
    
    elif resp == "6":
      print()
      print("############################################")
      print("#####  Você está no Módulo Informações  ####")
      print("############################################")
      print()
      print("##### Projeto de Gestão de uma Livraria ####")
      print("##### Desenvolvido por:                 ####")
      print("##### Diêgo Axel @diegoaxelbsr          ####")
      print("##### Projeto do curso de               ####")
      print("##### Sistemas de Informação - UFRN     ####")
      print("##### Licença Pública Geral GNU         ####")
      print("##### www.gnu.org/licenses/gpl.html     ####")
      print()
      input("Tecle <ENTER> para continuar...")

print()
print("Você encerrou o programa!")
print("Até logo!")