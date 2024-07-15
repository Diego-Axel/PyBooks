import pickle

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