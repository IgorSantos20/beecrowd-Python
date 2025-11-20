import math

valor = float(input())
# Converter para inteiro (em centavos) para evitar imprecisão, somando um pequeno valor para lidar com casos de arredondamento
valor_centavos = int(valor * 100 + 0.001)

notas = [10000, 5000, 2000, 1000, 500, 200] # Valores em centavos
moedas = [100, 50, 25, 10, 5, 1] # Valores em centavos

print("NOTAS:")
for nota in notas:
    quantidade = valor_centavos // nota
    print(f"{quantidade} nota(s) de R$ {nota/100:.2f}")
    valor_centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    quantidade = valor_centavos // moeda
    print(f"{quantidade} moeda(s) de R$ {moeda/100:.2f}")
    valor_centavos %= moeda
