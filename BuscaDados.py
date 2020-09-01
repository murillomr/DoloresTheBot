import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/79.0'}
proxies = {"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"}

class BuscaDados():
    @classmethod
    def jogadores(cls):
        url = 'https://api.cartolafc.globo.com/atletas/mercado/'
#       resposta = requests.get(url, proxies=proxies, headers=headers, verify=False)
        resposta = requests.get(url, headers=headers)
        #print(resposta.content)
        r = resposta.content
        #print(r)
        jogado = r.decode('utf-8')
        #print(jogado)
        return jogado

    @classmethod
    def statusmercado(cls):
        url = 'https://api.cartolafc.globo.com/mercado/status'
        resposta = requests.get(url, headers=headers)
        r = resposta.content
        #print(r)
        statusmer = r.decode('utf-8')
        #print(statusmer)
        return statusmer

    @classmethod
    def partidas(cls):
        url = 'https://api.cartolafc.globo.com/partidas'
        resposta = requests.get(url, headers=headers)
        r = resposta.content
        #print(r)
        jogos = r.decode('utf-8')
        #print(jogos)
        return jogos

#BuscaDados.jogadores()
#BuscaDados.statusmercado()
#BuscaDados.partidas()