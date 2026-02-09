from Orquestrador import Orquestra
from BuscaDados import BuscaDados

Ataque = Orquestra.Atacantes()
Meia = Orquestra.Meias()
Lateral = Orquestra.Laterais()
Zaga = Orquestra.Zagueiros()
Gol = Orquestra.Goleiros()
Tecnico = Orquestra.Tecnicos()

for i in Ataque['qualificados']:
    if i['Posicao'] == 1:
        Atk1 = i['ID']
        Preco_atk1 = i['Preco']
    elif i['Posicao'] == 2:
        Atk2 = i['ID']
        Preco_atk2 = i['Preco']
    elif i['Posicao'] == 3:
        Atk3 = i['ID']
        Preco_atk3 = i['Preco']
    elif i['Posicao'] == 4:
        Atk4 = i['ID']
        Preco_atk4 = i['Preco']
    elif i['Posicao'] == 5:
        Atk5 = i['ID']
        Preco_atk5 = i['Preco']
    else:
        pass


for i in Meia['qualificados']:
    if i['Posicao'] == 1:
        Mei1 = i['ID']
        Preco_mei1 = i['Preco']
    elif i['Posicao'] == 2:
        Mei2 = i['ID']
        Preco_mei2 = i['Preco']
    elif i['Posicao'] == 3:
        Mei3 = i['ID']
        Preco_mei3 = i['Preco']
    elif i['Posicao'] == 4:
        Mei4 = i['ID']
        Preco_mei4 = i['Preco']
    elif i['Posicao'] == 5:
        Mei5 = i['ID']
        Preco_mei5 = i['Preco']
    else:
        pass


for i in Lateral['qualificados']:
    if i['Posicao'] == 1:
        Lat1 = i['ID']
        Preco_lat1 = i['Preco']
    elif i['Posicao'] == 2:
        Lat2 = i['ID']
        Preco_lat2 = i['Preco']
    elif i['Posicao'] == 3:
        Lat3 = i['ID']
        Preco_lat3 = i['Preco']
    elif i['Posicao'] == 4:
        Lat4 = i['ID']
        Preco_lat4 = i['Preco']
    elif i['Posicao'] == 5:
        Lat5 = i['ID']
        Preco_lat5 = i['Preco']
    else:
        pass


for i in Zaga['qualificados']:
    if i['Posicao'] == 1:
        Zag1 = i['ID']
        Preco_zag1 = i['Preco']
    elif i['Posicao'] == 2:
        Zag2 = i['ID']
        Preco_zag2 = i['Preco']
    elif i['Posicao'] == 3:
        Zag3 = i['ID']
        Preco_zag3 = i['Preco']
    elif i['Posicao'] == 4:
        Zag4 = i['ID']
        Preco_zag4 = i['Preco']
    elif i['Posicao'] == 5:
        Zag5 = i['ID']
        Preco_zag5 = i['Preco']
    else:
        pass

for i in Gol['qualificados']:
    if i['Posicao'] == 1:
        Gol1 = i['ID']
        Preco_gol1 = i['Preco']
    elif i['Posicao'] == 2:
        Gol2 = i['ID']
        Preco_gol2 = i['Preco']
    elif i['Posicao'] == 3:
        Gol3 = i['ID']
        Preco_gol3 = i['Preco']
    elif i['Posicao'] == 4:
        Gol4 = i['ID']
        Preco_gol4 = i['Preco']
    elif i['Posicao'] == 5:
        Gol5 = i['ID']
        Preco_gol5 = i['Preco']
    else:
        pass

for i in Tecnico['qualificados']:
    if i['Posicao'] == 1:
        Tec1 = i['ID']
        Preco_tec1 = i['Preco']
    elif i['Posicao'] == 2:
        Tec2 = i['ID']
        Preco_tec2 = i['Preco']
    elif i['Posicao'] == 3:
        Tec3 = i['ID']
        Preco_tec3 = i['Preco']
    elif i['Posicao'] == 4:
        Tec4 = i['ID']
        Preco_tec4 = i['Preco']
    elif i['Posicao'] == 5:
        Tec5 = i['ID']
        Preco_tec5 = i['Preco']
    else:
        pass

try:
    Time1_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat1 + Preco_lat2 \
              + Preco_zag1 + Preco_zag2 + Preco_gol1 + Preco_tec1
    Time1 = [Tec1, Gol1, Zag2, Zag1, Lat2, Lat1, Mei3, Mei2, Mei1, Atk3, Atk2, Atk1]
    Capitao_time1 = Atk1
except:
    Time1_preco = 900
try:
    Time2_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat1 + Preco_lat2 \
                  + Preco_zag1 + Preco_zag2 + Preco_gol2 + Preco_tec2
    Time2 = [Tec2, Gol2, Zag2, Zag1, Lat2, Lat1, Mei3, Mei2, Mei1, Atk3, Atk2, Atk1]
    Capitao_time2 = Atk1
except:
    Time2_preco = 900
try:
    Time3_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat1 + Preco_lat2 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol2 + Preco_tec2
    Time3 = [Tec2, Gol2, Zag3, Zag4, Lat2, Lat1, Mei3, Mei2, Mei1, Atk3, Atk2, Atk1]
    Capitao_time3 = Atk1
except:
    Time3_preco = 900
try:
    Time4_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat1 + Preco_lat2 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
    Time4 = [Tec3, Gol3, Zag3, Zag4, Lat2, Lat1, Mei3, Mei2, Mei1, Atk3, Atk2, Atk1]
    Capitao_time4 = Atk1
except:
    Time4_preco = 900
