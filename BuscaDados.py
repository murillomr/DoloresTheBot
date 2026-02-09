import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/79.0'}
proxies = {"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"}

class BuscaDados():
    @classmethod
    def jogadores(cls):
        url = 'https://api.cartolafc.globo.com/atletas/mercado'
        #resposta = requests.get(url, proxies=proxies, headers=headers, verify=False)
        resposta = requests.get(url, headers=headers)
        #print(resposta.content)
        r = resposta.content
        #print(r)
        jogado = r.decode('utf-8')
        return jogado

    @classmethod
    def statusmercado(cls):
        url = 'https://api.cartolafc.globo.com/mercado/status'
        #resposta = requests.get(url, headers=headers, proxies=proxies, verify=False)
        resposta = requests.get(url, headers=headers)
        r = resposta.content
        #print(r)
        statusmer = r.decode('utf-8')
        #print(statusmer)
        return statusmer

    @classmethod
    def partidas(cls):
        url = 'https://api.cartolafc.globo.com/partidas'
        #resposta = requests.get(url, headers=headers, proxies=proxies, verify=False)
        resposta = requests.get(url, headers=headers)
        r = resposta.content
        #print(r)
        jogos = r.decode('utf-8')
        #print(jogos)
        return jogos

    @classmethod
    def patrimonio(cls):
        url = 'https://api.cartolafc.globo.com/auth/time'
        resposta = requests.get(url, headers=headers_auth)
        r = resposta.content
        #print(r)
        patrimonio = r.decode('utf-8')
        patrimonio = json.loads(patrimonio)
        return patrimonio['patrimonio']

    @classmethod
    def escalar(cls, jogadores, capitao, time):
        url = 'https://api.cartolafc.globo.com/auth/time/salvar'
        payload_time = {"esquema":3,"atletas":jogadores,"capitao":capitao}
        requisicao = requests.post(url, proxies=proxies, verify=False, headers=headers_auth, data=json.dumps(payload_time))
        escalado = 'O ' + time + ' foi escalado'
        return escalado

