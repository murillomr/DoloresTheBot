from BuscaDados import BuscaDados
from Esteira_jogador import Esteira
from Esteira_clubes import Partidas
from Filtragem import FiltragemJogadores, FiltragemJogosClubes

teste = FiltragemJogadores.Atacantes()
abc = Esteira.media_ponto(teste)
abc2 = Esteira.qtd_jogos(abc)
abc3 = Esteira.desvalorizou(abc2)
#print(abc3)
abc4 = Esteira.gols(abc3)
#print(abc4)
abc5 = Esteira.cartoes(abc4)
#print(abc5)
abc6 = Esteira.faltas(abc5)
print(abc6)
abc7 = Esteira.finalizacoes(abc6)
print(abc7)
abc8 = Esteira.assistencias(abc7)
print(abc8)
abc9 = Esteira.desarmes(abc8)
print(abc9)


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