try:
    Time5_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat4 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
    Time5 = [Tec3, Gol3, Zag3, Zag4, Lat4, Lat3, Mei3, Mei2, Mei1, Atk3, Atk2, Atk1]
    Capitao_time5 = Atk1
except:
    Time5_preco = 900
try:
    Time6_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei3 + Preco_mei4 + Preco_mei5 + Preco_lat4 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
    Time6 = [Tec3, Gol3, Zag3, Zag4, Lat4, Lat3, Mei3, Mei4, Mei5, Atk3, Atk2, Atk1]
    Capitao_time6 = Atk1
except:
    Time6_preco = 900
try:
    Time7_preco = Preco_atk1 + Preco_atk4 + Preco_atk5 + Preco_mei3 + Preco_mei4 + Preco_mei5 + Preco_lat4 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
    Time7 = [Tec3, Gol3, Zag3, Zag4, Lat4, Lat3, Mei3, Mei4, Mei5, Atk4, Atk5, Atk1]
    Capitao_time7 = Atk1
except:
    Time7_preco = 900
try:
    Time8_preco = Preco_atk2 + Preco_atk4 + Preco_atk3 + Preco_mei1 + Preco_mei4 + Preco_mei2 + Preco_lat5 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag5 + Preco_gol4 + Preco_tec4
    Time8 = [int(Tec4), int(Gol4), int(Zag5), int(Zag4), int(Lat5), int(Lat3), int(Mei1), int(Mei4), int(Mei2), int(Atk4), int(Atk3), int(Atk2)]
    Capitao_time8 = int(Atk2)
except:
    Time8_preco = 900
try:
    Time9_preco = Preco_atk2 + Preco_atk1 + Preco_atk5 + Preco_mei3 + Preco_mei4 + Preco_mei2 + Preco_lat5 + Preco_lat4 \
                  + Preco_zag2 + Preco_zag5 + Preco_gol5 + Preco_tec5
    Time9 = [Tec5, Gol5, Zag5, Zag2, Lat5, Lat4, Mei2, Mei3, Mei4, Atk5, Atk1, Atk2]
    Capitao_time9 = Atk1
except:
    Time9_preco = 900
try:
    Time10_preco = Preco_atk5 + Preco_atk4 + Preco_atk3 + Preco_mei5 + Preco_mei4 + Preco_mei3 + Preco_lat5 + Preco_lat4 \
                  + Preco_zag4 + Preco_zag5 + Preco_gol5 + Preco_tec5
    Time10 = [Tec5, Gol5, Zag5, Zag4, Lat5, Lat4, Mei5, Mei3, Mei4, Atk5, Atk4, Atk3]
    Capitao_time10 = Atk3
except:
    Time10_preco = 900
try:
    Time11_preco = Preco_atk5 + Preco_atk2 + Preco_atk3 + Preco_mei5 + Preco_mei2 + Preco_mei3 + Preco_lat5 + Preco_lat2 \
                  + Preco_zag3 + Preco_zag5 + Preco_gol1 + Preco_tec1
    Time11 = [Tec1, Gol1, Zag5, Zag3, Lat5, Lat2, Mei5, Mei3, Mei2, Atk5, Atk2, Atk3]
    Capitao_time11 = Atk2
except:
    Time11_preco = 900


patrimonio = BuscaDados.patrimonio()
#patrimonio = 114
print(patrimonio)

if patrimonio > Time1_preco:
    print("funcao de escalar time1")
    BuscaDados.escalar(jogadores=Time1, capitao=Capitao_time1, time='time1')
elif patrimonio > Time2_preco:
    print("time2")
    BuscaDados.escalar(jogadores=Time2, capitao=Capitao_time2, time='time2')
elif patrimonio > Time3_preco:
    print("time3")
    BuscaDados.escalar(jogadores=Time3, capitao=Capitao_time3, time='time3')
elif patrimonio > Time4_preco:
    print("time4")
    BuscaDados.escalar(jogadores=Time4, capitao=Capitao_time4, time='time4')
elif patrimonio > Time5_preco:
    print("time5")
    BuscaDados.escalar(jogadores=Time5, capitao=Capitao_time5, time='time5')
elif patrimonio > Time6_preco:
    print("time6")
    BuscaDados.escalar(jogadores=Time6, capitao=Capitao_time6, time='time6')
elif patrimonio > Time7_preco:
    print("time7")
    BuscaDados.escalar(jogadores=Time7, capitao=Capitao_time7, time='time7')
elif patrimonio > Time8_preco:
    print("time8")
    BuscaDados.escalar(jogadores=Time8, capitao=Capitao_time8, time='time8')
elif patrimonio > Time9_preco:
    print("time9")
    BuscaDados.escalar(jogadores=Time9, capitao=Capitao_time9, time='time9')
elif patrimonio > Time10_preco:
    print("time10")
    BuscaDados.escalar(jogadores=Time10, capitao=Capitao_time10, time='time10')
elif patrimonio > Time11_preco:
    print("time11")
    BuscaDados.escalar(jogadores=Time11, capitao=Capitao_time11, time='time11')
else:
    print("todos times sao mais caros:", Time1_preco, Time2_preco, Time3_preco, Time4_preco, Time5_preco, Time6_preco,
          Time7_preco, Time8_preco, Time9_preco, Time10_preco, Time11_preco)


'''
print(Time1_preco)
print(Time2_preco)
print(Time3_preco)
print(Time4_preco)
print(Time5_preco)
print(Time6_preco)
print(Time7_preco)
print(Time8_preco)
print(Time9_preco)
print(Time10_preco)
print(Time11_preco)
'''

#print(Atk1)
#print(Atk2)
#print(Atk3)
#print(Preco_atk1 + Preco_atk2 + Preco_atk3)