

'''
Fuzzy logic functions

'''

__author__ = 'caraciol@gmail.com'

import math
from fuzzy import *

ultimo_erro = 0.0
m = MatrizRegras()

def ajustar_saida(frequencia,feedback,valorReferencia):
    global ultimo_erro
    diferenca = frequencia = abs(feedback)
    taxa_de_mudanca = diferenca - ultimo_erro
    
    #Atualiza ultimo erro
    ultimo_erro = diferenca
    
    #Calcula os arrays com funcao de pertinencia de error e errorDot
    pertinenciaFrequencia = funcaoPertinenciaFrequencia(diferenca,valorReferencia)
    pertinenciaTaxa = funcaoPertinenciaTaxaMudanca(taxa_de_mudanca,valorReferencia)
    
    #Determina Foras de Disparo
    matrizPrioridades = m.obterRegras(pertinenciaFrequencia, pertinenciaTaxa)
    
    output = valorSaida(matrizPrioridades)
    
    
    #Calcula resposta do Sistema
    print '---------------------'
    print 'diferenca %f' % diferenca
    print 'abs(feedback)  %f'  % abs(feedback)
    
    return output
    


if __name__ == '__main__':
    
    '''
     * E2 - 82.407  (E)
     * A2 - 110  (A)
     * D3 - 146.83 (D)
     * G3 - 196  (G)
     * B3 - 246.94  (B)
     * E4 - 329.63  (E)
    '''
    
    frequencia = 5
    frequenciaDesejada = 0
    valorReferencia = 2
    acaoAfinar = ''
    
    for i in range(1000):
        print '---------------------------------'
        print 'frequencia %f'  %  frequencia
        correcao = ajustar_saida(frequenciaDesejada,frequencia,valorReferencia)
        frequencia = frequencia + (frequencia * (correcao/1000))
        print 'correcao %f' % correcao
        print 'nova frequencia %f' % frequencia
        
        if frequencia > frequenciaDesejada:
            acaoAfinar = 'Apert'
        else:
            acaoAfinar = 'Afroux'
        
        if correcao > 20:
            print   'Pode ' +  acaoAfinar + 'ar um bocado'
        
        elif correcao > 10:
            print   'Pode ' +  acaoAfinar + 'e um pouco'

        elif correcao > 5:
            print   'Pode ' +  acaoAfinar + 'e so mais um pouquinho'
            
        elif correcao > 2:
            print   'Pode ' +  acaoAfinar + 'e so mais um pouquinho de nada'

        else:
            print 'Agora ta afinado!'