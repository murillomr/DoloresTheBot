from BuscaDados import BuscaDados
from Esteira_jogador import Esteira
from Esteira_clubes import Partidas
from Filtragem import FiltragemJogadores, FiltragemJogosClubes


class Orquestra():
    @classmethod
    def Atacantes(cls):
        Filtro = FiltragemJogadores.Atacantes()
        Media_pt = Esteira.media_ponto(Filtro)
        Qtd_jogos = Esteira.qtd_jogos(Media_pt)
        Desval = Esteira.desvalorizou(Qtd_jogos)
        Gols = Esteira.gols(Desval)
        Cartoes = Esteira.cartoes(Gols)
        Faltas = Esteira.faltas(Cartoes)
        Finalizacoes = Esteira.finalizacoes(Faltas)
        Assists = Esteira.assistencias(Finalizacoes)
        Desarmes = Esteira.desarmes(Assists)
        Mandante = Esteira.mandante(Desarmes)
        Clube = Esteira.posicaotime(Mandante)
        ResultadoFinal = Esteira.adversario(Clube)
        lista = []
        for i in ResultadoFinal:
            lista.append(i['score_robot'])
            if i['score_robot'] > 8:
                score = str(i['score_robot'])
                score = score[:4]
                print("O jogador " + i['apelido'] + " esta com " + score + " pontos")
            else:
                pass
        # return lista
        lista_sort = sorted(lista, reverse=True)
        x = 0
        pontuacao_final = []
        while x < 5:
            print(str(lista_sort[x]))
            pontuacao_final.append(lista_sort[x])
            x = x + 1
        print(pontuacao_final)
        print(pontuacao_final[0])
        dic_final = {"qualificados": []}
        for i in ResultadoFinal:
            if pontuacao_final[0] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o maior pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 1})
            elif pontuacao_final[1] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o segundo pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 2})
            elif pontuacao_final[2] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o terceiro pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 3})
            elif pontuacao_final[3] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quarto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 4})
            elif pontuacao_final[4] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quinto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 5})
            else:
                pass
        print(dic_final)
        return dic_final

    @classmethod
    def Meias(cls):
        Filtro = FiltragemJogadores.Meias()
        Media_pt = Esteira.media_ponto(Filtro)
        Qtd_jogos = Esteira.qtd_jogos(Media_pt)
        Desval = Esteira.desvalorizou(Qtd_jogos)
        Gols = Esteira.gols(Desval)
        Cartoes = Esteira.cartoes(Gols)
        Faltas = Esteira.faltas(Cartoes)
        Finalizacoes = Esteira.finalizacoes(Faltas)
        Assists = Esteira.assistencias(Finalizacoes)
        Desarmes = Esteira.desarmes(Assists)
        Mandante = Esteira.mandante(Desarmes)
        Clube = Esteira.posicaotime(Mandante)
        ResultadoFinal = Esteira.adversario(Clube)
        lista = []
        for i in ResultadoFinal:
            lista.append(i['score_robot'])
            if i['score_robot'] > 8:
                score = str(i['score_robot'])
                score = score[:4]
                print("O jogador " + i['apelido'] + " esta com " + score + " pontos")
            else:
                pass
        # return lista
        lista_sort = sorted(lista, reverse=True)
        x = 0
        pontuacao_final = []
        while x < 5:
            print(str(lista_sort[x]))
            pontuacao_final.append(lista_sort[x])
            x = x + 1
        # print(pontuacao_final)
        # print(pontuacao_final[0])
        dic_final = {"qualificados": []}
        for i in ResultadoFinal:
            if pontuacao_final[0] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o maior pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 1})
            elif pontuacao_final[1] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o segundo pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 2})
            elif pontuacao_final[2] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o terceiro pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 3})
            elif pontuacao_final[3] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quarto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 4})
            elif pontuacao_final[4] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quinto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 5})
            else:
                pass
        print(dic_final)
        return dic_final

    @classmethod
    def Laterais(cls):
        Filtro = FiltragemJogadores.Laterais()
        Media_pt = Esteira.media_ponto(Filtro)
        Qtd_jogos = Esteira.qtd_jogos(Media_pt)
        Desval = Esteira.desvalorizou(Qtd_jogos)
        Gols = Esteira.gols(Desval)
        Cartoes = Esteira.cartoes(Gols)
        Faltas = Esteira.faltas(Cartoes)
        Finalizacoes = Esteira.finalizacoes(Faltas)
        Assists = Esteira.assistencias(Finalizacoes)
        Desarmes = Esteira.desarmes(Assists)
        Mandante = Esteira.mandante(Desarmes)
        Clube = Esteira.posicaotime(Mandante)
        ResultadoFinal = Esteira.adversario(Clube)
        lista = []
        for i in ResultadoFinal:
            lista.append(i['score_robot'])
            if i['score_robot'] > 8:
                score = str(i['score_robot'])
                score = score[:4]
                #print("O jogador " + i['apelido'] + " esta com " + score + " pontos")
            else:
                pass
        # return lista
        lista_sort = sorted(lista, reverse=True)
        x = 0
        pontuacao_final = []
        while x < 5:
            print(str(lista_sort[x]))
            pontuacao_final.append(lista_sort[x])
            x = x + 1
        # print(pontuacao_final)
        # print(pontuacao_final[0])
        dic_final = {"qualificados": []}
        for i in ResultadoFinal:
            if pontuacao_final[0] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o maior pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 1})
            elif pontuacao_final[1] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o segundo pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 2})
            elif pontuacao_final[2] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o terceiro pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 3})
            elif pontuacao_final[3] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quarto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 4})
            elif pontuacao_final[4] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quinto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 5})
            else:
                pass
        print(dic_final)
        return dic_final

    @classmethod
    def Zagueiros(cls):
        Filtro = FiltragemJogadores.Zagueiros()
        Media_pt = Esteira.media_ponto(Filtro)
        Qtd_jogos = Esteira.qtd_jogos(Media_pt)
        Desval = Esteira.desvalorizou(Qtd_jogos)
        Gols = Esteira.gols(Desval)
        Cartoes = Esteira.cartoes(Gols)
        Faltas = Esteira.faltas(Cartoes)
        Finalizacoes = Esteira.finalizacoes(Faltas)
        Assists = Esteira.assistencias(Finalizacoes)
        Desarmes = Esteira.desarmes(Assists)
        Mandante = Esteira.mandante(Desarmes)
        Clube = Esteira.posicaotime(Mandante)
        ResultadoFinal = Esteira.adversario(Clube)
        lista = []
        for i in ResultadoFinal:
            lista.append(i['score_robot'])
            if i['score_robot'] > 8:
                score = str(i['score_robot'])
                score = score[:4]
                #print("O jogador " + i['apelido'] + " esta com " + score + " pontos")
            else:
                pass
        # return lista
        lista_sort = sorted(lista, reverse=True)
        x = 0
        pontuacao_final = []
        while x < 5:
            # print(str(lista_sort[x]))
            pontuacao_final.append(lista_sort[x])
            x = x + 1
        # print(pontuacao_final)
        # print(pontuacao_final[0])
        dic_final = {"qualificados": []}
        for i in ResultadoFinal:
            if pontuacao_final[0] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o maior pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 1})
            elif pontuacao_final[1] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o segundo pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 2})
            elif pontuacao_final[2] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o terceiro pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 3})
            elif pontuacao_final[3] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quarto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 4})
            elif pontuacao_final[4] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quinto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 5})
            else:
                pass
        print(dic_final)
        return dic_final

    @classmethod
    def Goleiros(cls):
        Filtro = FiltragemJogadores.Goleiros()
        Media_pt = Esteira.media_ponto(Filtro)
        Qtd_jogos = Esteira.qtd_jogos(Media_pt)
        Desval = Esteira.desvalorizou(Qtd_jogos)
        Gols = Esteira.gols(Desval)
        Cartoes = Esteira.cartoes(Gols)
        Faltas = Esteira.faltas(Cartoes)
        Finalizacoes = Esteira.finalizacoes(Faltas)
        Assists = Esteira.assistencias(Finalizacoes)
        Desarmes = Esteira.desarmes(Assists)
        Mandante = Esteira.mandante(Desarmes)
        Clube = Esteira.posicaotime(Mandante)
        ResultadoFinal = Esteira.adversario(Clube)
        lista = []
        for i in ResultadoFinal:
            lista.append(i['score_robot'])
            if i['score_robot'] > 8:
                score = str(i['score_robot'])
                score = score[:4]
                #print("O jogador " + i['apelido'] + " esta com " + score + " pontos")
            else:
                pass
        # return lista
        lista_sort = sorted(lista, reverse=True)
        x = 0
        pontuacao_final = []
        while x < 5:
            print(str(lista_sort[x]))
            pontuacao_final.append(lista_sort[x])
            x = x + 1
        print(pontuacao_final)
        print(pontuacao_final[0])
        dic_final = {"qualificados": []}
        for i in ResultadoFinal:
            if pontuacao_final[0] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o maior pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 1})
            elif pontuacao_final[1] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o segundo pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 2})
            elif pontuacao_final[2] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o terceiro pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 3})
            elif pontuacao_final[3] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quarto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 4})
            elif pontuacao_final[4] == i['score_robot']:
                print("O jogador " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quinto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 5})
            else:
                pass
        print(dic_final)
        return dic_final

    @classmethod
    def Tecnicos(cls):
        Filtro = FiltragemJogadores.Tecnicos()
        Media_pt = Esteira.media_ponto(Filtro)
        Desval = Esteira.desvalorizou(Media_pt)
        Mandante = Esteira.mandante(Desval)
        Clube = Esteira.posicaotime(Mandante)
        ResultadoFinal = Esteira.adversario(Clube)
        lista = []
        for i in ResultadoFinal:
            lista.append(i['score_robot'])
            if i['score_robot'] > 8:
                score = str(i['score_robot'])
                score = score[:4]
            else:
                pass
        # return lista
        lista_sort = sorted(lista, reverse=True)
        x = 0
        pontuacao_final = []
        while x < 5:
            print(str(lista_sort[x]))
            pontuacao_final.append(lista_sort[x])
            x = x + 1
        print(pontuacao_final)
        print(pontuacao_final[0])
        dic_final = {"qualificados": []}
        for i in ResultadoFinal:
            if pontuacao_final[0] == i['score_robot']:
                print("O tecnico " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o maior pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 1})
            elif pontuacao_final[1] == i['score_robot']:
                print("O tecnico " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o segundo pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 2})
            elif pontuacao_final[2] == i['score_robot']:
                print("O tecnico " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o terceiro pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 3})
            elif pontuacao_final[3] == i['score_robot']:
                print("O tecnico " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quarto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 4})
            elif pontuacao_final[4] == i['score_robot']:
                print("O tecnico " + i['apelido'] + " com ID " + str(i['atleta_id']) + " eh o quinto pontuador")
                dic_final["qualificados"].append(
                    {"Jogador": i['apelido'], "ID": str(i['atleta_id']), "Preco": i['preco_num'],
                     "ScoreBOT": i['score_robot'], "Posicao": 5})
            else:
                pass
        print(dic_final)
        return dic_final
