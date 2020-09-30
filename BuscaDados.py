import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/79.0'}
headers_auth = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/79.0', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJXLUppTjhfZXdyWE9uVnJFN2lfOGpIY28yU1R4dEtHZF94aW01R2N4WS1ZIn0.eyJqdGkiOiIzM2ZjYTc2OS00MzBkLTQ5ZGItYjljYy00NzFkY2E1MjU1ZjgiLCJleHAiOjE2MDM1OTMwNzIsIm5iZiI6MCwiaWF0IjoxNjAxMDAxMDcyLCJpc3MiOiJodHRwczovL2lkLmdsb2JvLmNvbS9hdXRoL3JlYWxtcy9nbG9iby5jb20iLCJzdWIiOiJmOjNjZGVhMWZiLTAwMmYtNDg5ZS1iOWMyLWQ1N2FiYTBhZTQ5NDo0NGM0MzNmYi1mNDFiLTQxY2QtOTMzNS0zOWIyMWE2MTlkZTQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjYXJ0b2xhQGFwcHMuZ2xvYm9pZCIsImF1dGhfdGltZSI6MTYwMTAwMTA3MCwic2Vzc2lvbl9zdGF0ZSI6ImMyMTRiMGY3LTU0NDAtNGQ0Ny1hYTBmLThmZDQxN2MzZWIzZSIsImFjciI6IjEiLCJzY29wZSI6Im9wZW5pZCBlbWFpbCBnbG9ib2lkIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJNdXJpbGxvIE1hcnRpbmV6IiwicHJlZmVycmVkX3VzZXJuYW1lIjoidXh1a3RnYW1teXltd2R2eWFsYWYiLCJmYW1pbHlfbmFtZSI6IiIsImVtYWlsIjoiNmQucm9jaGFAZ21haWwuY29tIiwiZ2xvYm9faWQiOiI0NGM0MzNmYi1mNDFiLTQxY2QtOTMzNS0zOWIyMWE2MTlkZTQifQ.Z2dQqu5PSBX1aWmUtH4lfB3Gtv8OoReUmfOCwiMbfBINjQaIREZvNQGAv9CXg0Zd3z7dDik5wgzYRMEhuqg2tfpssRLZjHv83_q7F-qVrshU-D3iGqFidtZjhvHgkAIndNzrObF4TUtaVuRVsMoBPFRFkFkMY1kapa3xnpaen5CUf1jrY-NKcfiJ67zU8Qgv5EQl3Kk_YhTwp7_hEpLFj3r29ZSWcFRtDpp1uIMF7qQq8JZYFPHgoQ0SoKco1TXgvz-JdHedYG8qwvVBpeaKRwCyBXjjJ8fC_BVkUnCIIjskblsXd3CpRuu7Y4JQeXJ4c6FnzFwI38xNK1fKswsJoA'}
headers_auth_hx = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/79.0', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJXLUppTjhfZXdyWE9uVnJFN2lfOGpIY28yU1R4dEtHZF94aW01R2N4WS1ZIn0.eyJqdGkiOiJkM2JiZTdmYy01MGJlLTQyZjYtYjVmNy05ZTRjNjk1YjkzNDkiLCJleHAiOjE2MDIwNDM1ODYsIm5iZiI6MCwiaWF0IjoxNTk5NDUxNTg2LCJpc3MiOiJodHRwczovL2lkLmdsb2JvLmNvbS9hdXRoL3JlYWxtcy9nbG9iby5jb20iLCJzdWIiOiJmOjNjZGVhMWZiLTAwMmYtNDg5ZS1iOWMyLWQ1N2FiYTBhZTQ5NDowZGQwZmY2Zi1kYjQyLTQ3NGYtOWEwNy05ODM1OWY0ODQzM2QiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjYXJ0b2xhQGFwcHMuZ2xvYm9pZCIsImF1dGhfdGltZSI6MTU5OTQ1MTU4NSwic2Vzc2lvbl9zdGF0ZSI6IjMzZjEzMDViLTg1ZGQtNDUyZC04Y2Y4LTNlMzJhNDhjMWFkMyIsImFjciI6IjEiLCJzY29wZSI6Im9wZW5pZCBlbWFpbCBnbG9ib2lkIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJNdXJpbGxvIE1hcnRpbmV6IiwicHJlZmVycmVkX3VzZXJuYW1lIjoidW91dmhtbndxbXhrZWZmdmxhcW0iLCJmYW1pbHlfbmFtZSI6IiIsImVtYWlsIjoibXVyaWxsb2h4Y3hAZ21haWwuY29tIiwiZ2xvYm9faWQiOiIwZGQwZmY2Zi1kYjQyLTQ3NGYtOWEwNy05ODM1OWY0ODQzM2QifQ.QOCW7xGhdJ6KpdRb05Qoq28AYeIHmiTsZrYd4WrhpvYHlSREZkFWopL4Ri0jxFxUb3-nlViWWK4rVeQCVdkP0z3nov6NhISzk5m0kTuT87AiOQtcOikhI1yKmh48J59sWHOxvhvf9-kPRVG4TK7kYJ30lrHBDyotzHPBR8wTnxaVRrE_b7sYqsb9qangBzjftp-gowoxdidWAVdx4ZKKSgTgP37jjmvxahu3EJdFiUnLqacoVdHYbUjsyVPRI6mWx7StGK_IFxtZGvy8NY50EGBDfqMz5athEYxoKQqLUG9oeDkhQ6DrbVNDz4mP5VleFYwt9JUMYDr2yjruuc8N-A'}
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
        #print(jogado)
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

#BuscaDados.jogadores()
#BuscaDados.statusmercado()
#BuscaDados.partidas()