import pickle
import estoque.dicionario as arqv_es

###################################################
#####        SALVANDO DADOS - PRODUTOS        #####
###################################################

def salvar_dados_produtos():
  arq_produtos = open("produtos.dat", "wb")
  pickle.dump(arqv_es.produtos, arq_produtos)
  arq_produtos.close()