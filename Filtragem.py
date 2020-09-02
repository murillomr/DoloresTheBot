import json
from BuscaDados import BuscaDados

class FiltragemMercado():
    @classmethod
    def Statusmercado(cls):
        estado_mercado = BuscaDados.statusmercado()
        estado_mercado = json.loads(estado_mercado)
        estado_mercado = estado_mercado['status_mercado']
        #retorna "1" em caso de mercado aberto
        return estado_mercado

class FiltragemJogadores():
    @classmethod
    def Provaveis(cls):
        lista = BuscaDados.jogadores()
        lista = json.loads(lista)
        lista = lista['atletas']
        print(lista)
        provaveis = []
        for i in lista:
            if i['status_id'] == 7:
                provaveis.append(i)
            else:
                pass
        for i in provaveis:
            i['score_robot'] = 0
        print(provaveis)
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
        print(atacantes)
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
        print(meias)
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
        print(zagueiros)
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
        print(laterais)
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
        print(goleiros)
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
        print(tecnicos)
        return tecnicos



class FiltragemJogosClubes():

    @classmethod
    def JogosClubes(cls):
        jogosclubes = BuscaDados.partidas()
        jogosclubes = json.loads(jogosclubes)
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
