valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

print(f"TRIANGULO: {a*c/2:.3f}")
print(f"CIRCULO: {3.14159*c**2:.3f}")
print(f"TRAPEZIO: {(a+b)*c/2:.3f}")
print(f"QUADRADO: {b*b:.3f}")
print(f"RETANGULO: {a*b:.3f}")