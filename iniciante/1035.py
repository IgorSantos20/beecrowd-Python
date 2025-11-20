valores = input().split()

valores_inteiros = list(map(int, valores))

a = valores_inteiros[0]
b = valores_inteiros[1]
c = valores_inteiros[2]
d = valores_inteiros[3]

if b > c and d > a and c + d > a + b and c >= 0 and d >= 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")