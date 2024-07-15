import pickle

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