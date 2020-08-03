import json
from BuscaDados import BuscaDados

class Filtragem():
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
        print(provaveis)
        return provaveis

#Filtragem.Provaveis()