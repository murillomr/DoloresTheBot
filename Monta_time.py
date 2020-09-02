from Orquestrador import Orquestra

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
except:
    Time2_preco = 900
try:
    Time3_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat1 + Preco_lat2 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol2 + Preco_tec2
except:
    Time3_preco = 900
try:
    Time4_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat1 + Preco_lat2 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
except:
    Time4_preco = 900
try:
    Time5_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei1 + Preco_mei2 + Preco_mei3 + Preco_lat4 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
except:
    Time5_preco = 900
try:
    Time6_preco = Preco_atk1 + Preco_atk2 + Preco_atk3 + Preco_mei3 + Preco_mei4 + Preco_mei5 + Preco_lat4 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
except:
    Time6_preco = 900
try:
    Time7_preco = Preco_atk1 + Preco_atk4 + Preco_atk5 + Preco_mei3 + Preco_mei4 + Preco_mei5 + Preco_lat4 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag3 + Preco_gol3 + Preco_tec3
except:
    Time7_preco = 900
try:
    Time8_preco = Preco_atk2 + Preco_atk4 + Preco_atk3 + Preco_mei1 + Preco_mei4 + Preco_mei2 + Preco_lat5 + Preco_lat3 \
                  + Preco_zag4 + Preco_zag5 + Preco_gol4 + Preco_tec4
except:
    Time8_preco = 900
try:
    Time9_preco = Preco_atk2 + Preco_atk1 + Preco_atk5 + Preco_mei3 + Preco_mei4 + Preco_mei2 + Preco_lat5 + Preco_lat4 \
                  + Preco_zag2 + Preco_zag5 + Preco_gol5 + Preco_tec5
except:
    Time9_preco = 900
try:
    Time10_preco = Preco_atk5 + Preco_atk4 + Preco_atk3 + Preco_mei5 + Preco_mei4 + Preco_mei3 + Preco_lat5 + Preco_lat4 \
                  + Preco_zag4 + Preco_zag5 + Preco_gol5 + Preco_tec5
except:
    Time10_preco = 900


print(Time1_preco)
print(Time2_preco)
print(Time3_preco)
print(Time4_preco)
print(Time5_preco)
print(Time6_preco)
print(Time7_preco)
print(Time8_preco)
print(Time9_preco)


#print(Atk1)
#print(Atk2)
#print(Atk3)
#print(Preco_atk1 + Preco_atk2 + Preco_atk3)