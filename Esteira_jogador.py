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
                i['score_robot'] = 0.6 + i['score_robot']
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