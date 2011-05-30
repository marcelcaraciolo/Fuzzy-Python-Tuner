

'''
Fuzzy logic functions

'''

__author__ = 'caraciol@gmail.com'

import math


class MatrizRegras(object):
	
	def obterRegras(self,diferenca, taxaMudanca):
		prioridade =  [0.0] * 9
		prioridade[0] = min (diferenca[0], taxaMudanca[0])
		prioridade[1] = min (diferenca[1], taxaMudanca[0])
		prioridade[2] = min (diferenca[2], taxaMudanca[0])
		prioridade[3] = min (diferenca[0], taxaMudanca[1])
		prioridade[4] = min (diferenca[1], taxaMudanca[1])
		prioridade[5] = min (diferenca[2], taxaMudanca[1])
		prioridade[6] = min (diferenca[0], taxaMudanca[2])
		prioridade[7] = min (diferenca[1], taxaMudanca[2])
		prioridade[8] = min (diferenca[2], taxaMudanca[2])

		return prioridade
		

def valorSaida(matrizRegras):
	
	esquerda =0.0
	direita = 0.0
	centro = 0.0
	saida = 0.0
	
	#sqrt(R0**2 + R3**2 + R6**2 + R7**2)
	esquerda = matrizRegras[0] ** 2 + matrizRegras[3] **  2 + matrizRegras[6] ** 2  + matrizRegras[7] ** 2
	esquerda = math.sqrt(esquerda)

	centro = matrizRegras[4]
	
	#sqrt(R1**2 + R2**2 + R5**2 + R8**2)
	direita = matrizRegras[1] ** 2 + matrizRegras[2] ** 2 + matrizRegras[5] ** 2 + matrizRegras[8] ** 2
	direita = math.sqrt(direita)
	
	'''
	   (neg_center * neg_strenght + centro_center * centro_strenght + pos_center * pos_strenght)
	   ----------------------------------------------------------------------------------------- 
	                    (neg_strenght + centro_strenght + pos_strenght)
	
	'''
	saida = ((-100) * esquerda + 0 * centro + (+100) * direita)	/ (esquerda + centro + direita);
	
	return saida
	
	

def funcaoPertinenciaFrequencia(frequencia,valorReferencia):
    pertinencia = [0.0,0.0,0.0]
    
    pertinencia[0] = desafinacaoEsquerda(frequencia,valorReferencia)
    pertinencia[1] = afinado(frequencia,valorReferencia)
    pertinencia[2] = desafinacaoDireita(frequencia,valorReferencia)

    return pertinencia
    
def desafinacaoEsquerda(frequencia,valorReferencia):
    if frequencia < - valorReferencia:
        return 1.0
    elif frequencia > 0:
        return 0.0
    else:
        return - 0.1 * frequencia  #y = ax+ b
    
def afinado(frequencia,valorReferencia):
    if frequencia <= -valorReferencia or frequencia >= valorReferencia:
        return 0.0
    elif frequencia > 0:
        return (-0.1 * frequencia +1)
    elif frequencia <= 0:
        return (0.1 * frequencia +1)
    else:
        return 0.0


def desafinacaoDireita(frequencia,valorReferencia):
    if frequencia > valorReferencia:
        return 1.0
    elif frequencia < 0:
        return 0.0
    else:
        return 0.1 * frequencia

def funcaoPertinenciaTaxaMudanca(frequencia,valorReferencia):
    pertinencia = [0.0,0.0,0.0]
    
    pertinencia[0] = desafinacaoEsquerdaTaxa(frequencia,valorReferencia)
    pertinencia[1] = afinadoTaxa(frequencia,valorReferencia)
    pertinencia[2] = desafinacaoDireitaTaxa(frequencia,valorReferencia)

    return pertinencia
    

def desafinacaoEsquerdaTaxa(frequencia,valorReferencia):
    if frequencia < - valorReferencia:
        return 1.0
    elif frequencia > 0:
        return 0.0
    else:
        return - 0.1 * frequencia  #y = ax+ b

def afinadoTaxa(frequencia,valorReferencia):
    if frequencia <= -valorReferencia or frequencia >= valorReferencia:
        return 0.0
    elif frequencia > 0:
        return (-0.1 * frequencia +1)
    elif frequencia <= 0:
        return (0.1 * frequencia +1)
    else:
        return 0.0


def desafinacaoDireitaTaxa(frequencia,valorReferencia):
    if frequencia > valorReferencia:
        return 1.0
    elif frequencia < 0:
        return 0.0
    else:
        return 0.1 * frequencia