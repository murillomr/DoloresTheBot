from Filtragem import FiltragemMercado


Status = FiltragemMercado.Statusmercado()

if Status == 1:
    print('aberto')
elif Status == 2:
    print('fechado')
else:
    print('erro na requisiçao')