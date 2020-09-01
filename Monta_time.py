from Orquestrador import Orquestra

Ataque = Orquestra.Atacantes()
Meia = Orquestra.Meias()

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

print(Atk1)
print(Atk2)
print(Atk3)
print(Preco_atk1 + Preco_atk2 + Preco_atk3)