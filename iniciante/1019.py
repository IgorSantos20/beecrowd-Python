duracao_segundos = int(input())

horas = duracao_segundos // 3600
resto = duracao_segundos % 3600

minutos = resto // 60
segundos = resto % 60


print(f"{horas}:{minutos}:{segundos}")