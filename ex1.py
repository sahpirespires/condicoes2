placar1 =int(input('Digite os gols do time1:'))
placar2= int(input('Digite os gols do time2:'))

if placar1 == placar2:
    print("empate")

elif placar1 > placar2:
    print("time1 tem a vitoria")
else:
    print(f"{placar2} tem a vitoria")


