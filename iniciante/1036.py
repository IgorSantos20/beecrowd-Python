from math import sqrt

valores = input().split()

valores_float = list(map(float, valores))

a = valores_float[0]
b = valores_float[1]
c = valores_float[2]

delta = pow(b, 2) - 4 * a * c

try:
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a)

    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")
except:
    print("Impossivel calcular")
