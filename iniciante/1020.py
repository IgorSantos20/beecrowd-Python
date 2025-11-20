idade_dias = int(input())

ano = idade_dias // 365
resto = idade_dias % 365

mes = resto // 30
resto = resto % 30

dias = resto

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")