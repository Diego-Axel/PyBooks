import pickle

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