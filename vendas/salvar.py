import pickle
import vendas.dicionario as arqv_vd

###################################################
#####         SALVANDO DADOS - VENDAS         #####
###################################################

def salvar_dados_vendas():
  arq_vendas = open("vendas.dat", "wb")
  pickle.dump(arqv_vd.vendas, arq_vendas)
  arq_vendas.close()