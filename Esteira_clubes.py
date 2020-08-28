
class Partidas():
    @classmethod
    def mandantes(cls, partidas):
        mandante_id = []
        for i in partidas:
            mandante_id.append(i['clube_casa_id'])
        return mandante_id

    @classmethod
    def libertadores(cls, clubes):
        clubes_validos = ['262', '263', '264', '265', '266', '267', '275', '276', '277', '280',
                          '282', '284', '285', '290', '292', '293', '294', '354', '356', '373']
        clubes_libertadores = []
        for i in clubes_validos:
            liberta = clubes[i]
            if liberta['posicao'] < 5:
                clubes_libertadores.append(liberta['id'])
        return clubes_libertadores

    @classmethod
    def pre_libertadores(cls, clubes):
        clubes_validos = ['262', '263', '264', '265', '266', '267', '275', '276', '277', '280',
                          '282', '284', '285', '290', '292', '293', '294', '354', '356', '373']
        clubes_prelibertadores = []
        for i in clubes_validos:
            preliberta = clubes[i]
            if preliberta['posicao'] == 5 or preliberta['posicao'] == 6 or preliberta['posicao'] == 7:
                clubes_prelibertadores.append(preliberta['id'])
        return clubes_prelibertadores

    @classmethod
    def sulamericana(cls, clubes):
        clubes_validos = ['262', '263', '264', '265', '266', '267', '275', '276', '277', '280',
                          '282', '284', '285', '290', '292', '293', '294', '354', '356', '373']
        clubes_sulamericana = []
        for i in clubes_validos:
            sulamericana = clubes[i]
            if sulamericana['posicao'] > 7 and sulamericana['posicao'] < 13:
                clubes_sulamericana.append(sulamericana['id'])
        return clubes_sulamericana

    @classmethod
    def neutro(cls, clubes):
        clubes_validos = ['262', '263', '264', '265', '266', '267', '275', '276', '277', '280',
                          '282', '284', '285', '290', '292', '293', '294', '354', '356', '373']
        clubes_neutros = []
        for i in clubes_validos:
            neutros = clubes[i]
            if neutros['posicao'] > 12 and neutros['posicao'] < 17:
                clubes_neutros.append(neutros['id'])
        return clubes_neutros

    @classmethod
    def rebaixamento(cls, clubes):
        clubes_validos = ['262', '263', '264', '265', '266', '267', '275', '276', '277', '280',
                          '282', '284', '285', '290', '292', '293', '294', '354', '356', '373']
        clubes_rebaixamento = []
        for i in clubes_validos:
            rebaixamento = clubes[i]
            if rebaixamento['posicao'] > 16:
                clubes_rebaixamento.append(rebaixamento['id'])
        return clubes_rebaixamento
