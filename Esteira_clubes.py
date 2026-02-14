from Filtragem import FiltragemJogosClubes

libertadores = []
preliberta = []
sulamericana = []
neutro = []
z4 = []

class Partidas():
    @classmethod
    def mandantes(cls, partidas):
        mandante_id = []
        for i in partidas:
            mandante_id.append(i['clube_casa_id'])
        return mandante_id

    @classmethod
    def filtro_times(cls):
        filtra = FiltragemJogosClubes.Jogos()
        for i in filtra:
            if i['clube_casa_posicao'] < 5:
                libertadores.append(i['clube_casa_id'])
            if 4 < i['clube_casa_posicao'] < 7:
                preliberta.append(i['clube_casa_id'])
            if 6 < i['clube_casa_posicao'] < 13:
                sulamericana.append(i['clube_casa_id'])
            if 12 < i['clube_casa_posicao'] < 17:
                neutro.append(i['clube_casa_id'])
            if i['clube_casa_posicao'] > 16:
                z4.append(i['clube_casa_id'])
            if i['clube_visitante_posicao'] < 5:
                libertadores.append(i['clube_visitante_id'])
            if 4 < i['clube_visitante_posicao'] < 7:
                preliberta.append(i['clube_visitante_id'])
            if 6 < i['clube_visitante_posicao'] < 13:
                sulamericana.append(i['clube_visitante_id'])
            if 12 < i['clube_visitante_posicao'] < 17:
                neutro.append(i['clube_visitante_id'])
            if i['clube_visitante_posicao'] > 16:
                z4.append(i['clube_visitante_id'])
        return {'libertadores': libertadores, 'preliberta': preliberta, 'sulamericana': sulamericana,
                'neutro': neutro, 'z4': z4}

