from BuscaDados import BuscaDados
from Esteira_jogador import Esteira
from Esteira_clubes import Partidas
from Filtragem import FiltragemJogadores, FiltragemJogosClubes

teste = FiltragemJogadores.Atacantes()
abc = Esteira.media_ponto(teste)
abc2 = Esteira.qtd_jogos(abc)
abc3 = Esteira.desvalorizou(abc2)
# print(abc3)
abc4 = Esteira.gols(abc3)
# print(abc4)
abc5 = Esteira.cartoes(abc4)
# print(abc5)
abc6 = Esteira.faltas(abc5)
print(abc6)
abc7 = Esteira.finalizacoes(abc6)
print(abc7)
abc8 = Esteira.assistencias(abc7)
print(abc8)
abc9 = Esteira.desarmes(abc8)
print(abc9)

abc10 = Esteira.mandante(abc9)
print(abc10)

abc11 = Esteira.libertadores(abc10)
print(abc11)

abc12 = Esteira.prelibertadores(abc11)
print(abc12)

abc13 = Esteira.sulamericana(abc12)
print(abc13)

abc14 = Esteira.neutros(abc13)
print(abc14)

abc15 = Esteira.rebaixamento(abc14)
print(abc15)

abc16 = Esteira.adversario(abc15)
print(abc16)

lista = []
for i in abc15:
    lista.append(i['score_robot'])
    if i['score_robot'] > 8:
        score = str(i['score_robot'])
        score = score[:4]
        print("O jogador " + i['apelido'] + " esta com " + score + " pontos")
    else:
        pass

lista_sort = sorted(lista, reverse=True)
x = 0
while x < 5:
    print(str(lista_sort[x]))
    x = x + 1


'''
jogos1 = FiltragemJogosClubes.Jogos()
print(jogos1)

clubes1 = FiltragemJogosClubes.Clubes()
print(clubes1)

mandantes = Partidas.mandantes(jogos1)
print(mandantes)

libertadores = Partidas.libertadores(clubes1)
print(libertadores)

preliberta = Partidas.pre_libertadores(clubes1)
print(preliberta)

sula = Partidas.sulamericana(clubes1)
print(sula)

neutro = Partidas.neutro(clubes1)
print(neutro)

z4 = Partidas.rebaixamento(clubes1)
print(z4)
'''
