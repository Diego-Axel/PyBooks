import pickle
import clientes.dicionario as arqv_cl # -> arquivo cliente

###################################################
#####        SALVANDO DADOS - CLIENTES        #####
###################################################

def salvar_dados_clientes():
  arq_clientes = open("clientes.dat", "wb")
  pickle.dump(arqv_cl.clientes, arq_clientes)
  arq_clientes.close()