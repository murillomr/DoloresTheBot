from Esteira_clubes import Partidas
from Filtragem import FiltragemJogosClubes

partidas = FiltragemJogosClubes.Jogos()
times = FiltragemJogosClubes.Clubes()


class Esteira():
    @classmethod
    def media_ponto(cls, jogadores):
        for i in jogadores:
            pto_media = i['media_num']
            i['score_robot'] = pto_media + i['score_robot']
        return jogadores

    @classmethod
    def qtd_jogos(cls, jogadores):
        for i in jogadores:
            qtd_jogos = i['jogos_num'] * 0.3
            i['score_robot'] = qtd_jogos + i['score_robot']
        return jogadores

    @classmethod
    def desvalorizou(cls, jogadores):
        for i in jogadores:
            if i['variacao_num'] < 0:
                i['score_robot'] = 2 + i['score_robot']
            else:
                pass
        return jogadores

    @classmethod
    def gols(cls, jogadores):
        for i in jogadores:
            scouts = i['scout']
            try:
                gols = scouts['G'] * 0.4
                i['score_robot'] = gols + i['score_robot']
            except:
                pass
        return jogadores

    @classmethod
    def cartoes(cls, jogadores):
        for i in jogadores:
            scouts = i['scout']
            try:
                amarelo = scouts['CA'] * 0.2
                i['score_robot'] = i['score_robot'] - amarelo
            except:
                pass
            try:
                vermelho = scouts['CV'] * 0.4
                i['score_robot'] = i['score-robot'] - vermelho
            except:
                pass
        return jogadores

    @classmethod
    def faltas(cls, jogadores):
        for i in jogadores:
            scouts = i['scout']
            try:
                faltas = scouts['FC'] * 0.03
                i['score_robot'] = i['score_robot'] - faltas
            except:
                pass
        return jogadores

    @classmethod
    def finalizacoes(cls, jogadores):
        for i in jogadores:
            scouts = i['scout']
            try:
                finalizacao = scouts['FS'] * 0.2
                i['score_robot'] = finalizacao + i['score_robot']
            except:
                pass
        return jogadores

    @classmethod
    def assistencias(cls, jogadores):
        for i in jogadores:
            scouts = i['scout']
            try:
                assistencia = scouts['A'] * 0.2
                i['score_robot'] = assistencia + i['score_robot']
            except:
                pass
        return jogadores

    @classmethod
    def desarmes(cls, jogadores):
        for i in jogadores:
            scouts = i['scout']
            try:
                desarme = scouts['DS'] * 0.03
                i['score_robot'] = desarme + i['score_robot']
            except:
                pass
        return jogadores

    @classmethod
    def mandante(cls, jogadores):
        mandantes = Partidas.mandantes(partidas)
        for i in jogadores:
            if i['clube_id'] in mandantes:
                i['score_robot'] = i['score_robot'] + 2
            else:
                pass
        return jogadores

    @classmethod
    def posicaotime(cls, jogadores):
        GetPosicao = Partidas.filtro_times()
        libertadores = GetPosicao['libertadores']
        prelibertadores = GetPosicao['preliberta']
        sulamericana = GetPosicao['sulamericana']
        neutros = GetPosicao['neutro']
        z4 = GetPosicao['z4']
        for i in jogadores:
            clube_id = i['clube_id']
            if clube_id in libertadores:
                i['score_robot'] = i['score_robot'] + 3
            elif clube_id in prelibertadores:
                i['score_robot'] = i['score_robot'] + 1.5
            elif clube_id in sulamericana:
                i['score_robot'] = i['score_robot'] + 0.3
            elif clube_id in neutros:
                i['score_robot'] = i['score_robot'] - 1
            elif clube_id in z4:
                i['score_robot'] = i['score_robot'] - 2
        return jogadores

    @classmethod
    def adversario(cls, jogadores):
        GetPosicao = Partidas.filtro_times()
        liberta = GetPosicao['libertadores']
        preliberta = GetPosicao['preliberta']
        sula = GetPosicao['sulamericana']
        neutro = GetPosicao['neutro']
        z4 = GetPosicao['z4']
        for i in jogadores:
            clube_id = i['clube_id']
            for w in partidas:
                # print(w['clube_casa_id'])
                if clube_id == w['clube_casa_id']:
                    rival_id = w['clube_visitante_id']
                else:
                    rival_id = w['clube_casa_id']
                if rival_id in liberta:
                    i['score_robot'] = i['score_robot'] - 2
                elif rival_id in preliberta:
                    i['score_robot'] = i['score_robot'] - 1
                elif rival_id in sula:
                    i['score_robot'] = i['score_robot'] + 0.3
                elif rival_id in neutro:
                    i['score_robot'] = i['score_robot'] + 1.5
                elif rival_id in z4:
                    i['score_robot'] = i['score_robot'] + 3
                else:
                    pass
        return jogadores

    #####################################################################################################
    ## Daqui pra frente os metodos nao sao usados, obsoletos.. todos estado dentro do def posicaotime()
    ##
    #####################################################################################################

    @classmethod
    def libertadores(cls, jogadores):
        libertadores = Partidas.libertadores(times)
        for i in jogadores:
            if i['clube_id'] in libertadores:
                i['score_robot'] = i['score_robot'] + 2
            else:
                pass
        return jogadores

    @classmethod
    def prelibertadores(cls, jogadores):
        prelibertadores = Partidas.pre_libertadores(times)
        for i in jogadores:
            if i['clube_id'] in prelibertadores:
                i['score_robot'] = i['score_robot'] + 1
            else:
                pass
        return jogadores

    @classmethod
    def sulamericana(cls, jogadores):
        sulamericana = Partidas.sulamericana(times)
        for i in jogadores:
            if i['clube_id'] in sulamericana:
                i['score_robot'] = i['score_robot'] + 0.3
            else:
                pass
        return jogadores

    @classmethod
    def neutros(cls, jogadores):
        neutros = Partidas.neutro(times)
        for i in jogadores:
            if i['clube_id'] in neutros:
                i['score_robot'] = i['score_robot'] - 1
            else:
                pass
        return jogadores

    @classmethod
    def rebaixamento(cls, jogadores):
        z4 = Partidas.rebaixamento(times)
        for i in jogadores:
            if i['clube_id'] in z4:
                i['score_robot'] = i['score_robot'] - 2
            else:
                pass
        return jogadores
