from random import *

print('_.'*20)
print('\nJOGO DE ANALOGRAMA')
print('_.'*20) 


print('DICA:FRUTAS\n')
print('São ao todo dez frutas.Mais so podera digitar 5 delas...\nSe ACERTAR ganha 1 ponto,Se ERRAR perde 1 ponto\n')
print('BOA SORTE !!')

print('..INICIANDO..\n')
from contador import conta
def embaralha(palavras):
    
    embaralha_palavra=sample(palavras,len(palavras))
    
    reune_palavra=' '.join(embaralha_palavra)
    
    print(reune_palavra)

palavras='ameixaamorajabuticaba\nmelanciaacerolapitanga\nabacaxilimaotangerina'
lista_palavras=['ameixa','amora','jabuticaba','melancia','acerola','pitanga','abacaxi','limao','tangerina','morango']
embaralha(palavras)

contador=0

contador_acertos=0
while contador<5:
    chute=input('\ndigite: ')
    

    if chute in lista_palavras:
        print('vc acertou!!')
        
        contador_acertos+=1
        print('Pontos',contador_acertos)
    elif chute!=lista_palavras:
        print('vc errou!!')
        contador_acertos-=1
        print('Pontos',contador_acertos)
    contador= contador +1 
    
if contador_acertos==5:
    print('**PARABENS!!..VOCÊ ACERTOU TODAS**\n')

print(f'FIM!!!...total de pontos {contador_acertos}')