import json
from BuscaDados import BuscaDados

lista = BuscaDados.jogadores()
lista = json.loads(lista)
lista = lista['atletas']
jogos = BuscaDados.partidas()

class FiltragemMercado():
    @classmethod
    def Statusmercado(cls):
        estado_mercado = BuscaDados.statusmercado()
        estado_mercado = json.loads(estado_mercado)
        estado_mercado = estado_mercado['status_mercado']
        return estado_mercado



class FiltragemJogadores():
    @classmethod
    def Provaveis(cls):
        provaveis = []
        for i in lista:
            if i['status_id'] == 7:
                provaveis.append(i)
            else:
                pass
        for i in provaveis:
            i['score_robot'] = 0
        return provaveis

    @classmethod
    def Atacantes(cls):
        provaveis = FiltragemJogadores.Provaveis()
        atacantes = []
        for i in provaveis:
            if i['posicao_id'] == 5:
                atacantes.append(i)
            else:
                pass
        return atacantes

    @classmethod
    def Meias(cls):
        provaveis = FiltragemJogadores.Provaveis()
        meias = []
        for i in provaveis:
            if i['posicao_id'] == 4:
                meias.append(i)
            else:
                pass
        return meias

    @classmethod
    def Zagueiros(cls):
        provaveis = FiltragemJogadores.Provaveis()
        zagueiros = []
        for i in provaveis:
            if i['posicao_id'] == 3:
                zagueiros.append(i)
            else:
                pass
        return zagueiros

    @classmethod
    def Laterais(cls):
        provaveis = FiltragemJogadores.Provaveis()
        laterais = []
        for i in provaveis:
            if i['posicao_id'] == 2:
                laterais.append(i)
            else:
                pass
        return laterais

    @classmethod
    def Goleiros(cls):
        provaveis = FiltragemJogadores.Provaveis()
        goleiros = []
        for i in provaveis:
            if i['posicao_id'] == 1:
                goleiros.append(i)
            else:
                pass
        return goleiros

    @classmethod
    def Tecnicos(cls):
        provaveis = FiltragemJogadores.Provaveis()
        tecnicos = []
        for i in provaveis:
            if i['posicao_id'] == 6:
                tecnicos.append(i)
            else:
                pass
        return tecnicos

class FiltragemJogosClubes():

    @classmethod
    def JogosClubes(cls):
        #jogosclubes = BuscaDados.partidas()
        jogosclubes = json.loads(jogos)
        #print(jogosclubes)
        return jogosclubes

    @classmethod
    def Jogos(cls):
        jogos = FiltragemJogosClubes.JogosClubes()
        #print(jogos['partidas'])
        return jogos['partidas']

    @classmethod
    def Clubes(cls):
        clubes = FiltragemJogosClubes.JogosClubes()
        #print(clubes['clubes'])
        return clubes['clubes']

#Filtragem.Atacantes()
