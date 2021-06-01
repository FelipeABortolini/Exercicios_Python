from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dados

preco = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(preco, 80, 30)
