import datetime as dt


print(dt.time(10, 6, 21, 7), 'Hora:minuto:segundo.microsegundo')
print(dt.date(2020, 4, 25), 'Ano-mes-dia')
print('-'*50)
print(dt.datetime(2020, 4, 25, 12, 6, 21, 7), 'ano-mes-dia hora:minuto:segundo.microsendo')

natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1,1)

print((reveillon - natal))
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)


